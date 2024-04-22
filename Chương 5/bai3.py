class Nut:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
class CayNhiPhan:
    def __init__(self):
        self.goc = None
    def dem_nut_la(self, nut):
        # Nếu nut là None hoặc là nút lá, trả về 0
        if nut is None or (nut.left is None and nut.right is None):
            return 1
        # Đếm số nút lá của cây con bên trái và cây con bên phải
        so_nut_la_ben_trai = self.dem_nut_la(nut.left) if nut.left else 0
        so_nut_la_ben_phai = self.dem_nut_la(nut.right) if nut.right else 0
        # Tổng số nút lá là tổng số nút lá của cả hai cây con
        return so_nut_la_ben_trai + so_nut_la_ben_phai
    def nhap_cay(self):
        # Hàm này cho phép người dùng nhập dữ liệu cho cây
        def nhap_nut():
            info = int(input("Nhập giá trị của nút (hoặc nhập -1 nếu là nút lá): "))
            if info == -1:
                return None
            nut = Nut(info)
            nut.left = nhap_nut()
            nut.right = nhap_nut()
            return nut
        
        self.goc = nhap_nut()

    def SoNutLa(self):
        return self.dem_nut_la(self.goc)


def main():
    cay = CayNhiPhan()
    cay.nhap_cay()
    print("Số nút lá của cây là:", cay.SoNutLa())

if __name__ == "__main__":
    main()
