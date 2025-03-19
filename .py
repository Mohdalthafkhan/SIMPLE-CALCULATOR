def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y != 0:
        return x/y
    else:
      return "Error! division by zero"
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    while True:
        choice = input("Enter choice (1/2/3/4): ")
        if choice in ('1', '2', '3', '4'):
          num1 = float(input("Enter first number: "))
          num2 = float(input("Enter second number: "))
          if choice == '1':
              print(f"The result is: {add(num1, num2)}")
          elif choice == '2':
              print(f"The result is: {subtract(num1, num2)}")
          elif choice == '3':
              print(f"The result is: {multiply(num1, num2)}")
          elif choice == '4':
              print(f"The result is: {divide(num1, num2)}")

          next_calculation = input("Do you want to perform another calculation? (yes/no): ")
          if next_calculation.lower() != "yes":
              break
          else:
              print("Invalid Input")

                  
calculator()
 
OUTPUT:-
Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
Enter choice (1/2/3/4): 1
Enter first number: 4
Enter second number: 4
The result is: 8.0
Do you want to perform another calculation? (yes/no): yes
Invalid Input
Enter choice (1/2/3/4): 2
Enter first number: 4
Enter second number: 4
The result is: 0.0
Do you want to perform another calculation? (yes/no): yes
Invalid Input
Enter choice (1/2/3/4): 3
Enter first number: 4
Enter second number: 4
The result is: 16.0
Do you want to perform another calculation? (yes/no): yes
Invalid Input
Enter choice (1/2/3/4): 4
Enter first number: 4
Enter second number: 4
The result is: 1.0
Do you want to perform another calculation? (yes/no): no

=== Code Execution Successful ===