def add_matrices(): #O(N^2), where N is the number of rows multiplied by the number of columns
    # Prompt for matrix size
    rows = int(input("Enter number of rows: "))  # O(1)
    columns = int(input("Enter number of columns: "))  # O(1)

    # Initialize matrices
    matrix1 = []  # O(1)
    matrix2 = []  # O(1)
    result = []  # O(1)

    # Prompt for elements of first matrix O(N^2)
    print("Enter elements of the first matrix:")
    for i in range(rows):  # O(N), where n is the number of rows * columns
        row = []
        for j in range(columns):  # O(N), where n is the number of columns
            element = int(input())
            row.append(element)
        matrix1.append(row)

    # Prompt for elements of second matrix: O(N^2)
    print("Enter elements of the second matrix:")
    for i in range(rows):  # O(N), where n is rows * columns
        row = []
        for j in range(columns):  # O(N), where n is the number of columns
            element = int(input())
            row.append(element)
        matrix2.append(row)

    # Add matrices: O(N^2)
    for i in range(rows): # O(N), where n is the number of rows * columns
        row = []
        for j in range(columns):  # O(N), where n is the number of columns
            element = matrix1[i][j] + matrix2[i][j]
            row.append(element)
        result.append(row)

    # Display result
    print("Result:")
    print(f"The result of adding {matrix1} and {matrix2} is {result}")  # O(1)


def checkRotation(): #O(N^2), where N is the number of rows multiplied by the number of columns
    # Prompt for matrix size
    rows1 = int(input("Enter number of rows for the first matrix: "))  # O(1)
    columns1 = int(input("Enter number of columns for the first matrix: "))  # O(1)

    rows2 = int(input("Enter number of rows for the second matrix: "))  # O(1)
    columns2 = int(input("Enter number of columns for the second matrix: "))  # O(1)

    # Initialize matrices
    matrix_x = []  # O(1)
    matrix_y = []  # O(1)

    # Prompt for elements of first matrix: O(N^2)
    print("Enter elements of the first matrix:")
    for i in range(rows1):  # O(N), where n is the number of rows * columns
        row = []
        for j in range(columns1):  # O(N), where n is the number of columns1
            element = int(input())
            row.append(element)
        matrix_x.append(row)

    # Prompt for elements of second matrix: O(N^2)
    print("Enter elements of the second matrix:")
    for i in range(rows2): # O(N), where n is the number of rows * columns
        row = []
        for j in range(columns2):  # O(N), where n is the number of columns2
            element = int(input())
            row.append(element)
        matrix_y.append(row)

    # Check for rotation: O(N^2)
    is_rotation = True
    for i in range(rows1):  # O(N), where n is the number of rows1
        for j in range(columns1): # O(N), where n is the number of columns1
            if i < columns2 and j < rows2:
                if matrix_x[i][j] != matrix_y[j][i]:
                    is_rotation = False
                    return False
            else:
                if matrix_x[i][j] != 0:
                    is_rotation = False
                    return False
    
    return is_rotation


def invertDictionary(): #O(N), where N is the number of key-value pairs
    # Prompt for dictionary creation  
  #O(N), where N is the number of key-value pairs entered by the user.
    print("Create a dictionary:")
    dictionary = {}
    while True:
        key = input("Enter your keys and type 'done' when finished: ")
        if key.lower() == "done":  # Convert input to lowercase for case-insensitive check
            break
        value = input("Insert value for key: ")
        dictionary[key] = value

    # Invert the dictionary
  #O(N), where N is the number of key-value pairs in the original dictionary
    inverted_dict = {}
    for key, value in dictionary.items():
        if value not in inverted_dict:
            inverted_dict[value] = [key]
        else:
            inverted_dict[value].append(key)

    # Display the original and inverted dictionaries O(1)
    print("Before inverting:")
    print(dictionary)
    print("After inverting:")
    print(inverted_dict)


def convertToDict(): # O(N) where N is the number of sets of user data entered by the user
    user_data = []
    while True: #O(N)
        print("Enter user data (or 'done' to finish):")
        first_name = input("First Name: ")
        if first_name.lower() == 'done':
            break
        last_name = input("Last Name: ")
        user_id = input("ID: ")
        job_title = input("Job Title: ")
        company = input("Company: ")

        user_info = [first_name, last_name, user_id, job_title, company]
        user_data.append(user_info)

    # Create an empty dictionary to store the user information
    user_dict = {} #O(1)
    
    # Convert the user_data list of lists into the desired dictionary format
    for user in user_data: # O(N)
        user_id = user[2]  # Extract the user ID from the user's data (ID is at index 2)
        user_info = user[:2] + user[3:]  # Extract the user information without the ID
        user_dict[user_id] = user_info  # Assign the user ID as the key and user_info as the value

    return user_dict

def reverse(s: str): #O(N), where N is the length of the input string s
    if len(s) == 1: 
        return s
    else:
        return s[-1] + reverse(s[:-1])
    

def checkIfPalindrome(): #O(N), where N is the length of the word entered by the user
  user_word = str(input("Enter a word to check if it is a palindrome: "))
  #invert the word the user input
  inverted_word = reverse(user_word) #O(N)
  if user_word == inverted_word: #O(N)
    print("This word is a palindrome")

  else: 
    print("This word is not a palindrome")


def mergeSort(arr): #O(N log N) where N is the size of the input array arr
    if len(arr) > 1: #O(1)
        mid = len(arr) // 2
        sub_array1 = arr[:mid]
        sub_array2 = arr[mid:]

        mergeSort(sub_array1) #O(log N)
        mergeSort(sub_array2)

        i = j = k = 0

        while i < len(sub_array1) and j < len(sub_array2): #O(N)
            if sub_array1[i] < sub_array2[j]:
                arr[k] = sub_array1[i]
                i += 1
            else:
                arr[k] = sub_array2[j]
                j += 1
            k += 1

        while i < len(sub_array1):
            arr[k] = sub_array1[i]
            i += 1
            k += 1

        while j < len(sub_array2):
            arr[k] = sub_array2[j]
            j += 1
            k += 1


def findElement(): #O(N log N), where N is the length of the list
    search_for = int(input("Enter the element you want to search for: "))
    list_1 = [1, 90, 7, 6, 14, 16, 18]
    found = False

    for i in range(len(list_1)): #O(N),where N is length of list
        if list_1[i] == search_for:
            print(f"The number {search_for} is found at index {i}")
            found = True
            break

    if not found: #O(N log N)
        print("Not found")
        mergeSort(list_1)
        print("Sorted list:", list_1)


  

def main(): #O(N log N), WORST CASE
    # Ask for user's name
    name = input("Enter your name: ")  # O(1)
    print("Welcome,", name)

    while True:  # O(n), where n could be infinity if the user doesn't choose 7 to exit (worst case)
        # Display menu
        print("\nMenu:")
        print("1. Add Matrices")
        print("2. Check Rotation")
        print("3. Invert Dictionary")
        print("4. Convert Matrix to Dictionary")
        print("5. Check Palindrome")
        print("6. Search for an Element (BONUS: Search, if element found then sort using merge sort algorithm)")
        print("7. Exit")

        choice = int(input("Enter your choice: "))  # O(1)

        if choice == 1:
            add_matrices()  
          # O(N^2) where N is the number of rows multiplied by the number of columns.
        elif choice == 2:
            rotation_result = checkRotation() 
          #O(N^2) where N is the number of rows multiplied by the number of columns.
            if rotation_result:
                print("The matrices are rotations of each other.")
            else:
                print("The matrices are not rotations of each other.")
        elif choice ==3:
          invertDictionary()
          # O(N) where N is the number of key-value pairs.
        elif choice == 4:
          result_dict = convertToDict()
          # O(N) where N is the number of sets of user data entered by the user.
          print("Converted Dictionary:")
          print(result_dict)
        elif choice == 5:
          checkIfPalindrome()
          # O(N) where N is the length of the word entered by the user.
        elif choice == 6:
          findElement()
          #O(N log N) where N is the length of the list list_1.
        elif choice == 7:
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")



main()
