#Queston 1:

#Part A)
#https://github.com/Chahine-Chahine

#Part B)

a = 10*(90+2)-5
print("The answer of expression a is ", a)

b = 10*90+2-5
print("The answer of expression b is ", b)

c = 10*90+(2-5)
print("The answer of expression c is ", c)

d = 10.0*(90+2)-5
print("The answer of expression d is ", d)

e = 120/(20+40)-(6-2)/4
print("The answer of expression e is ", e)

f = 5.0/2
print("The answer of expression f is ", f)

g = 5/2
print("The answer of expression g is ", g)

h = 5.0/2.0
print("The answer of expression h is", h)

i = 5/2.0
print("The answer of expression i is ", i)

j = 678%3*(8-(9/4))
print("The answer of expression j is ", j)

print("________________________________________")
#Question 2

id = "0"+ input("Choose an id number for you please: ")
name = input("Enter your name here: ")
name= name.upper().strip()
birth_date = input("Enter your birth full date: ")
birth_date = birth_date.replace("-" , "/").strip()
address = input("Enter your address: ")
address = address.lower().strip()

output = f"Your user ID is: {id}, Name: {name}, Date of birth: {birth_date}, Address: {address}"

print(output)

print("________________________________________")
#Question 3

number = eval(input("Enter a number: "))
count = len(str(number))

if number == int :
  print(f"{number} has {count} digits.")

elif number == float :
  print(f"{number} has {count -1} degits")

#I used the f"..." using the python docs :https://docs.python.org/3/tutorial/inputoutput.html

print("________________________________________")
#Question 4

number_grade = int(input("Enter your numerical grade: "))

#I added the first if statement case to privent the user adding a grade higher than 100
if number_grade >= 101:
    letter_grade = "Invalid Grade. Please assign a grade less than 101"
elif number_grade >= 90:
    if number_grade >= 97:
        letter_grade = "A+"
    elif number_grade >= 93:
        letter_grade = "A"
    else:
        letter_grade = "A-"
elif number_grade >= 80:
    if number_grade >= 87:
        letter_grade = "B+"
    elif number_grade >= 83:
        letter_grade = "B"
    else:
        letter_grade = "B-"
elif number_grade >= 70:
    if number_grade >= 77:
        letter_grade = "C+"
    elif number_grade >= 73:
        letter_grade = "C"
    else:
        letter_grade = "C-"
elif number_grade >= 60:
    if number_grade >= 67:
        letter_grade = "D+"
    elif number_grade >= 63:
        letter_grade = "D"
    else:
        letter_grade = "D-"
else:
    letter_grade = "F"

#I did not use F+ or F- ,etc.. since it is a failing grade so it won't matter

print(f"{number_grade} is equivalent to a {letter_grade}")

print("________________________________________")
#Question 5

n = int(input("Enter a number: "))

#The increasing pattern starts increasing from 1 to reach n
for i in range(1 , n+1):
  print("*" * i)
#The decreasing pattern starts at n-1 and continue decreasing to reach 0
for i in range(n-1, 0 , -1):
  print("*" * i)
  
print("________________________________________")
#Question 6

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

#This is a while loop that will validate if the second_number is less than the first_number and ask for a new input for the second_number
while second_number < first_number:
    print("Second number should be greater than or equal to the first number.")
    second_number = int(input("Enter the second number: "))

print("Even numbers between", first_number, "and", second_number, "are:")
#This for loop is to validate if the number is even between range of first and second number+1 since the second parameter is exclusive then if true print the number 

for number in range(first_number, second_number):
    if number % 2 == 0:
        print(number, end="-- ")

print(second_number)
  
print()
print("hello world")


#The comments in the code are for my own reference latter in addition to if the instructor wanted to know how i think about the problem I am solving