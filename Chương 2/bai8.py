def nhap_ma_tran_vuong():
    n = int(input("Nhập kích thước của ma trận vuông: "))
    matran = []
    print("Nhập các hàng của ma trận:")
    for i in range(n):
        hang = []
        for j in range(n):
            phan_tu = int(input(f"Nhập phần tử ở hàng {i+1}, cột {j+1}: "))
            hang.append(phan_tu)
        matran.append(hang)
    
    return matran
def la_ma_tran_tam_giac_duoi(matran):
    n = len(matran)
    for i in range(n):
        for j in range(i):
            if matran[i][j] != 0:
                return False
    return True

ma_tran = nhap_ma_tran_vuong()
if la_ma_tran_tam_giac_duoi(ma_tran):
    print("Ma trận là ma trận tam giác dưới")
else:
    print("Ma trận không phải là ma trận tam giác dưới")
