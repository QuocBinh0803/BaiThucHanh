class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self):
        self.root = None
    def SoNut(self, root):
        if root is None:
            return 0
        else:
            return self.SoNut(root.left) + self.SoNut(root.right) + 1
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

print("Số nút của cây nhị phân:", tree.SoNut(tree.root))
