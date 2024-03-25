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
def nhom_cot_giong_nhau(matran):
    n = len(matran)
    cot = []
    for j in range(n):
        cot.append([matran[i][j] for i in range(n)])
    nhom_cot = {}
    for i in range(n):
        col = tuple(cot[i])
        if col in nhom_cot:
            nhom_cot[col].append(i)
        else:
            nhom_cot[col] = [i]
    for key, value in nhom_cot.items():
        print("Nhóm chỉ mục cột giống nhau:", value)
ma_tran = nhap_ma_tran_vuong()
nhom_cot_giong_nhau(ma_tran)
