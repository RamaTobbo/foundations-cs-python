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
            closed_tab = tabs.pop()
            print(f"last  Tab {closed_tab['title']} is closed")

# if there is no tabs so there is no content to display ,if the user enter no index so the content of the last tab will be displayed
#else if the user enter an index we will dispaly the content of the tab at that index
#if the user enter an index but invalid we will also consider it as index not provided and display the content of the last tab
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
            last_tab = tabs[-1]
            print(f"last  Tab {last_tab['title']} ")
            displayTabContent(last_tab)

# get the url than display its html content
def displayTabContent(tab):
    url=tab['url']
    response=requests.get(url)
    print(response.content)

# we should create nested tab first
# if there is no tabs so we can not open nested tab
# if there is tabs the user should specify at which tab he want to open a nested tab
#if the user enter invalid index nothing will be added
def openNestedTab():
    if len(tabs)==0:
        print("No tabs to create nested tabs.")
        return

    parent = int(input("Enter the index of the parent tab to insert nested tabs: ").strip())

    if parent <= len(tabs):
        tabs[parent]['nested_tabs'].append(createNestedTabs())

    else:
        print("Invalid parent tab index.")




# nested tab the user should enter the title and the content
def createNestedTabs():
    nested_tabs = []
    while True:
        title = input("Enter the Title for the nested tab : ")
        if len(title)==0:

            break
        content = input("Enter the content for the nested tab: ")
        nested_tabs.append({"title": title, "content": content})
    return nested_tabs
