class Node:
    def __init__(self, val =0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right))+1
    
def traverse_all_levels(root):
    for i in range(height(root)):
        traverse_n_level(root, i)

def traverse_n_level(root, lvl):
    if root is None:
        return
    if lvl == 0:
        print(root.val)
        return
    traverse_n_level(root.left, lvl-1)
    traverse_n_level(root.right, lvl-1)

root = Node(1,Node(2, Node(4), Node(5)),Node(3))
traverse_all_levels(root)
