def main():
    name=input("enter your name: ")
    print(f"welcome {name}")
    while True:

        print("""1.Add Matrices
             2. Check Rotation
             3. Invert Dictionary
             4. Convert Matrix to Dictionary
             5. Check Palindrome
             6. Search for an Element & Merge Sort
              7. Exit
    """)
        choice=input("Choose a number between (1-7):")
        if choice =='1':
           add_matrices()
        elif choice == '2':
          is_rotation([1,2,3],[4,5,6])
        elif choice == '3':
           invert_dictionary()
        elif choice == '4':
            lsit_to_dictionary({1,2,3})
        elif choice == '5':
           print( is_palindrome("r"))
        elif choice == '6':
           search_element()
        elif choice == '7':
            exit(0)
        else:
            print("Enter a valid option")


def add_matrices():
     rows = int(input("Enter number of rows: "))
     cols=int(input("Enter number of cols: "))
     m1=[]
     m2=[]
     print("Enter elements for the first matrix:")
     for i in range(rows):
         row=[]
         for j in range(cols):
             nbs=int(input("enter number :"))
             row.append(nbs)
         m1.append(row)
     print(f"Enter elements for the second matrix:")
     for i in range(rows):
         row=[]
         for j in range(cols):
             nbs=int(input(f"enter number at row :"))
             row.append(nbs)
         m2.append(row)
     result=[]
     for i in range(rows):
         row=[]
         for j in range(cols):
             row.append(m1[i][j]+m2[i][j])
         result.append(row)
     for row in result:
         print(row)

def is_rotation(m1,m2):
    rows=1
def invert_dictionary():
    original={}
    inverted={}
    items=int(input("Enter the number of items in the dictionary:"))
    for i in range(items):
        key=input("Enter a key: ")
        value=input("Enter a value:")
        original[key]=value
    for key,value in original.items():
        if value in inverted:
            inverted[value]=key
    print(original)
    print(inverted)
def lsit_to_dictionary(info):
    dict={}
    for i in info:
        user_id=i[2]
        user=i[:2]+i[3:]
        dict[user_id]=user
    return dict
info = [["firstname1", "lastname1", "ID1", "jobtitle1", "company1"],
             ["firstname2", "lastname2", "ID2", "jobtitle2", "company2"],
             ["firstname3", "lastname3", "ID3", "jobtitle3", "company3"]]
dict=lsit_to_dictionary(info)
print(dict)
def is_palindrome(s):
    return s == s[::-1]
def search_element():
    list=[1,2]
    element=input("Enter the element you want:")
    found=False
    index=-1
    for i in (len(list)):
        if list[i]==element:
            found=True
            index=i
            break
    if found:
        print(f"Element {element} found at index {index}")
    else:
        print("element not found")

main()