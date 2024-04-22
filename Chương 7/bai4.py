class DoThi:
    def __init__(self, V):
        self.V = V  # Số lượng đỉnh
        self.dinh_ke = [[] for _ in range(V)]  # Danh sách kề của mỗi đỉnh
   # Thêm cạnh vào đồ thị
    def them_canh(self, u, v):
        self.dinh_ke[u].append(v)
    # Hàm hỗ trợ cho DFS
    def _DFS(self, u, visited, recStack):
        visited[u] = True  # Đánh dấu đỉnh hiện tại là đã thăm
        recStack[u] = True  # Đánh dấu đỉnh hiện tại là đã thăm và nằm trong stack đang xét

        # Duyệt qua các đỉnh kề của đỉnh hiện tại
        for v in self.dinh_ke[u]:
            if not visited[v]:  # Nếu đỉnh kề chưa được thăm, tiến hành duyệt đỉnh kề đó
                if self._DFS(v, visited, recStack):  # Nếu hàm đệ quy trả về True, tức là tìm thấy chu trình
                    return True
            elif recStack[v]:  # Nếu đỉnh kề đã được thăm và nằm trong stack đang xét, tức là tìm thấy chu trình
                return True
        recStack[u] = False  # Khi kết thúc duyệt đỉnh u, loại bỏ đỉnh u khỏi stack đang xét
        return False
    # Phương thức kiểm tra xem đồ thị có chu trình hay không
    def ChuTrinh(self):
        visited = [False] * self.V  # Mảng đánh dấu các đỉnh đã thăm
        recStack = [False] * self.V  # Mảng đánh dấu các đỉnh nằm trong stack đang xét

        # Duyệt qua tất cả các đỉnh trong đồ thị
        for u in range(self.V):
            if not visited[u]:  # Nếu đỉnh chưa được thăm, thực hiện DFS từ đỉnh đó
                if self._DFS(u, visited, recStack):  # Nếu hàm DFS trả về True, tức là tìm thấy chu trình
                    return True
        return False  # Không tìm thấy chu trình trong đồ thị
# Hàm main để kiểm tra
if __name__ == "__main__":
    print("Nhập số đỉnh của đồ thị:")
    V = int(input())
    print("Nhập số cạnh của đồ thị:")
    E = int(input())
    dt = DoThi(V)
    print("Nhập các cạnh của đồ thị:")
    for _ in range(E):
        u, v = map(int, input().split())
        dt.them_canh(u, v)
    if dt.ChuTrinh():
        print("Đồ thị có chu trình.")
    else:
        print("Đồ thị không có chu trình.")
