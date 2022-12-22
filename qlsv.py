#Yêu cầu bài kiểm tra giữa kỳ: 
# thiết kế chương trình và lập trình python chương trình quản lý danh sách lớp học.
# 1. Thông tinh sinh viên trong lớp bao gồm: tên họ, mã sinh viên, ngày tháng năm sinh, thuộc tổ, giới tính, điểm giữa kỳ, điểm cuối kỳ, điểm chuyên cần; 
# 2. Tìm kiếm sinh viên theo các thông tin từ users; 
# 3. Chọn và chỉnh sửa thông tin sinh viên; 
# 4. Tính toán điểm cuối kỳ của sinh viên (trung bình cộng 3 điểm thành phần); 
# 5. Thêm sinh viên; 
# 6. Xoá sinh viên

LSV = []
check=[0]

def nhap():
    for i in range(0,n):
        print('nhap sinh vien thu ',i+1)
        id = int(input('\tNhap mssv '))        
        k=1
        t=len(check)
        while k==1:
            m=0
            for index in check:
                if id!=index:
                    m=m+1
            if m==t:
                k=2
            else: id = int(input('\tNhap lai mssv '))
        check.append(id)           
        ten = input('\tNhap ho va ten ')
        gt = input('\tNhap gioi tinh ')
        sn = input('\tNhap ngay thang nam sinh ')
        to = int(input('\tNhap to '))
        dgk = float(input('\tNhap diem giua ki '))
        dck = float(input('\tNhap diem cuoi ki '))
        dcc = float(input('\tNhap diem chuyen can '))
        
        in4 = { "ma sv":id , "ten":ten , "gioi tinh":gt , "sinh nhat":sn , "to":to , "diem giua ki":dgk , "diem cuoi ki":dck , "diem chuyen can":dcc} 
        LSV.append(in4) 

def xuat():
    print('STT \t mssv \t Tên \t Giới tính \t Tổ \t Ngày tháng năm sinh\t Điểm giữa kì \t Điểm cuối kì \t Điểm chuyên cần ')
    for i in range(0,len(LSV)):
        print((i+1) , "\t" , LSV[i]["ma sv"] , "\t" , LSV[i]["ten"] , "\t" , LSV[i]["gioi tinh"] , "\t\t" , LSV[i]["to"] , "\t\t" , LSV[i]["sinh nhat"] ,"\t\t" , LSV[i]["diem giua ki"] ,"\t\t", LSV[i]["diem cuoi ki"] , "\t\t", LSV[i]["diem chuyen can"] )

        
def timsv():
    idcantim = int(input('Nhap mssv can tim '))
    j=0
    for i in range(0,len(LSV)):        
        if LSV[i].get("ma sv")==idcantim:
            print('sinh vien can tim la ',LSV[i])
            j=j+1
        if j==0:
            print('Khong co sinh vien nay !')            

def themsv():            
    id = int(input('\tNhap mssv '))
    ten = input('\tNhap ho va ten ')
    gt = input('\tNhap gioi tinh ')
    sn = input('\tNhap ngay thang nam sinh ')
    to = int(input('\tNhap to '))
    dgk = float(input('\tNhap diem giua ki '))
    dck = float(input('\tNhap diem cuoi ki '))
    dcc = float(input('\tNhap diem chuyen can '))        
    in4 = { "ma sv":id , "ten":ten , "gioi tinh":gt , "sinh nhat":sn , "to":to , "diem giua ki":dgk , "diem cuoi ki":dck , "diem chuyen can":dcc} 
    LSV.append(in4) 
    

def xoasv():
    msv = int(input('Nhap ma sinh vien can xoa: '))
    j=0
    for i in range(0,len(LSV)):               
        if LSV[i].get("ma sv")==msv:
            j=j+1
            LSV.remove(LSV[i])
    if j==0:
        print('Khong co sinh vien nay !')
                

def tinhdiem():    
    for i in range (0,len(LSV)):
        dtk = (LSV[i].get("diem giua ki")+LSV[i].get("diem cuoi ki")+LSV[i].get("diem chuyen can"))/3
        LSV[i]["diem tong ket"]=dtk
    print('STT \t mssv \t Tên \t Giới tính \t Tổ \t Ngày tháng năm sinh\t Điểm giữa kì \t Điểm cuối kì \t Điểm chuyên cần \t Điểm tổng kết ')
    for i in range(0,len(LSV)):
        print((i+1) , "\t" , LSV[i]["ma sv"] , "\t" , LSV[i]["ten"] , "\t" , LSV[i]["gioi tinh"] , "\t\t" , LSV[i]["to"] , "\t\t" , LSV[i]["sinh nhat"] ,"\t\t" , LSV[i]["diem giua ki"] ,"\t\t", LSV[i]["diem cuoi ki"] , "\t\t", LSV[i]["diem chuyen can"] ,"\t\t", LSV[i]["diem tong ket"] )
      
    

def suathongtin():
    id = int(input('Nhap ma sinh vien can sua: '))
    chon = int(input('Chon thong tin muon sua:\n1.Ten\n2.ma sinh vien\n3.gioi tinh\n4.To\n5.Diem giua ki\n6.Diem cuoi ki\n7.Diem chuyen can\n8.Ngay thang nam sinh\n')) 
    j=0
    for i in range(0,len(LSV)):
        if LSV[i].get("ma sv")==id:
            if chon == 1:
                ten = input('Nhap ten moi ')
                LSV[i]["ten"] = ten
            elif chon == 2:
                masv = int(input('Nhap ma sinh vien moi '))
                LSV[i]["ma sv"] = masv
            elif chon == 3:
                gt = input('Nhap lai gioi tinh ')
                LSV[i]["gioi tinh"] = gt
            elif chon == 4:
                to = int(input('nhap lai to '))
                LSV[i]["to"] = to
            elif chon == 5:
                dgk = float(input('nhap lai diem giua ki '))
                LSV[i]["diem giua ki"] = dgk
            elif chon == 6:
                dck = float(input('nhap lai diem cuoi ki '))
                LSV[i]["diem cuoi ki"] = dck
            elif chon == 7:
                dcc = float(input('nhap lai diem chuyen can '))
                LSV[i]["diem chuyen can"] = dcc
            elif chon == 8:
                sn = input('Nhap lai ngay thang nam sinh')
                LSV[i]["sinh nhat"] = sn
            j=j+1
        if j==0:
            print('Khong co sinh vien nay !')
            
print('\t\t\t\t\tCHUONG TRINH QUAN LY SINH VIEN PYTHON')
n = int(input('Nhap so sinh vien '))
nhap()
while True:    
    print('Chon cac chuc nang\n1.Chinh sua thong tin sinh vien\n2.Them sinh vien\n3.Tim sinh vien\n4.Xoa sinh vien\n5.Tinh diem cuoi ki\n6.Xuat\n7.Thoat')
    luachon = int(input('Nhap lua chon '))
    if luachon == 1:
        suathongtin()        
    elif luachon == 2:
        themsv()        
    elif luachon == 3:
        timsv()         
    elif luachon == 4:
        xoasv()        
    elif luachon == 5:
        tinhdiem()        
    elif luachon == 6:
        xuat()
    elif luachon == 7:
        break
    else:
        print('Moi ban nhap lai')
    
       
    





