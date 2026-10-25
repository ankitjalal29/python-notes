#write a program to store seven fruits enterd by the user .
list=[]
name1=input("enter the name of fruits 1 : ", )
list.append(name1)

name2=input("enter the name of fruits 2 : ", )
list.append(name2)

name3=input("enter the name of fruits 3 : ", )
list.append(name3)

name4=input("enter the name of fruits 4 : ", )
list.append(name4)

name5=input("enter the name of fruits 5 : ", )
list.append(name5)

name6=input("enter the name of fruits 6 : ", )
list.append(name6)

name7=input("enter the name of fruits 7 : ", )
list.append(name7)
print(list)

#2--write a program to accept marks of 6 students and display them in a sorted manner.

marks=[]
student1=int(input("enter marks of student : ",))
marks.append(student1)
student2=int(input("enter marks of student : ",))
marks.append(student2)
student3=int(input("enter marks of student : ",))
marks.append(student3)
student4=int(input("enter marks of student : ",))
marks.append(student4)
student5=int(input("enter marks of student : ",))
marks.append(student5)
student6=int(input("enter marks of student : ",))
marks.append(student6)
marks.sort()
print(marks)      #output-- [4, 7, 34, 45, 46, 56]

 

#3-- write a program to sum a list with four numbers 
list5=(23,34,45,55)
a,b,c,d=list5
print(a+b+c+d) #output 157

#by built in function
print(sum(list5))    #output =157

#4-- write a program to count the number of zero in a tuple 
tuple2=(23,34,0,0,0,0,6,67,0)
print(tuple2.count(0))   #output=5