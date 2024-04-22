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
    def so_sanh_cay(self, nut1, nut2):
        # Hàm này so sánh hai cây bắt đầu từ hai nút đã cho
        if nut1 is None and nut2 is None:
            return True
        elif nut1 is None or nut2 is None:
            return False
        else:
            return (nut1.info == nut2.info and
                    self.so_sanh_cay(nut1.left, nut2.left) and
                    self.so_sanh_cay(nut1.right, nut2.right))
    def SoSanh(self, cay2):
        # Hàm này trả về True nếu hai cây giống hệt hoàn toàn, ngược lại trả về False
        return self.so_sanh_cay(self.goc, cay2.goc)
def main():
    print("Nhập cây thứ nhất:")
    cay1 = CayNhiPhan()
    cay1.nhap_cay()
    
    print("Nhập cây thứ hai:")
    cay2 = CayNhiPhan()
    cay2.nhap_cay()
    # So sánh hai cây
    if cay1.SoSanh(cay2):
        print("Hai cây giống hệt nhau.")
    else:
        print("Hai cây không giống nhau.")
if __name__ == "__main__":
    main()
