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

def co_hang_giong_nhau(matran):
    for i in range(len(matran)):
        for j in range(i + 1, len(matran)):
            if matran[i] == matran[j]:
                return True
    return False
ma_tran = nhap_ma_tran_vuong()
if co_hang_giong_nhau(ma_tran):
    print("Ma trận có ít nhất hai hàng giống nhau")
else:
    print("Ma trận không có ít nhất hai hàng giống nhau")
