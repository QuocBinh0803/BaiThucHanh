class Nut:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
class CayNhiPhan:
    def __init__(self):
        self.goc = None
    def dem_nut_trung_gian(self, nut):
        # Nếu nut là None hoặc là nút lá, trả về 0
        if nut is None or (nut.left is None and nut.right is None):
            return 0
        # Đếm số nút trung gian của cây con bên trái và cây con bên phải
        so_nut_trung_gian_ben_trai = self.dem_nut_trung_gian(nut.left) if nut.left else 0
        so_nut_trung_gian_ben_phai = self.dem_nut_trung_gian(nut.right) if nut.right else 0
        # Nếu nut không phải là nút lá và cũng không phải là nút gốc, thì nó là nút trung gian
        if nut.left or nut.right:
            return 1 + so_nut_trung_gian_ben_trai + so_nut_trung_gian_ben_phai
        else:
            return 0
    def nhap_cay(self):
        # Hàm này cho phép người dùng nhập dữ liệu cho cây từ bàn phím
        def nhap_nut():
            info = int(input("Nhập giá trị của nút (hoặc nhập -1 nếu là nút lá): "))
            if info == -1:
                return None
            nut = Nut(info)
            nut.left = nhap_nut()
            nut.right = nhap_nut()
            return nut
        
        self.goc = nhap_nut()

    def SoNutTrungGian(self):
        return self.dem_nut_trung_gian(self.goc)
def main():
    cay = CayNhiPhan()
    cay.nhap_cay()
    print("Số nút trung gian của cây là:", cay.SoNutTrungGian())

if __name__ == "__main__":
    main()
