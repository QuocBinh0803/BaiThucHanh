class TuDien:
    def __init__(self):
        self.tu_dong_nghia = {}
        self.tu_trai_nghia = {}

    def NhapTu(self):
        tu = input("Nhập từ: ")
        tu_dong_nghia = input("Nhập từ đồng nghĩa (nếu có): ")
        tu_trai_nghia = input("Nhập từ trái nghĩa (nếu có): ")
        self.tu_dong_nghia[tu] = tu_dong_nghia
        self.tu_trai_nghia[tu] = tu_trai_nghia

    def TraTu(self, tu):
        dong_nghia = self.tu_dong_nghia.get(tu)
        trai_nghia = self.tu_trai_nghia.get(tu)
        return dong_nghia, trai_nghia

# Ví dụ sử dụng lớp TuDien
tu_dien = TuDien()
tu_dien.NhapTu()

tu_can_tra = input("Nhập từ cần tra: ")
dong_nghia, trai_nghia = tu_dien.TraTu(tu_can_tra)
if dong_nghia:
    print(f"Từ đồng nghĩa của '{tu_can_tra}' là '{dong_nghia}'")
if trai_nghia:
    print(f"Từ trái nghĩa của '{tu_can_tra}' là '{trai_nghia}'")

