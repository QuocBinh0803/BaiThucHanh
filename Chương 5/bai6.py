class Nut:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
class CayNhiPhan:
    def __init__(self):
        self.goc = None
    def nhap_cay(self):
        # Hàm này cho phép người dùng nhập dữ liệu cho cây từ bàn phím
        def nhap_nut():
            giatri = int(input("Nhập giá trị của nút (hoặc nhập -1 nếu muốn bỏ qua nút này): "))
            if giatri == -1:
                return None
            nut = Nut(giatri)
            nut.left = nhap_nut()
            nut.right = nhap_nut()
            return nut       
        self.goc = nhap_nut()
    def chieu_cao(self, nut):
        # Hàm này tính chiều cao của một cây con tại một nút
        if nut is None:
            return 0
        return 1 + max(self.chieu_cao(nut.left), self.chieu_cao(nut.right))

    def KiemTraAVL(self):
        # Hàm này kiểm tra xem cây có phải là cây AVL không
        def kiem_tra_avl(nut):
            if nut is None:
                return True
            # Tính độ chênh lệch chiều cao giữa cây con bên trái và cây con bên phải của mỗi nút
            chenh_lech = abs(self.chieu_cao(nut.left) - self.chieu_cao(nut.right))
            # Nếu độ chênh lệch lớn hơn 1, cây không cân bằng
            if chenh_lech > 1:
                return False
            # Kiểm tra cân bằng của cây con bên trái và cây con bên phải của nút hiện tại
            return kiem_tra_avl(nut.left) and kiem_tra_avl(nut.right)    
        return kiem_tra_avl(self.goc)
def main():
    cay = CayNhiPhan()
    cay.nhap_cay()
    print("Cây là một cây AVL:", cay.KiemTraAVL())
if __name__ == "__main__":
    main()
