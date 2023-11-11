
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

