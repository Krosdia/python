import random
list =[1,2,3,4,5]
tup = (1, 2, 3, 4, 5 )
random.choice(range(1,20))
x = random.choice(range(1,20))
y = random.choice(range(1,20))
list.append(x)
newTuple = (tup,y)
print(list)
print(newTuple)
