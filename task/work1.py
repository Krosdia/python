r = range(0,51);
print("偶数为：");
for i in r:
  if(i % 2 == 0):
      print(i,end=',');
print("奇数为："); 
for j in r:
    if(j % 2 ==1):
        print(j,end=',');     
print("质数为：");
b = False;
for a in range(2,51):
    for c in range(2,a):
        if(a % c == 0):
            b = False; 
            
        else:
            b = True
    if(b == True) :
        print(a,end=',');     
print("能同时被2和3整除的数为:");
for d in range(0,51):
    if(d % 2 == 0 and d % 3 == 0):
        print(d,end=',');   