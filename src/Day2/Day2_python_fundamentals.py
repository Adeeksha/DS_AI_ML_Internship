#datatype
age=22
print(age)
print(type(age))

#simple calculator
print("Input from user")
num1=int(input("Enter a number 1:"))
print(num1)
num2=int(input("Enter a number 2:"))
print(num2)
sum=num1+num2
subtraction=num1-num2
multiplication=num1*num2
division=num1/num2
print("Enter an operation to be performed on 2 numbers:")
result=input("Enter operation (+, -, *, /): ")
if(result=="+"):
    print("sum of 2 numbers is:",sum)
elif(result=="-"):
    print("subtraction of 2 numbers is:",subtraction)
elif(result=="*"):
    print("multiplication of 2 numbers is:",multiplication)
elif(result=="/"):
    print("divison of 2 numbers is:",division)


#String concatenation
name=input("Enter your name:")
print("Welcome "+name+"!")

#String format 
print("Name below is printed using String Format")
print(f"Welcome {name}!")






