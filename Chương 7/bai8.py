class DoThi:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]
    def themCanh(self, u, v):
        self.adj[u].append(v)
    def DFS(self, u, v, visited):
        if u == v:
            return True
        visited[u] = True
        for i in self.adj[u]:
            if not visited[i]:
                if self.DFS(i, v, visited):
                    return True
        return False
    def DuongDi(self, v1, v2):
        visited = [False] * self.V
        return self.DFS(v1, v2, visited)
# Hàm main để kiểm tra
if __name__ == "__main__":
    # Nhập số đỉnh và số cạnh của đồ thị
    V = int(input("Nhập số đỉnh của đồ thị: "))
    E = int(input("Nhập số cạnh của đồ thị: "))    
    # Tạo đồ thị
    dt = DoThi(V)
    # Nhập các cạnh của đồ thị
    print("Nhập các cạnh của đồ thị:")
    for _ in range(E):
        u, v = map(int, input().split())
        dt.themCanh(u, v)
    # Nhập hai đỉnh v1 và v2
    v1, v2 = map(int, input("Nhập hai đỉnh v1 và v2: ").split())
    # Kiểm tra xem có đường đi từ v1 đến v2 hay không
    if dt.DuongDi(v1, v2):
        print("Có đường đi từ đỉnh", v1, "đến đỉnh", v2)
    else:
        print("Không có đường đi từ đỉnh", v1, "đến đỉnh", v2)
