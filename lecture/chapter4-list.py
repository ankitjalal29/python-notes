                #exercise 4 
                  #LIST-list are mutable

#list indexing-
list=[12,23,12]
print(list[0])      #output - 12

#list slicing- 
list1=[32,3,23,3]
print(list[0:3])    #output - [12, 23, 12]

#method--
#1-append-
friends=["apple","ankit",4,5.66,False,"aakash"]
print(friends)      #output - ['apple', 'ankit', 4, 5.66, False, 'aakash']
friends.append("jalal")
print(friends)      #output-  ['apple', 'ankit', 4, 5.66, False, 'aakash', 'jalal']

#2-sort-
l1=[32,43,23,23,34,54,1,232,3,445,23]
l1.sort()
print(l1)           #output- [1, 3, 23, 23, 23, 32, 34, 43, 54, 232, 445]

#3-  reverse-
l1.reverse()
print(l1)           #output - [445, 232, 54, 43, 34, 32, 23, 23, 23, 3, 1]

#4-  insert-
l1.insert(3,232323)
print(l1)           #output- [445, 232, 54, 232323, 43, 34, 32, 23, 23, 23, 3, 1]

#5- pop-
l1.pop(3)
print(l1)           #output - [445, 232, 54, 43, 34, 32, 23, 23, 23, 3, 1]

#6- remove
l1.remove(445)
print(l1)           #output- [232, 54, 43, 34, 32, 23, 23, 23, 3, 1]
