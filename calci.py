# Additional question for Lecture Assignment-II

num1 = float(input("Enter first number for calculation:")) 
op = input("Enter the operator: ")
num2 = float(input("Enter second number for calculation:"))
print ("The entered expression is :",num1,op,num2)
check = input("Is the expression entered correct? (y/n): ")

if check == 'y':
    if op == '+':
        print(num1,"+",num2,"=",num1+num2)
    elif op == '-':
        print(num1,"-",num2,"=",num1-num2)
    elif op == '*':
        print(num1,"*",num2,"=",num1*num2)
    elif op == '/':
        print(num1,"/",num2,"=",num1/num2)
else:
    print("Please correct the expression values")