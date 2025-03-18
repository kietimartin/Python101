num1 = int(input("Input the first digit: "))
operation = input("What operation do you want to do? ")
num2 = int(input("Input the second digit: "))

if operation == "+":
    print(num1 + num2)

elif operation == "-":
    print(num1 - num2)

elif operation == "/":
    print(num1 / num2)

elif operation == "*":
    print(num1 * num2)

else:
    print("Input valid operation.")

