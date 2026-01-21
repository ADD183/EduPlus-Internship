tup=("Data",("Science","AI",100))
print(tup[1][1])  # Accessing nested tuple element
print(tup[0:2])
print(len(tup))  # Finding length of tuple
print(tup[1].index("AI"))  # Finding index of an element
print(tup.count("Data"))  # Counting occurrences of an element

employee={("John",28,"Engineer",50000),("Alice",32,"Doctor",75000),("Bob",25,"Artist",40000)}
for emp in employee:
    print(emp)
name, age, profession, salary =employee  # Unpacking tuple
print("Name:",name)
print("Age:",age)

loctaions={"Financial Capital":("Mumbai","India"),"Tech Hub":("Bangalore","India")}
print("Location Info:",loctaions[("Tech Hub")])  # Accessing tuple from dictionary value

tup2=(3,1,4,5,2,7,9,8,6)    
print(len(tup2))
print(max(tup2))  # Finding maximum value      
print(min(tup2))  # Finding minimum value
print(tup2[-1::-1])
print(tup2)     #Remains as it is because tuples are immutable
asc=tuple(sorted(tup2))  # Sorting tuple elements in ascending order
print(asc)
desc=tuple(sorted(tup2, reverse=True))
print(desc) # Sorting tuple elements in descending order

numbers=tuple(range(1,11))
print(numbers)  # Generating tuple using range

status=(True,False,True,False,True)
print(all(status))
print(any(status))

score=(85,90,78,92,88)
name=("Alice","Bob","Charlie","David","Eve")
combined=tuple(zip(name,score)) # Combining two tuples using zip
print(combined)