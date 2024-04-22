class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def ChieuCao(self, root):
        if root is None:
            return 0
        else:
            left_height = self.ChieuCao(root.left)
            right_height = self.ChieuCao(root.right)
            return max(left_height, right_height) + 1

def build_tree():
    print("Nhập giá trị cho các nút của cây (nhập -1 để dừng):")
    root_data = int(input("Nhập giá trị cho nút gốc: "))
    if root_data == -1:
        return None
    root = Node(root_data)
    print("Nhập cây con bên trái của", root_data)
    root.left = build_tree()
    print("Nhập cây con bên phải của", root_data)
    root.right = build_tree()
    return root

tree = BinaryTree()
tree.root = build_tree()

print("Chiều cao của cây nhị phân:", tree.ChieuCao(tree.root))
