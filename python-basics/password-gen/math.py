num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sum = num1 + num2
print("The sum of", num1, "and", num2, "is", sum)
difference = num1 - num2
print("The difference between", num1, "and", num2, "is", difference)
product = num1 * num2
print("The product of", num1, "and", num2, "is", product)
if num2 != 0:
    quotient = num1 / num2
    print("The quotient of", num1, "divided by", num2, "is", quotient)
else:
    print("Cannot divide by zero.")