def main():
    name=input("enter your name: ")
    print(f"welcom {name}")
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
        return 0
    elif choice=='2':
        return 0
    elif choice == '3':
        return 0
    elif choice == '4':
        return 0
    elif choice == '5':
        return 0
    elif choice == '6':
        return 0
    elif choice == '7':
        exit(0)
    else:
        print("Enter a valid option")

def add_matrices:
     rows = int(input("Enter number of rows: "))
     cols=int(input("Enter number of cols: "))
     m1=[]
     m2=[]
     print("Enter elements for the first matrix:")
     for i in range(rows):
         row=[]
         for j in range(cols):
             nbs=int(input("enter number at row {i+1},column {j+1}:"))
             row.append(nbs)
         m1.append(row)
     print("Enter elements for the second matrix:")
     for i in range(rows):
         row=[]
         for j in range(cols):
             nbs=int(input("enter number at row {i+1},column {j+1}:"))
             row.append(nbs)
         m2.append(row)
     result=[]
     for i in range(rows):
         row=[]
         for j in range(cols):
             row.append(m1[i][j]+m2[i][j])
         result.append(row)



