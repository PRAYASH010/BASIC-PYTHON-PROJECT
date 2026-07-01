print("="*100)
print("CALCULATOR PERFORMING BASIC ARITHMETIC OPERATIONS")
print("="*100)
arithmetic_operator = input("What do you want to do?(- + * /) : ")

num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))

match arithmetic_operator:
    case "+":
        print("The addition of two number is : ",num1 + num2)
    case "-":
        print("The subtraction of two number is : ", num1 - num2)
    case "*":
        print("The multiplication of two number is : ", num1 * num2)
    case "/":
        print("The division of two number is : ",num1 / num2)