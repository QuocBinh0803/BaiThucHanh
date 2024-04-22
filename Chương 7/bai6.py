class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []
    def add_edge(self, start, end):
        self.edges.append((start, end))

    def SoCungVao(self, v):
        count = 0
        for edge in self.edges:
            if edge[1] == v:
                count += 1
        return count

# Hàm chính để thử nghiệm phương thức SoCungVao
def main():
    vertices = int(input("Nhập số đỉnh của đồ thị: "))
    dt = Graph(vertices)
    edges = int(input("Nhập số cung của đồ thị: "))
    for _ in range(edges):
        start, end = map(int, input("Nhập cung (start, end): ").split())
        dt.add_edge(start, end)
    v = int(input("Nhập đỉnh để tính số cung đi vào: "))
    print("Số cung đi vào đỉnh", v, "là:", dt.SoCungVao(v))

if __name__ == "__main__":
    main()
