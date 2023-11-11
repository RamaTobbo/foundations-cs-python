import json

import requests

tabs = []
#big0(1)
def openTab():
    title = input("Enter the Title: ")
    url = input("Enter the URL: ")
    tabs.append({"title": title, "url": url, "nested_tabs": []})
#bigO(n)
def closeTab():
    if len(tabs)==0:
        print("No tabs to close ")
        return

    index =input("Enter the index of the tab to close : ").strip()

    if len(index)==0 :
        closed_tab = tabs.pop()
        print(f"last  Tab {closed_tab['title']} is closed")
    else:
        i = int(index)
        if i < len(tabs):
            closed_tab = tabs.pop(i)
            print(f"Tab {closed_tab['title']} is closed")
        else:
           print("invalid index")

# if there is no tabs so there is no content to display ,if the user enter no index so the content of the last tab will be displayed
#else if the user enter an index we will dispaly the content of the tab at that index
#if the user enter an index but invalid we will print invalid index
#displaying the content as html form so we should create a function to display the html content
#big0(1)
def switchTab():
    if len(tabs)==0:
        print("No tabs to display its content ")
        return
    index = input("Enter the index of the tab to display its content: ")
    if len(index)==0 :
        last_tab = tabs[-1]
        print(f"last  Tab {last_tab['title']} ")
        displayTabContent(last_tab)



    else:
        i = int(index)
        if i<len(tabs):

         switched_tab = tabs[i]
         print(f"Tab {switched_tab['title']} ")
         displayTabContent(switched_tab)
        else:
            print("invalid index")

# get the url than display its html content
#bigO(1)
def displayTabContent(tab):
    url=tab['url']
    response=requests.get(url)
    print(response.content)

# we should create nested tab first
# if there is no tabs so we can not open nested tab
# if there is tabs the user should specify at which tab he want to open a nested tab
#if the user enter invalid index nothing will be added
#bigO((1)
def openNestedTab():
    if len(tabs)==0:
        print("No tabs to create nested tabs.")
        return

    parent = int(input("Enter the index of the parent tab to insert nested tabs: ").strip())

    if parent < len(tabs):
        tabs[parent]['nested_tabs'].append(createNestedTabs())

    else:
        print("Invalid parent tab index.")




# nested tab the user should enter the title and the content
#bigO(n)
def createNestedTabs():
    nested_tabs = []
    while True:
        title = input("Enter the Title for the nested tab : ")
        if len(title)==0:

            break
        content = input("Enter the content for the nested tab: ")
        nested_tabs.append({"title": title, "content": content})
    return nested_tabs

#remove all elements from the list using clear() method
#bigO(1)
def clearAllTabs():
     tabs.clear()

#first we should open the file path and create a json file
# json.dump is to connect file and jason data
##bigO(n)
def saveTabs():


    file_path = input("Enter the file path to import tabs: ").strip()

    with open(file_path, 'w') as file:
             json.dump(tabs,file)
    print("Tabs are saved successfully")

#import tabs that take file path as parameter
#json.load it take a file and return an object or data
#bigO(N)
def importTabs(file_path):


    with open(file_path, 'r') as file:
             y = json.load(file)
    return y

#bigO(N)
def displayAllTabs():
    nested_tabs=[]
    if len(tabs)==0:
        print("No open tabs ")
    else:
        for opened_tab in tabs:

            print( f" Tab title: {opened_tab['title']}")
            if 'nested_tabs' in opened_tab:

                for nested in opened_tab['nested_tabs']:
                    for nested_tab in nested:

                       print(f" Tab title: {nested_tab['title']}")


def displayMenu():
    print("\nMenu:")
    print("1. Open Tab")
    print("2. Close Tab")
    print("3. Switch Tab")
    print("4. Display All Tabs")
    print("5. Open Nested Tab")
    print("6. Clear All Tabs")
    print("7. Save Tabs")
    print("8. Import Tabs")
    print("9. Exit")




#bigO(N)
def main():
    user=input("Enter your name :")
    print(f"welcome {user}")
    displayMenu()
    choice = input("Enter your choice (1-9): ").strip()

    while choice !='9':



        if choice == '1':
            openTab()
        elif choice == '2':
            closeTab()
        elif choice == '3':
            switchTab()
        elif choice == '4':
            displayAllTabs()
        elif choice == '5':
            openNestedTab()
            print(tabs)
        elif choice == '6':
            clearAllTabs()
        elif choice == '7':
            saveTabs()
        elif choice == '8':
            file_path = input("Enter the file path to import tabs: ").strip()
            loaded = importTabs(file_path)
            print("loaded")


        elif choice != '9':
            print("Invalid choice. ")
        displayMenu()
        choice = input("Enter your choice (1-9): ").strip()



main()