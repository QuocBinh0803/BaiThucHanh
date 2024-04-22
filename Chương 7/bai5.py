class DoThi:
    def __init__(self, so_dinh):
        self.so_dinh = so_dinh
        self.danh_sach_ke = [[] for _ in range(so_dinh)]

    def them_canh(self, dinh1, dinh2):
        self.danh_sach_ke[dinh1].append(dinh2)
        self.danh_sach_ke[dinh2].append(dinh1)

    def BacDinh(self, v):
        return len(self.danh_sach_ke[v])
if __name__ == "__main__":
    so_dinh = int(input("Nhập số đỉnh của đồ thị: "))
    dt = DoThi(so_dinh)
    # Nhập số cạnh của đồ thị
    so_canh = int(input("Nhập số cạnh của đồ thị: "))
    print("Nhập các cạnh của đồ thị (theo định dạng: dinh1 dinh2): ")
    for _ in range(so_canh):
        dinh1, dinh2 = map(int, input().split())
        dt.them_canh(dinh1, dinh2)
    # Nhập đỉnh cần tính bậc
    dinh = int(input("Nhập đỉnh cần tính bậc: "))
    print("Bậc của đỉnh {} là: {}".format(dinh, dt.BacDinh(dinh)))
