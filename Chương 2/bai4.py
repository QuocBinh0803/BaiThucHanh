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
def nhom_hang_giong_nhau(matran):
    nhom_hang = {}    
    for i in range(len(matran)):
        hang = matran[i]
        if tuple(hang) in nhom_hang:
            nhom_hang[tuple(hang)].append(i)
        else:
            nhom_hang[tuple(hang)] = [i]
    
    for key, value in nhom_hang.items():
        print("Nhóm hàng giống nhau:", value)

ma_tran = nhap_ma_tran_vuong()
nhom_hang_giong_nhau(ma_tran)
