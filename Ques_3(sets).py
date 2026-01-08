country={'India','USA','UK','Russia','China'}
print(country)  # 1

country2={"UK","UAE","USA","UK"}
print(country2)  # 2

fruits=set(["apple","banana","cherry","apple"])
print(fruits)  # 3

country2.add("Germany")
print(country2)  # 4

country.update(country2)
country.update(["Spain","Italy"])
print(country)  # 5

fruits.add("cherry") #6
print(fruits)   #positions changes

country.remove("Russia")
print(country)  # 7

country.discard("Spain") #8
print(country)  # no error

popped=fruits.pop()
print("Popped fruit:",popped)
print(fruits) # 9

country.clear()
print(country)  # 10

A={1,2,3,4,5}
B={4,5,6,7,8}
C={2,3,4}

print("Union:", A | B) # 11

print("Intersection:", A & B) # 12

print("First Set- Second Set:",A - B) # 13

print("Symmetric Difference:", A ^ B) # 14

print("C is subset of A?",C.issubset(A)) # 15

print("A is superset of C?",A.issuperset(C)) # 16

print("Doesn't A and B have common ?",A.isdisjoint(B)) # 17

print("Is India present in country?","India" in country) # 18

print("Is UAE not present in country?","UAE" not in country) # 19

print("Lenght of country2 set:",len(country2)) # 20

print("Max value:",max(A)) # 21

print("Min value:",min(A))  # 21

print("Sum of A set:",sum(A)) # 22

sort=sorted(B)  #Needed varible because set are immutable
print("Ascending order of B set:",sort) # 23

rev_sort=sorted(B,reverse=True)
print("Descending order of B set:",rev_sort) # 24

bool={1,1,1}
print("Any element is true:",any(bool) ) # 25

print("All element are true:",all(bool)) # 26

D=C.copy()
print(C)
print(D) # 27

del D
#print("D after deletion:",D) # Error because D is deleted # 28

list=[1,2,2,3,4,4,5]
X=set(list)
print(X) # 29

class_A={"Alice","Bob","Charlie"}
class_B={"Bob","David","Eve"}

print("Same students:", class_A & class_B) # 30

print("Class A sudents:",class_A - class_B) #30

print("All students:", class_A | class_B) #30


