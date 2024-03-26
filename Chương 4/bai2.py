class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class DanhSachLienKet:
    def __init__(self):
        self.head = None
    def them_phan_tu(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
    def DaoNguoc(self):
        if self.head is None:
            return 
        stack = []
        current = self.head
        while current:
            stack.append(current)
            current = current.next      
        self.head = stack.pop()
        current = self.head
        while stack:
            current.next = stack.pop()
            current = current.next
        current.next = None
    def in_danh_sach(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
# ví dụ
dslk = DanhSachLienKet()
dslk.them_phan_tu(1)
dslk.them_phan_tu(2)
dslk.them_phan_tu(3)
dslk.them_phan_tu(4)
print("Danh sách trước khi đảo ngược:")
dslk.in_danh_sach()
dslk.DaoNguoc()
print("Danh sách sau khi đảo ngược:")
dslk.in_danh_sach()
