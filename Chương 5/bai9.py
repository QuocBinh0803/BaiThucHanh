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
    def cay_con(self, nut1, nut2):
        # Hàm này kiểm tra xem cây bắt đầu từ nút nut2 có phải là cây con của cây bắt đầu từ nút nut1 không
        if nut2 is None:
            return True
        if nut1 is None:
            return False
        if nut1.info == nut2.info:
            return (self.cay_con(nut1.left, nut2.left) and
                    self.cay_con(nut1.right, nut2.right))
        return self.cay_con(nut1.left, nut2) or self.cay_con(nut1.right, nut2)
    def CayCon(self, cay2):
        # Hàm này trả về True nếu cây cay2 là cây con của cây hiện tại, ngược lại trả về False
        return self.cay_con(self.goc, cay2.goc)
def main():
    print("Nhập cây thứ nhất:")
    cay1 = CayNhiPhan()
    cay1.nhap_cay()
    
    print("Nhập cây thứ hai:")
    cay2 = CayNhiPhan()
    cay2.nhap_cay()

    # Kiểm tra cây thứ hai có phải là cây con của cây thứ nhất không
    if cay1.CayCon(cay2):
        print("Cây thứ hai là cây con của cây thứ nhất.")
    else:
        print("Cây thứ hai không là cây con của cây thứ nhất.")

if __name__ == "__main__":
    main()
