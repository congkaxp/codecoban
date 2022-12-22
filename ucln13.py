a = int(input('nhập a '))
b = int(input('nhập b '))
x=[]
y=[]
for i in range(1,a+1):
    if (a%i==0):
        x+=[i]
for i in range(1,b+1):
    if (b%i==0):
        y+=[i]
print('ucln là ',max(set(x)&set(y))) 
   