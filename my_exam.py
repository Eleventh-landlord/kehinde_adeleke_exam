#Question 1

#Basic calculator

#Function to add numbers
def add(a, b):
    return a + b

#Function to subtract
def subtract(a, b):
    return a - b

#Function to multiply
def multiply(a, b):
    return a * b

#Function to divid
def division(a, b):
    if b != 0:
     return a / b
    else:
        return "Error: Cannot divid by zero"
#start a loop  
while True:
#display operation option to user
 print("Select Operator: ")
 print("1. Add")
 print("2. Subtract")
 print("3. Multiply")
 print("4. Division")
 print("0. Exit")

 choice = input("select an Operator: ")
 if choice == "0":
    print("Exiting calculator")
    break
 try:
      if choice == "1":
       num1 = float(input("Enter first number: "))
       num2 = float(input("Enter second number: "))
       print("Result: ", add(num1, num2))
      elif choice == "2":
       num1 = float(input("Enter first number: "))
       num2 = float(input("Enter second number: "))
       print("Result: ", subtract(num1, num2))
      elif choice == "3":
       num1 = float(input("Enter first number: "))
       num2 = float(input("Enter second number: "))
       print("Result: ", multiply(num1, num2))
      elif choice == "4":
       num1 = float(input("Enter first number: "))
       num2 = float(input("Enter second number: "))
       print("Result: ", division(num1, num2))
       break
      else:
         print("Error! invalid operation")
 except OverflowError:
  print("Enter a non zero integer")
 except Exception as e:
   print("Error") 
#ask user if he wants to perform another operation
 again = input("Do you want to select another choice (Yes/No): ").title()
 if again not in {"Yes"}:
#if No then it would exit the calculator
   print("Exisiting calculator")
   break
 



#Question 2
while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")
    if user_input == "exit":
        print("Goodbye!")
        break        # break out of loop
    
    num = int(user_input)   # convert to integer
    
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")



#Question 3
#start loop
while True:
#Tell user to input age
    age = input("Enter your age (or type exit to quit): ").lower()
    #if age is exit the it exits the program
    if age.lower() == "exit":
        print("Goodbye!")
        break
    
    try:
        age = int(age)
        if age >= 18:
            print("You can vote")   #if age is greater than 18 print one can vote
        else:
            print("You cannot vote")   #If age is less than 18 the print you cant vote
    except:
        print("Invalid input")
 


