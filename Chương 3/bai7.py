class Node:
    def __init__(self, he_so, so_mu):
        self.he_so = he_so
        self.so_mu = so_mu
        self.ke_tiep = None
class DanhThuc:
    def __init__(self):
        self.head = None
    def them_so_hang(self, he_so, so_mu):
        if self.head is None:
            self.head = Node(he_so, so_mu)
            self.head.ke_tiep = self.head  
        else:
            current = self.head
            while current.ke_tiep is not self.head:
                current = current.ke_tiep
            new_node = Node(he_so, so_mu)
            new_node.ke_tiep = self.head 
            current.ke_tiep = new_node  
    def in_danh_thuc(self):
        if self.head is None:
            print("Danh sách liên kết trống.")
            return
        current = self.head
        while True:
            print(f"{current.he_so}x^{current.so_mu}", end="")
            current = current.ke_tiep
            if current is self.head:  
                break
            print(" + ", end="")
        print()

# ví dụ
dathuc = DanhThuc()
dathuc.them_so_hang(3, 2)
dathuc.them_so_hang(4, 1)
dathuc.them_so_hang(2, 0)

print("Danh thức gốc:")
dathuc.in_danh_thuc()
