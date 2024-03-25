def nhap_ma_tran_vuong():
    n = int(input("Nhập kích thước của ma trận vuông: "))
    matran = []
    print("Nhập các phần tử của ma trận:")
    for i in range(n):
        hang = []
        for j in range(n):
            phan_tu = int(input(f"Nhập phần tử ở hàng {i+1}, cột {j+1}: "))
            hang.append(phan_tu)
        matran.append(hang)
    return matran
def la_ma_tran_doi_xung(matran):
    if len(matran) != len(matran[0]):
        return False
    n = len(matran)
    for i in range(n):
        for j in range(i+1, n):
            if matran[i][j] != matran[j][i]:
                return False
    return True
ma_tran = nhap_ma_tran_vuong()
if la_ma_tran_doi_xung(ma_tran):
    print("Ma trận là ma trận đối xứng")
else:
    print("Ma trận không phải là ma trận đối xứng")
