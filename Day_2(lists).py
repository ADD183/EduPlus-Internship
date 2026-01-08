list1=[1,2,3,4,5]
list2=["apple","banana","cherry"]
list3=[1,"apple",3.5,True]

list1.sort()
print(list1)
# Accessing elements
print(list3[-1])
print("1St element:",list2[0])

#Slicing
#print(list1[0:3])
#print(list1[::-1])
#print(list1[::2])
#print(list1[::-2])

# Modifying elements
list2[1]="orange"
#print(list2)
list2.append("mango")
#print(list2)

list2.insert(-2,'grapes')  #Insert 'grapes' at the second last position
#print(list2)

list2.remove("apple")
#print(list2)

X=list2.pop()  # Remove and return the last element
#print(X)
del list2[0]  # Delete the first element
#print(list2)

list2.clear()  # Clear the entire list
#print(list2)

list3.extend(list1) # Extend list3 by appending elements from list1
#print(list3)

print("apple" in list3) #membership test

print("grapes" not in list3) #membership test

#list3.remove([0:3]) # Remove elements from index 0 to 2

list4=[3,1,4,5,2,3,3]
list4.sort()  # Sort the list
print(list4)
list4.sort(reverse=True)  # Sort the list in descending order
print(list4)

list4.reverse() # Reverse the list

Y=list4.count(3) # Count occurrences of 3 in the list
print(Y)


list5=list4.copy() # Create a copy of list4
print(list5)

list6=[["apple","banana"],["cherry","mango"]] # Nested list
print(list6[0][1])

squares=[x**2 for x in range(1,11)] # List comprehension to generate squares of numbers from 1 to 10

even=[x**2 for x in range(1,11) if x%2==0] # Even squares using list comprehension
odd=[x**2 for x in range (1,11) if x%2 != 0] # Odd squares using list comprehension

print("Even squares:",even)
print("Odd squares:",odd)

tuple=(1,2,3,4,5)
convert=list(tuple)
print(convert)

name="HelloWorld!"
char_list=list(name)
print(char_list)

