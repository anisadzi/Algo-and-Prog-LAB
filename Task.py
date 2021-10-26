operator=eval(input("Enter your operator (1. Addition 2. Subtraction 3. Multiplication 4. Division)"))
num_1=eval(input("Enter your first number"))
num_2=eval(input("Enter the second number"))

if(operator==1):
    result=num_1+num_2
    print(f'Result is: {result}')
elif(operator==2):
    result = num_1 - num_2
    print(f'Result is: {result}')
elif(operator==3):
    result = num_1 * num_2
    print(f'Result is: {result}')
elif(operator==4):
    result= num_1 / num_2
    print(f'Result is: {result}')