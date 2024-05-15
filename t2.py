# calculator
n1 = float(input("Enter the number1 : "))
n2 = float(input("Enter the number2 : "))
ch = input("Enter operation (+,-,*,/,%) : ")

if(ch == '+'):
    print("Addition of n1 and n2 = "+str(n1+n2))
elif(ch == '-'):
    print("Subtraction of n1 and n2 = "+str(n1-n2))
elif(ch == '*'):
    print("Multiplication of n1 and n2 = "+str(n1*n2))
elif(ch == '/'):
    print("Division of n1 and n2 = "+str(n1/n2))
elif(ch == '%'):
    print("Mod of n1 and n2 = "+str(n1%n2))
else:
    print("Invalid operator")
