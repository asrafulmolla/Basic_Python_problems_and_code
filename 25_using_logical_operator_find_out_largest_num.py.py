num1=int(input("Enter the first num: "))
num2=int(input("Enter the 2nd num: "))
num3=int(input("Enter the 3rd num: "))
if(num1>num2 and num1>num3):
    print(num1," is big")
elif(num2>num1 and num2>num3):
    print(num2," is big")
else:
    print(num3, " is big")