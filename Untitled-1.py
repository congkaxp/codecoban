a=1
while a<100//5:
 b=1
 while b<100//3:
  c=100-(a+b)
  if 15*a+9*b+c==300:
   print(a,'  ',b,"  ",c)
  b=b+1
 a=a+1