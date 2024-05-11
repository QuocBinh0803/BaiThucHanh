class TuDien:
    def __init__(self):
        self.du_lieu = {}

    def NhapTu(self, tu, dong_nghia=None, trai_nghia=None):
        key = self.BamTu(tu)
        value = {'dong_nghia': dong_nghia, 'trai_nghia': trai_nghia}
        self.du_lieu[key] = value

    def BamTu(self, tu):
        return tu[0].lower()  # Hàm băm lấy ký tự đầu tiên của từ

    def DongNghia(self, tu):
        key = self.BamTu(tu)
        if key in self.du_lieu and self.du_lieu[key]['dong_nghia']:
            return self.du_lieu[key]['dong_nghia']
        else:
            return []

    def TraiNghia(self, tu):
        key = self.BamTu(tu)
        if key in self.du_lieu and self.du_lieu[key]['trai_nghia']:
            return self.du_lieu[key]['trai_nghia']
        else:
            return []
# Sử dụng lớp TuDien
tudien = TuDien()
# Thêm từ vào từ điển
tudien.NhapTu('mèo', ['cat', 'kitty'], ['chó', 'doggy'])
tudien.NhapTu('cá', ['fish'], ['chim', 'bird'])
# Tra cứu từ đồng nghĩa và từ trái nghĩa
print("Từ đồng nghĩa của 'mèo':", tudien.DongNghia('mèo'))
print("Từ trái nghĩa của 'mèo':", tudien.TraiNghia('mèo'))
print("Từ đồng nghĩa của 'cá':", tudien.DongNghia('cá'))
print("Từ trái nghĩa của 'cá':", tudien.TraiNghia('cá'))
