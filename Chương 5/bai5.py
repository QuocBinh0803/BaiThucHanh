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
    def kiem_tra_BST(self, nut, gioi_han_min=float('-inf'), gioi_han_max=float('inf')):
        # Nếu nut là None, nó là một cây BST
        if nut is None:
            return True        
        # Kiểm tra giới hạn của giá trị nút hiện tại
        if nut.info <= gioi_han_min or nut.info >= gioi_han_max:
            return False
        
        # Kiểm tra nút con bên trái và nút con bên phải với giới hạn thích hợp
        return (self.kiem_tra_BST(nut.left, gioi_han_min, nut.info) and
                self.kiem_tra_BST(nut.right, nut.info, gioi_han_max))
    def KiemTraBST(self):
        return self.kiem_tra_BST(self.goc)
def main():
    cay = CayNhiPhan()
    cay.nhap_cay()
    print("Cây là một cây BST:", cay.KiemTraBST())
if __name__ == "__main__":
    main()
