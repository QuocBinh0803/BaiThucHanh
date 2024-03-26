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
    def in_nguoc_khong_de_qui(self):
        stack = []
        current = self.head
        while current:
            stack.append(current.data)
            current = current.next
        while stack:
            print(stack.pop(), end=" ")
dslk = DanhSachLienKet()
n = int(input("Nhập số lượng phần tử: "))
for i in range(n):
    data = int(input(f"Nhập giá trị cho phần tử thứ {i + 1}: "))
    dslk.them_phan_tu(data)
print("In ngược danh sách (không sử dụng đệ qui):")
dslk.in_nguoc_khong_de_qui()
