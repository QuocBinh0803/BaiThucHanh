class DoThi:
    def __init__(self):
        self.adj = {}
    def themCanh(self, u, v):
        if u not in self.adj:
            self.adj[u] = []
        if v not in self.adj:
            self.adj[v] = []
        self.adj[u].append(v)
        self.adj[v].append(u)
    def ChuaDinh(self, v):
        if v in self.adj:
            return True
        return False
# Nhập đồ thị từ bàn phím
dt = DoThi()
print("Nhập số cạnh của đồ thị:")
num_edges = int(input())
print("Nhập các cạnh của đồ thị (u, v):")
for _ in range(num_edges):
    u, v = map(int, input().split())
    dt.themCanh(u, v)
# Nhập và kiểm tra một đỉnh cụ thể
dinh = int(input("Nhập đỉnh cần kiểm tra: "))
if dt.ChuaDinh(dinh):
    print(f"Đỉnh {dinh} tồn tại trong đồ thị.")
else:
    print(f"Đỉnh {dinh} không tồn tại trong đồ thị.")
