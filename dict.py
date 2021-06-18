"""a = {'ab':'car',1:'bat'}
a[2]='rat'
a[3]='cat'
a['89']='dog'
a[7]='seven'
print(a) 
a.popitem()
print(a.items())
print(a.keys())
print(a.values())
b = a.copy()
print(b)

for key in a:
    print(key,a[key])"""
"""a={}.fromkeys([1,2,3],0)
print(a.get(5,3))
print(a)"""

rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
id1 = id(rec)
del rec
rec = {"Name" : "Python", "Age":"20", "Addr" : "NJ", "Country" : "USA"}
id2 = id(rec)
print(id1)

my_dict = {}
my_dict[(1,2,4)] = 8
my_dict[(4,2,1)] = 10
my_dict[(1,2)] = 12
 
sum = 0
for k in my_dict:
    sum += my_dict[k]
 
print(sum)
print(my_dict)

rec = {"Name" : "Python", "Age":"20"}
r = rec.copy()
print(id(r)) 
print(id(rec))

def addone(index):
    if index in fruit:
        fruit[index] += 1
    else:
        fruit[index] = 1
        
fruit = {}
addone('Apple')
addone('Banana')
addone('apple')
print(fruit)
print (len(fruit))

my_dict = {}
my_dict[1] = 1
my_dict['1'] = 2
my_dict[1.0] = 4
 
sum = 0
for k in my_dict:
    sum += my_dict[k]
    
print (sum)