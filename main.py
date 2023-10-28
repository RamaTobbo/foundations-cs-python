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
            m=[[5,2,3],[1,5,4]]
            result=matrix_to_dictionary(m)
            print(result)
        elif choice == '5':
           print( is_palindrome("a"))
        elif choice == '6':
          search_element([5,2,3],5)
        elif choice == '7':
            exit(0)
        else:
            print("Enter a valid option")


def add_matrices():
     rows = int(input("Enter number of rows: "))
     cols=int(input("Enter number of columns: "))
     m1=[]
     m2=[]
     print("Enter elements for the first matrix:")
     for i in range(rows):
         row=[]
         for j in range(cols):
             nbs=int(input("enter number at row :"))
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

def matrix_to_dictionary(matrix):
    dictionary = {}
    for i in range(len(matrix)):
        result="ID"
        dictionary[i + 1] = matrix[i]
    return dictionary


def is_palindrome(s):
    return s == s[::-1]
def search_element(list,element):
    found=False
    for i in range(len(list)):
        if list[i]==element:
            found=True
            index=i
    if found:
        print(f"element is found at index {index}")
    else:
        print(f"element not found ")


    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
                if list[j]>list[j+1]:
                    temp=list[j]
                    list[j]=list[j+1]
                    list[j+1]=temp
    print(list)






main()