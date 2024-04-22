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
    def DFS(self, v, visited):
        visited[v] = True
        for i in self.adj[v]:
            if not visited[i]:
                self.DFS(i, visited)
    def SoThanhPhan(self):
        visited = {}
        count = 0
        for v in self.adj:
            if v not in visited:
                self.DFS(v, visited)
                count += 1
        return count
# Nhập đồ thị từ bàn phím
dt = DoThi()
n = int(input("Nhập số đỉnh của đồ thị: "))
print("Nhập các cạnh của đồ thị (u, v):")
for _ in range(n):
    u, v = map(int, input().split())
    dt.themCanh(u, v)

# Tính và in ra số thành phần liên thông
print("Số thành phần liên thông của đồ thị là:", dt.SoThanhPhan())
