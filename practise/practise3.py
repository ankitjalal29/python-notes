                                          #practise set ---3
#-1-- write a pyhton program to display a user entered name followed  by good afternoon using input () function

name=input("enter your name : ")
print(f"good afternoon, {name}")       #good afternoon, ankit jalal 

#2-- write a python program to fill in latter template given below with name and date.
letter ='''Dear <|name|>,
         You are selected !
                           <|date|>'''
print(letter.replace("<|name|>", "ankit Jalal").replace("<|date|>", "24 oct 2027 "))  #Dear ankit Jalal,
                                                                                                 #You are selected !
                                                                                                                    #24 oct 2027


#3-- write a  program to detect double space in a string .
detect="hello  my  name is  ankit jalal  "
print(detect.find("  "))      # index=5  tells the index of the element 


#4--replce the double space from problem 3 with single space .
print(detect.replace("  "," "))  #hello my name is ankit jalal
print(detect) #hello  my  name is  ankit jalal   this because string are 
                                                  #immutable which means that you can not change them by running functions on them 

#5 wite a progrma to formate the following letter using escape sequence characters.

sentence="dear ankit, this python course is nice. thanks!"
print(sentence) #dear ankit, this python course is nice. thanks!
num1="dear ankit,\n\tThis python course is nice.\n thanks!"
print(num1)  #dear ankit,
               #       This python course is nice.
              #thanks!

