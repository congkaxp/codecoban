a = int(input('nhập a '))
b = int(input('nhập b '))
c=a*b
d=[]
for i in range(1,c+1):
    if(i%a==0)&(i%b==0):
        d+=[i]
print('bcnn là ',max(d))