class BaiToan:
    def __init__(self, bt):
        self.bt = bt
    def HauTo(self):
        if not self.bt:
            return None
        def la_toan_tu(char):
            return char in {'+', '-', '*', '/'}
        def do_uu_tien(toan_tu):
            if toan_tu in {'+', '-'}:
                return 1
            elif toan_tu in {'*', '/'}:
                return 2
            return 0  
        stack_toan_tu = []
        hau_to = []
        i = 0
        while i < len(self.bt):
            char = self.bt[i]
            if char == ' ':
                i += 1
                continue
            elif char.isdigit():
                so_hang = char
                while i + 1 < len(self.bt) and self.bt[i + 1].isdigit():
                    so_hang += self.bt[i + 1]
                    i += 1
                hau_to.append(so_hang)
            elif la_toan_tu(char):
                while stack_toan_tu and do_uu_tien(stack_toan_tu[-1]) >= do_uu_tien(char):
                    hau_to.append(stack_toan_tu.pop())
                stack_toan_tu.append(char)
            elif char == '(':
                stack_toan_tu.append(char)
            elif char == ')':
                while stack_toan_tu and stack_toan_tu[-1] != '(':
                    hau_to.append(stack_toan_tu.pop())
                stack_toan_tu.pop()  # Loại bỏ '('
            i += 1
        while stack_toan_tu:
            hau_to.append(stack_toan_tu.pop())

        return ' '.join(hau_to)
# ví dụ
bt = "2 + 3 * 5"
bai_toan = BaiToan(bt)
print("Biểu thức hậu tố:", bai_toan.HauTo())
