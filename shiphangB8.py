while True:   
    n = float(input('Nhập số km: '))
    if n>0:
        print('Bạn có thu tiền hộ không ?')
        print('1. Không\n2. Có')
        luachon = int(input('Nhập lựa chọn của bạn '))
        if luachon==1:        
            if n<=3:
                print('số tiền ship là: 10000')
            else:
                print('số tiền ship là: ',(n-3)*3000+10000)
            break        
        elif luachon==2:       
            if n<=3:
                print('số tiền ship là: 15000')
            else:
                print('số tiền ship là: ',(n-3)*4000+15000)
            break

    
    

     
