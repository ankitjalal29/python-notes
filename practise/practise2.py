#write a python program to add two numbers.
a=int(input("enter a number :"))      #enter a number :43
b=int(input("enter a number :"))      #enter a number :23  
c=a+b
print(c)

#output
#66

#write a python program to find remainder when a number is divided by z

d=int(input("enter a number: "))  #enter a number: 44
z=int(input("enter a number for reamainder:")) #enter a number for reamainder:4
print("the reamiander is :", d%z) #the reamiander is : 0

#3 check the type of varriable assigned input fuction

v=(input("enter a number :  "))  #enter a number : 33
print(type(v))   #<class 'str'> (input always string value)

#4 use comparsion operator to  find out whether a given varriable a is greater than 'b' or not .
#take a =34 and b=80

number1=34
number2=80
print(a>b)  #False

#5  write a python program to find an average of two numbers entered by the user 

number4=int(input("enter a number : "))      #enter a number : 43
number5=int(input("enter a number : "))      #enter a number : 43
print("the average of two number is :", (number4+number5)/2)    #the average of two number is : 43.0

#6  write a python program to calculate the sqaure of the number given by user 

number6=int(input("enter a number  :"))   #enter a number  :34
print("the square of the number is :", number6**2)    #the square of the number is : 1156