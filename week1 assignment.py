#ask the user for input

num1= float(input("enter first number: "))
num2= float(input("enter second number: "))

#perfom basic operations
operation=input("enter mathematical operaion(+,-,*,/): ")
if operation=="+":
    result=num1 +num2
elif operation=="-":
    result=num1-num2
elif operation=="*":
    result=num1*num2
elif operation=="/":
    ifnum2==0
    print("error,divion by zero" )
    result=num1/num2
else:
    print("error,invalid operation")



print(f"{num1}{operation} {num2}={result}")


