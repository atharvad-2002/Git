# Day2

st="My name is Atharva dalvi.\nI am 18 years old"
print(st)

St=input("Enter Your first name: ")
So=input("Enter your last name: ")
print(St+ " " +So)
print(len(St))
print(St[0])
print(St + St[-5:])
print(St.capitalize())

Su="Atharva Dalvi"
print(Su.replace("Dalvi","intelligent"))
print(Su.find("th"))
print(Su.count("a"))


a=int(input("Enter your marks:"))

if(a>=90):
    print("You have secured A grade")
elif(90>a>=80):
    print(" You have secured B grade")

elif(80>a>=70):
    print("You have secured C grade")
elif(70>a>=60):
    print("you have secured D grade")

else:
    print("You have failed")

# practice question1:
a=int(input("Enter the numebr:"))
if(a%2==0):
    print("The entered number is a even number")
else:
    print("The number is odd")

# practice question 2
a=float(input("Enter the first number:"))
b=float(input("Enter the second number:"))
c=float(input("Enter the third number:"))

if(a>b and a>c):
    print(a,"is the greatest number")
elif(b>a and b>c):
    print(b,"the greatest number")
else:
    print(c,"the greatest number")

# practice question 3
a=int(input("Enter the number: "))
if(a%7==0):
    print("The number is a multiple of 7")
else:
    print("The number is not a multiple of 7")