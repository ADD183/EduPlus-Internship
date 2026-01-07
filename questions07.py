num=[1,2,3,4,5,6,7,8,9,10]
print(num)      #1

mix=[1,'ABC',3.5,True]
print(mix)         #2

print(num[0],num[-1])
x=len(num)/2
print(num[int(x)])   #3

print(num[0:3],num[-3::])   #4

num[1]=15
print(num)      #5

num.append(20)
print(num)      #6

num.insert(2,16)
print(num)      #7

num2=[30,40,50]
num.extend(num2)
print(num)      #8  

num.remove(16)
print(num)      #9

popped_element=num.pop(3)
print(popped_element)   #10

del num[0]
print(num)      #11

num.clear()
print(num)      #12 

num=[1,2,3,4,5,6,7,8,9,10,9,5,9]
print(5 in num)   #13

print(num.index(10))   #14

print(num.count(9))    #15

num.sort()
print(num)      #16

num.sort(reverse=True)
print(num)      #17

num.reverse()
print(num)      #18

num2=num.copy()
del num2[2:7]
print(num2)     #19

num3=[20,30,40,50]

print(num+num3)