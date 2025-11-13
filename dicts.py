d={"name":"Daniela","age":19,"city":"Barcelona"}
print(d) #{'name': 'Daniela', 'age': 19, 'city': 'Barcelona'}

d1=dict(name="Max",age=20,city="Bcn")
print(d1)

value=d1["name"]
print(value) # Max

d1["email"]="max@gmail"
print(d1) #now there's email

del d1["name"]
print(d1) #there's no name

d1.pop("age")
print(d1) #there's no age


if "name" in d:
    print(d["name"]) #Daniela

for key in d:
    print(key)

for key in d.keys():
    print(key) #name, age, city

for value in d.values():
    print(value) #Daniela, 19,Barcelona

for key,value in d.items():
    print(key,value)#name Daniela, age 19, city Barcelona

d2=d
print(d2)#the same

d2["email"]="dan@gmail"
print(d2)
print(d) #both have email


#but if i change
d2=d.copy()
d2["email"]="dan@gmail"
print(d2)
print(d) # original doesn't have email

d3={3:9,6:36,9:81}
print(d3)
value=d3[3]
print(value) #9

tup=(8,6) #list cannot do this
d3={tup:14}
print(d3) #{(8, 6): 14} 
