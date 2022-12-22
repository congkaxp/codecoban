from sre_constants import CH_UNICODE


chuoi = input('nhập: ')
nguyenam=[]
phuam=[]
chuso=[]
kytudb=[]
vitri=[]
liststr=list(chuoi)
for i in range(0,len(liststr)):
    if chuoi[i] in('u','o','a','i','ă','â','ơ','y','ô','ơ'):
        nguyenam+=chuoi[i]
    elif chuoi[i] in('0','1','2','3','4','5','6','7','8','9'):
        chuso+=chuoi[i]
    elif chuoi[i] in('q','w','r'):
        phuam+=chuoi[i]
    elif chuoi[i]==' ':
        vitri+=[i]
    else:
        kytudb+=chuoi[i]
print('các nguyên âm là: ',nguyenam)
print('các phụ âm là ',phuam)


