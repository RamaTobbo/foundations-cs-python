
tabs = []
def openTab():
    title = input("Enter the Title: ")
    url = input("Enter the URL: ")
    tabs.append({"title": title, "url": url, "nested_tabs": []})
