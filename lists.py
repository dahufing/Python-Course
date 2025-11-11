mylist=["ordenador","tele","mesa"]
print(mylist)

mylist2= list()
print(mylist2)

list3=[5,True,"apple"]
print(list3)
it1=mylist[1]
print(it1)
it2=mylist[-2]

for i in mylist:
    print(i)

if "tele" in mylist:
    print ("yes")
else:
    print("no")

longitud=len(mylist)
print(longitud)

mylist.append("mando")
print(mylist)

mylist.insert(1,"reloj")
print(mylist)

p=mylist.pop() #remove the last one
print(p)
print(mylist)

t=mylist.remove("tele")#remove specific
print(mylist)

c=mylist.clear() #remove all
print(mylist)

r=mylist.reverse()#reversed order

list1=[4,2,3,4,-1-3,10]
s=list1.sort()#ascending
print(list1)


new_list= sorted(list1)#if i don't want to cahnge my list

list0=[0]*5
print(list0)

list2=[1,2,3,4,5]
new_list2= list0 +list2 #everything together
print(new_list2)

list4=[1,2,3,4,5,6,7,8,9]
a=list4[1:5] #start index 1, final index 5
b=list4[::2]#with 2 steps
c=list4[::-1]#trick to reverse the list (1 step)

llist=["banana","cherry","apple"]
llist_copy=llist #because with this both depends over the other
llist_copy.append("lemon")#original and copy now has lemon
llist_copy2=llist.copy()#now the original is not modificated


l=[1,2,3,4,5,6]
b=[i*i for i in l] 