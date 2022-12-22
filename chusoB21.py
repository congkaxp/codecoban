n = int(input('Nhập n: '))
so_dao_nguoc = ''
while (n != 0):
    so_dao_nguoc += str(n % 10)
    n = n // 10
so_dao_nguoc = int(so_dao_nguoc) 
 
while (so_dao_nguoc != 0):
    print(list(so_dao_nguoc % 10), end= ',')
    so_dao_nguoc = so_dao_nguoc // 10
