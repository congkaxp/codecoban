import math
print('phuong trinh co dang ax^2+bx+c=0')
a=float(input('nhap a= '))
b=float(input('nhap b= '))
c=float(input('nhap c= '))
if (a == 0):
        if (b == 0):
            print ("Phương trình vô nghiệm!");
        else:
            x=-c/b
            print ("Phương trình có một nghiệm: x = ", x)
else:
    delta = b*b-4*a*c;
    if (delta > 0):
        x1 = (-b + math.sqrt(delta)) / (2 * a);
        x2 = (-b - math.sqrt(delta)) / (2 * a);
        print ("Phương trình có 2 nghiệm là: x1 = ", x1, " và x2 = ", x2);
    elif (delta == 0):
        x1 = -b/(2*a);
        print("Phương trình có nghiệm kép: x1 = x2 =", x1);
    else:
        print("Phương trình vô nghiệm!");
