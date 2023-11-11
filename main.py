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
def switchTab():
    if len(tabs)==0:
        print("No tabs to display its content ")
        return

# get the url than display its html content
def displayTabContent(tab):
    url=tab['url']
    response=requests.get(url)
    print(response.content)