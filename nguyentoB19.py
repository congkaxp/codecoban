n = int(input('nhập n: '))
if n==2:
    print('day la so nguyen to')
else:
    k=0
    for i in range(2,n):
        if (n%i==0):
            k=k+1
    if k==0:
        print('day la so nguyen to')
    else:
        print('day ko la so nguyen to')
