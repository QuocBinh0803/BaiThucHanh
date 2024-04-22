class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]
    def add_edge(self, u, v):
        self.graph[u].append(v)

    def SoCungRa(self, v):
        if v < 0 or v >= self.V:
            return "Đỉnh không tồn tại trong đồ thị"     
        return len(self.graph[v])
# Khởi tạo đồ thị
V = int(input("Nhập số đỉnh của đồ thị: "))
g = Graph(V)
# Nhập số cung của đồ thị
E = int(input("Nhập số cung của đồ thị: "))
# Nhập các cung của đồ thị
print("Nhập các cung của đồ thị (u v):")
for _ in range(E):
    u, v = map(int, input().split())
    g.add_edge(u, v)
# Nhập đỉnh để tính số cung đi ra
vertex = int(input("Nhập đỉnh v: "))
print("Số cung đi ra khỏi đỉnh", vertex, "là:", g.SoCungRa(vertex))
