class DoThi:
    def __init__(self, so_dinh):
        self.so_dinh = so_dinh
        self.ds_ke = [[] for _ in range(so_dinh)]
    def them_canh(self, dinh1, dinh2):
        self.ds_ke[dinh1].append(dinh2)
        self.ds_ke[dinh2].append(dinh1)
    def DFS(self, dinh, da_tham):
        da_tham[dinh] = True
        for dinh_ke in self.ds_ke[dinh]:
            if not da_tham[dinh_ke]:
                self.DFS(dinh_ke, da_tham)
    def LienThong(self):
        # Khởi tạo mảng đánh dấu đã thăm
        da_tham = [False] * self.so_dinh

        # Chọn một đỉnh bất kỳ làm đỉnh xuất phát và thực hiện DFS
        self.DFS(0, da_tham)
        # Kiểm tra xem tất cả các đỉnh đã được thăm chưa
        return all(da_tham)
# Hàm nhập đồ thị từ bàn phím
def nhap_do_thi():
    so_dinh = int(input("Nhập số đỉnh của đồ thị: "))
    dt = DoThi(so_dinh)
    print("Nhập các cạnh của đồ thị (mỗi cạnh ghi cặp đỉnh kề nhau):")
    while True:
        canh = input("Nhập cạnh (hoặc nhấn Enter để kết thúc): ")
        if not canh:
            break
        dinh1, dinh2 = map(int, canh.split())
        dt.them_canh(dinh1, dinh2)
    return dt
# Hàm main
def main():
    dt = nhap_do_thi()
    # Kiểm tra xem đồ thị có liên thông không
    if dt.LienThong():
        print("Đồ thị là đồ thị liên thông.")
    else:
        print("Đồ thị không là đồ thị liên thông.")
if __name__ == "__main__":
    main()
