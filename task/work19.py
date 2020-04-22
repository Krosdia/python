
lst=[2,56,4,9,17,30,7,8,24,1]
order=[]
for j in range(10,1,-1):
    smallest=lst[0]
    for i in range(1,j):
        if smallest<=lst[i]:
            pass
        else:
            smallest=lst[i]
    lst.remove(smallest)
    order.append(smallest)
order.append(lst[0])
print(order)  
