set1={3,2,5,1,3,4}
print(set1)  # Output: {1, 2, 3, 4, 5} - duplicates removed and unordered
set1.add(6) #used to add only one element to the set
print(set1)  # Output: {1, 2, 3, 4, 5, 6}

set2={1,"apple",3.5,True}

#set1.update(set2) #used to add multiple elements to the set
#print(set1)  # Output: {1, 2, 3, 4, 5, 6, 'apple', 3.5}

#set1.remove(3.5) #used to remove an element from the set, raises KeyError if element not found
print(set1)  # Output: {1, 2, 3, 4, 5, 6, 'apple'}

set1.discard(10) #used to remove an element from the set, does not raise error if element not found
print(set1)  # Output: {1, 2, 3, 4, 5, 6, 'apple'}

print(set1.pop()) #removes values randomly and returns an arbitrary element from the set 
print(set1)  # Output: set with one less element

A=set1.copy() #creates a shallow copy of the set
B={1,9,8,4,5,6}

print("Unioun:", A | B) # Union of sets
print("Intersection:",A & B) # Intersection of sets
print("Difference:", A - B) # Difference of sets
print("Symmetric Difference:",A ^ B) # Symmetric Difference of sets

print("Is apple is in set1?","apple" in set1) #membership test
print("Is 10 not in set1?","10" not in set1) #membership test

for i in set1:
    print("Items in set1:",i)  # Iterating through set elements


frozen=frozenset(["apple","banana","cherry"]) # Creating a frozenset (immutable set) only union/intersection operations can be perfrmed
print(frozen)  

Visit1={"Alice","Bob","Charlie","Eve"}
Visit2={"Bob","David","Eve","Frank"}

# Finding Unique Visitors
print("Unique Visitors are:",Visit1 | Visit2)

# Finding Common Visitors
print("Common Visitors are:",Visit1 & Visit2)

# Finding Visitors in Visit1 but not in Visit2
print("Visitors which didn't visit Visit2 are:", Visit1 - Visit2)

print("Max value in set1:",max(set1)) # Finding maximum value in set
print("Min value in set1:",min(set1)) # Finding minimum value in set
print("Sum of set1;",sum(set1)) # Finding sum of set elements
print("Length of set1:",len(set1)) # Finding length of set
print("Ascending order of set1:",sorted(set1)) # Sorting set elements in ascending order
print("Descending order of set1:",sorted(set1,reverse=True)) # Sorting set elements in descending order

binary_set={1,0,1}
print(any(binary_set)) # Returns True if any element is true
print(all(binary_set)) # Returns True if all elements are true

set3={1,2,3}
set4={2,3}
print("set4 is subset of set3?", set4.issubset(set3)) # Check if set4 is subset of set3
print("set3 is superset of set4?", set3.issuperset(set4)) # Check if set3 is superset of set4
print("set4 is superset of set3?",set4.issuperset(set3)) # Check if set4 is superset of set3
print("set4 is disjoint with set3?",set4.isdisjoint(set3)) # Check if set4 is disjoint with set3
set5=set3.copy()
print(set5)
