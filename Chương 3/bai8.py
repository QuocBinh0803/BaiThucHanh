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
            current.ke_tiep = Node(he_so, so_mu)
            current.ke_tiep.ke_tiep = self.head  
    def RutGon(self):
        if self.head is None:
            return
        current = self.head
        while current is not None:
            next_node = current.ke_tiep
            while next_node is not self.head:
                if next_node.so_mu == current.so_mu:
                    current.he_so += next_node.he_so
                    current.ke_tiep = next_node.ke_tiep
                    next_node = current.ke_tiep
                else:
                    next_node = next_node.ke_tiep
            current = current.ke_tiep
        prev = None
        current = self.head
        while current.ke_tiep is not self.head:
            if current.he_so == 0:
                if prev is None:
                    self.head = current.ke_tiep
                else:
                    prev.ke_tiep = current.ke_tiep
            else:
                prev = current
            current = current.ke_tiep
        if current.he_so == 0:
            if prev is None:
                self.head = None
            else:
                prev.ke_tiep = None
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
dathuc.them_so_hang(-3, 2)  
dathuc.them_so_hang(2, 0)

print("Danh thức gốc:")
dathuc.in_danh_thuc()
dathuc.RutGon()
print("Danh thức sau khi rút gọn:")
dathuc.in_danh_thuc()
