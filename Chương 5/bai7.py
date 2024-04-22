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
    def sao_chep_cay(self, nut):
        # Hàm này thực hiện sao chép một cây bắt đầu từ nút đã cho
        if nut is None:
            return None
        new_nut = Nut(nut.info)
        new_nut.left = self.sao_chep_cay(nut.left)
        new_nut.right = self.sao_chep_cay(nut.right)
        return new_nut
    def Chep(self):
        # Hàm này trả về một cây mới được sao chép từ cây gốc
        return CayNhiPhan(self.sao_chep_cay(self.goc))
def main():
    cay_goc = CayNhiPhan()
    cay_goc.nhap_cay()   
    # Sao chép cây gốc để tạo một cây mới
    cay_moi = cay_goc.Chep()
    # In cây mới
    print("Cây mới đã được sao chép từ cây gốc:")
    cay_moi.in_cay()
if __name__ == "__main__":
    main()
