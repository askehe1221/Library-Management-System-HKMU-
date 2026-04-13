class Node():
    """二叉树节点"""
    def __init__(self, item):
        self.item = item
        self.lchild = None
        self.rchild = None

class Tree():
    """二叉树"""
    def __init__(self):
        self.root = None
    
    def add(self, item):
        """层序添加节点"""
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)
    
    def preorder(self, node):
        """前序遍历"""
        if node is None:
            return
        print(node.item, end=" ")
        self.preorder(node.lchild)
        self.preorder(node.rchild)
    
    def inorder(self, node):
        """中序遍历"""
        if node is None:
            return
        self.inorder(node.lchild)
        print(node.item, end=" ")
        self.inorder(node.rchild)
    
    def postorder(self, node):
        """后序遍历"""
        if node is None:
            return
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print(node.item, end=" ")
    
    def levelorder(self):
        """层序遍历"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.item, end=" ")
            if cur_node.lchild:
                queue.append(cur_node.lchild)
            if cur_node.rchild:
                queue.append(cur_node.rchild)
    
    def height(self, node):
        """计算树的高度"""
        if node is None:
            return 0
        left_height = self.height(node.lchild)
        right_height = self.height(node.rchild)
        return max(left_height, right_height) + 1
    
    def node_count(self, node):
        """计算节点数量"""
        if node is None:
            return 0
        return 1 + self.node_count(node.lchild) + self.node_count(node.rchild)
    
    def find(self, node, item):
        """查找节点"""
        if node is None:
            return None
        if node.item == item:
            return node
        left = self.find(node.lchild, item)
        if left:
            return left
        right = self.find(node.rchild, item)
        return right
    
    def find_min(self, node):
        """查找最小值节点"""
        if node is None:
            return None
        if node.lchild is None:
            return node
        return self.find_min(node.lchild)
    
    def find_max(self, node):
        """查找最大值节点"""
        if node is None:
            return None
        if node.rchild is None:
            return node
        return self.find_max(node.rchild)
    
    def is_empty(self):
        """检查树是否为空"""
        return self.root is None

# 测试
print("=== 测试二叉树 ===")
tree = Tree()

# 添加节点
for i in range(1, 8):
    tree.add(i)

print("\n前序遍历:")
tree.preorder(tree.root)

print("\n中序遍历:")
tree.inorder(tree.root)

print("\n后序遍历:")
tree.postorder(tree.root)

print("\n层序遍历:")
tree.levelorder()

print(f"\n\n树的高度: {tree.height(tree.root)}")
print(f"节点数量: {tree.node_count(tree.root)}")
print(f"树是否为空: {tree.is_empty()}")

# 查找测试
print("\n查找测试:")
node = tree.find(tree.root, 5)
print(f"查找值为5的节点: {'找到' if node else '未找到'}")

# 查找最大最小值
min_node = tree.find_min(tree.root)
max_node = tree.find_max(tree.root)
print(f"最小值: {min_node.item if min_node else '无'}")
print(f"最大值: {max_node.item if max_node else '无'}")


