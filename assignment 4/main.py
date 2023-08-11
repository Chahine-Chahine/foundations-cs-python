#Creating the Node to be used in classes (stack, Queue, PriorityQueue, etc..)
class Node:
    def __init__(self, info): #O(1)
        self.info = info
        self.next = None
#------------------------------------------------------------------------------
#Stack implimentation 
class Stack: 
    def __init__(self): #O(1)
        self.head = None
        self.size = 0
#Function checking if stack is empty (return boolean True or False)
    def isEmpty(self): #O(1)
        return self.head is None
#Function to push into the stack
    def push(self, value): #O(1)
        node = Node(value)
        node.next = self.head
        self.head = node
        self.size += 1
#Function to remove from a class
    def pop(self): #O(1)
        if self.isEmpty():
            print("Cannot pop from an empty stack!")
        else:
            print("We are popping:", self.head.info)
            current = self.head
            self.head = self.head.next
            current.next = None
            self.size -= 1
#Function to peek from the stack the top element
    def peek(self): #O(1)
        if self.isEmpty():
            print("Cannot peek from an empty stack!")
        else:
            print("The top node is:", self.head.info)

#------------------------------------------------------------------------------
#Function that add the userInput into the stack then start pop(ing) the elements one by one after adding them into reversed_s so that the word is reversed then return the comparison boolean if equal or not(if equal then palindrome)
def isPalindrome(s): #O(n), where n is the length of the input string
    s = s.lower().replace(" ", "")
    stack = Stack()

    for char in s:
        stack.push(char)

    reversed_s = ""
    while not stack.isEmpty():
        reversed_s += stack.head.info
        stack.pop()

    return s == reversed_s

#------------------------------------------------------------------------------
#Implimenting class Queue
class Queue:
  #constructor function
    def __init__(self): #O(1)
        self.head = None
        self.tail = None
        self.size = 0
#Function to print the node and moving to the next until queue is empty
    def displayNode(self): #O(1)
        current = self.head
        while current is not None:
            print(current.info)
            current = current.next
#Function to check if the queue is empty
    def isEmpty(self): #O(1)
        return self.head is None
#Function to add to a queue
    def enqueue(self, value): #O(1)
        if isinstance(value, list):
            for val in value:
                node = Node(val)
                if self.isEmpty():
                    self.head = node
                    self.tail = node
                    self.size += 1
                else:
                    self.tail.next = node
                    self.tail = node
                    self.size += 1
        else:
            node = Node(value)
            if self.isEmpty():
                self.head = node
                self.tail = node
                self.size += 1
            else:
                self.tail.next = node
                self.tail = node
                self.size += 1
#Function to remove from a queue
    def dequeue(self, value): #O(1)
        if self.isEmpty():
            print("Your queue is already empty")
            return
        elif not self.search(value):
            print("The value is not found")
            return

        while self.head is not None and self.head.info == value:
            print(f"Removing {self.head.info}")
            self.head = self.head.next
            self.size -= 1

        current = self.head
        while current is not None and current.next is not None:
            if current.next.info == value:
                print(f"Removing {current.next.info}")
                current.next = current.next.next
                self.size -= 1
            else:
                current = current.next
#------------------------------------------------------------------------------
#Function to search for a value and return True if found
    def search(self, value):
        current = self.head
        while current is not None:
            if current.info == value:
                return True
            current = current.next
        return False

#------------------------------------------------------------------------------
#Class Student implimenting
class Student:
  #constructor function
    def __init__(self, name, midterm_grade, final_grade, attitude):
        self.name = name
        self.midterm_grade = midterm_grade
        self.final_grade = final_grade
        self.attitude = attitude
#Another constructor function
    def __lt__(self, other):
        if self.attitude == other.attitude:
            if self.final_grade == other.final_grade:
                return self.midterm_grade > other.midterm_grade
            return self.final_grade > other.final_grade
        return self.attitude
#------------------------------------------------------------------------------
#Class PriorityQueue Imprlimentation 
class PriorityQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
#Display nodes if found and print them in a specific criteria
    def displayNodes(self):
        current = self.head
        while current is not None:
            student = current.info
            print(f"Name: {student.name}, Midterm Grade: {student.midterm_grade}, Final Grade: {student.final_grade}, Attitude: {'Good' if student.attitude else 'Not Good'}")
            current = current.next
  #check if PriorityQueue is empty
    def isEmpty(self):
        return self.head == None
#Add to the PriorityQueue
    def enqueue(self, value):
        node = Node(value)
        if (self.isEmpty()):
            self.head = node
            self.tail = node
            self.size += 1
        else:
            if (node.info < self.head.info):
                node.next = self.head
                self.head = node
                self.size += 1
            else:
                current = self.head
                previous = current
                while (current != None and current.info < node.info):
                    previous = current
                    current = current.next

                if current == None:
                    self.tail = node

                previous.next = node
                node.next = current
                self.size += 1
#remove from the PriorityQueue
    def dequeue(self):
        if (self.isEmpty()):
            print("Your Queue is already empty!")
        elif self.size == 1:
            print("We are removing:", self.head.info.name)
            self.head = None
            self.tail = None
            self.size -= 1
        else:
            print("We are removing:", self.head.info.name)
            current = self.head
            self.head = self.head.next
            current.next = None
            self.size -= 1
#------------------------------------------------------------------------------
#Immplimentation of Stack2 this time built with a list
class Stack2: 
    def __init__(self): # O(n), where n is the number of elements in the stack
        self.items = []
#Add to a list
    def push(self, item): #O(1)
        self.items.append(item)
#remove from the list
    def pop(self): #O(1)
        if not self.isEmpty():
            return self.items.pop()
#check if the list is empty
    def isEmpty(self): #O(1)
        return len(self.items) == 0
#If the list is not empty return the last element so that we can peek
    def peek(self): #O(1)
        if not self.isEmpty():
            return self.items[-1]

#------------------------------------------------------------------------------
#Function that put the main rules for the arithmetic operations 
def applyOperator(operators, operands): 
  # O(n), where n is the length of the expression
    operator = operators.pop()
    operand2 = operands.pop()
    operand1 = operands.pop()

    if operator == "+":
        result = operand1 + operand2
    elif operator == "-":
        result = operand1 - operand2
    elif operator == "*":
        result = operand1 * operand2
    elif operator == "/":
        result = operand1 / operand2
    else:
        raise ValueError("Invalid operator")

    operands.push(result)

#------------------------------------------------------------------------------
def evaluateExpression(expression):
  # O(n), where n is the length of the expression
    operands_stack = Stack2()
    operators_stack = Stack2()

    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}

    i = 0
    while i < len(expression):
        if expression[i].isdigit():
            num = ""
            while i < len(expression) and expression[i].isdigit():
                num += expression[i]
                i += 1
            operands_stack.push(int(num))
        elif expression[i] in "+-*/":
            while (not operators_stack.isEmpty() and
                   operators_stack.peek() in "+-*/" and
                   precedence[operators_stack.peek()] >= precedence[expression[i]]):
                applyOperator(operators_stack, operands_stack)
            operators_stack.push(expression[i])
            i += 1
        elif expression[i] == "(":
            operators_stack.push(expression[i])
            i += 1
        elif expression[i] == ")":
            while operators_stack.peek() != "(":
                applyOperator(operators_stack, operands_stack)
            operators_stack.pop()
            i += 1
        else:
            i += 1

    while not operators_stack.isEmpty():
        applyOperator(operators_stack, operands_stack)

    return operands_stack.pop()
#------------------------------------------------------------------------------
#Menue to Display the student menue when user choose 3
def studentMenu():
  #  O(n), where n is the number of students in the priority queue
    pq = PriorityQueue()
    while True:
        print("a. Add a student")
        print("b. Interview a student")
        print("c. Return to main menu")

        choice = str(input("Choose from the list: ")).lower()

        if choice == "a":
            name = input("Enter student's name: ")
            midterm_grade = int(input("Enter midterm grade (0-100): "))
            final_grade = int(input("Enter final grade (0-100): "))
            attitude = input("Does the student have a good attitude? (yes/no): ").lower() == "yes"
            student = Student(name, midterm_grade, final_grade, attitude)
            pq.enqueue(student)
            print(f"{name} has been added to the priority queue.")

        elif choice == "b":
            if pq.isEmpty():
                print("No students in the queue.")
            else:
                student = pq.head.info
                print(f"Interviewing student: {student.name}")
                pq.dequeue()

        elif choice == "c":
            print("Back to the mainMenu")
            return False
        elif choice == "d":
          if pq.isEmpty():
                print("The queue is empty")
          else:
            print("The values inside the Priority list are: ")
            pq.displayNodes()
#------------------------------------------------------------------------------
#singly linked list menue show up when user choose 1
def singlyllMenu(): #O(n), where n is the number of elements in the queue
    queue = Queue()
    while True:
        print("a. Add Node")
        print("b. Display Nodes")
        print("c. Search for & Delete Node")
        print("d. Return to main menu")

        choice = str(input("Choose from the list: ")).lower()

        if choice == "a":
            numbers_str = input("Enter numbers to add to the LL (separated by commas): ")
            numbers = [int(num) for num in numbers_str.split(",")]
            queue.enqueue(numbers)
            print(f"{numbers} are successfully added to the list")

        elif choice == "b":
            if queue.isEmpty():
                print("The queue is empty")
            else:
                print("The values inside the linked list are: ")
                queue.displayNode()

        elif choice == "c":
            value = int(input("Enter a number to search for and delete: "))
            queue.dequeue(value)

        elif choice == "d":
            print("Back to the mainMenu")
            return False
#------------------------------------------------------------------------------
#The first menue that show up to the user
def mainMenu(): # Depends on the selected sub-menu worst case O(n)
    while True:
        print("1. Singly Linked List")
        print("2. Check if Palindrome")
        print("3. Priority Queue")
        print("4. Evaluate an Infix Expression")
        print("5. Exit")

        choice = int(input("Choose from the list: "))

        if choice == 1:
            singlyllMenu()

        elif choice == 2:
            string = input("Enter a string to check for palindrome: ")
            if isPalindrome(string):
                print("The string is a palindrome.")
            else:
                print("The string is not a palindrome.")

        elif choice == 3:
            studentMenu()

        elif choice == 4:
            infix_expression = input("Enter an infix expression: ")
            result = evaluateExpression(infix_expression)
            print("Result:", result)

        elif choice == 5:
            print("Exiting the program...")
            return False

#------------------------------------------------------------------------------
#Main function
def main(): #O(1)
  userName = input("Enter your name: ")
  print(f"Hello, {userName}")
  mainMenu()
  
main()


