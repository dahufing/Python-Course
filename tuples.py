tuple1=("Daniela",19,"Catalunya")
print(tuple1) # ('Daniela', 19, 'Catalunya')
print(type(tuple1)) #tuple

tuple2=tuple(["Daniela",19,"Catalunya"])

item= tuple2[0]
print(item) #shows Daniela

for i in tuple2:
    print(i) #print every item

if "Daniela" in tuple2:
    print("yes")
else:
    print("No")

tuple3=(1,2,3,4,5,6,8,11)
print(tuple3.index(2)) #how many times appears the numer 2
 
tuple3=list(tuple3)
print(tuple3) #now is a list 

a=(1,2,3,4,5,6,7,8,9,10)
b=a[2:5]
print(b) #gives (3,4,5) the last one doesn't appear


tuple4= "Daniela", 19, "Bcn"
name,age,city = tuple4

tuple5= (0,1,2,3,4)
i1, *i2, i3 = tuple5
print(i1) #0 first one
print(i3) #4 the last
print(i2) # a list [1, 2, 3]

import sys
l1=[0,1,2,"hola",True]
l2=(0,1,2,"hola",True)
print(sys.getsizeof(l1),"bytes") #104 bytes === List
print(sys.getsizeof(l2), "bytes") #88 bytes === Tuple

import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5]",number=100000)) #how many time take to create the LIST
print(timeit.timeit(stmt="(0,1,2,3,4,5)",number=100000)) #how many time take to create the TUPLE
