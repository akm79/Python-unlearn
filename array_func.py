from array import *
q=array('i',[])
a = input("enter size")
for i in range(int(a))          :
    b=input("enter data")
    q.append(int(b))
print(q)
q.insert(2,4)
for i in range(len(q)):
    print (q[i])
print (len(q))
print(max(q))
print(min(q))
print(sorted(q))
print(sum(q))

