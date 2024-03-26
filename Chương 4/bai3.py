class BaiToan:
    def __init__(self, bt):
        self.bt = bt
    def GiaTri(self):
        if not self.bt:
            return None
        def chuyen_trung_to_sang_hau_to(bieu_thuc):
            stack_toan_tu = []
            stack_gia_tri = []
            prec = {'+': 1, '-': 1, '*': 2, '/': 2}
            for char in bieu_thuc:
                if char.isdigit():
                    stack_gia_tri.append(int(char))
                elif char == '(':
                    stack_toan_tu.append(char)
                elif char == ')':
                    while stack_toan_tu and stack_toan_tu[-1] != '(':
                        op = stack_toan_tu.pop()
                        num2 = stack_gia_tri.pop()
                        num1 = stack_gia_tri.pop()
                        if op == '+':
                            stack_gia_tri.append(num1 + num2)
                        elif op == '-':
                            stack_gia_tri.append(num1 - num2)
                        elif op == '*':
                            stack_gia_tri.append(num1 * num2)
                        elif op == '/':
                            stack_gia_tri.append(num1 // num2)
                    stack_toan_tu.pop()  # Loại bỏ '('
                else:
                    while stack_toan_tu and stack_toan_tu[-1] != '(' and prec[stack_toan_tu[-1]] >= prec[char]:
                        op = stack_toan_tu.pop()
                        num2 = stack_gia_tri.pop()
                        num1 = stack_gia_tri.pop()
                        if op == '+':
                            stack_gia_tri.append(num1 + num2)
                        elif op == '-':
                            stack_gia_tri.append(num1 - num2)
                        elif op == '*':
                            stack_gia_tri.append(num1 * num2)
                        elif op == '/':
                            stack_gia_tri.append(num1 // num2)
                    stack_toan_tu.append(char)

            while stack_toan_tu:
                op = stack_toan_tu.pop()
                num2 = stack_gia_tri.pop()
                num1 = stack_gia_tri.pop()
                if op == '+':
                    stack_gia_tri.append(num1 + num2)
                elif op == '-':
                    stack_gia_tri.append(num1 - num2)
                elif op == '*':
                    stack_gia_tri.append(num1 * num2)
                elif op == '/':
                    stack_gia_tri.append(num1 // num2)
            
            return stack_gia_tri[0]

        return chuyen_trung_to_sang_hau_to(self.bt)
bt = input("Nhập biểu thức số học: ")
bai_toan = BaiToan(bt)
print("Giá trị của biểu thức:", bai_toan.GiaTri())
