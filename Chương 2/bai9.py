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
def co_cot_giong_nhau(matran):
    n = len(matran)
    cot = []
    for j in range(n):
        cot.append([matran[i][j] for i in range(n)])
    for i in range(n):
        for j in range(i + 1, n):
            if cot[i] == cot[j]:
                return True
    return False
ma_tran = nhap_ma_tran_vuong()
if co_cot_giong_nhau(ma_tran):
    print("Ma trận có ít nhất hai cột giống nhau")
else:
    print("Ma trận không có ít nhất hai cột giống nhau")
