class Node:
    def __init__(self, val =0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
def inorder_traversal(root):
    if root is None:
        return
    inorder_traversal(root.left)
    ls.append(root.val)
    inorder_traversal(root.right)
    
def find_inorder_successor(root):
    while root.left:
        root = root.left
    return root
    
def delete_node_bst(root, parent, val):
    if root.val == val:
        if parent:
            if root.left is None and root.right is None:
                if parent.left == root:
                    parent.left = None
                else:
                    parent.right = None
            elif root.left is not None and root.right is not None:
                new_node = find_inorder_successor(root.right)
                delete_node_bst(root, None, new_node.val)
                new_node.left = root.left
                new_node.right = root.right
                if parent.left == root:
                    parent.left = new_node
                else:
                    parent.right = new_node
            else:
                if parent.left == root:
                    if root.left:
                        parent.left = root.left
                    else:
                        parent.left = root.right
                else:
                    if root.left:
                        parent.right = root.left
                    else:
                        parent.right = root.right
        else:
            if root.left is None and root.right is None:
                root = None
            elif root.left is not None and root.right is not None:
                new_node = find_inorder_successor(root.right)
                delete_node_bst(root, None, new_node.val)
                new_node.left = root.left
                new_node.right = root.right
                root.val = new_node.val
            else:
                if root.left:
                    root = root.left
                else:
                    root = root.right
                    
    elif root.val>val:
        delete_node_bst(root.left, root, val)
    else:
        delete_node_bst(root.right, root, val)
root = Node(2,Node(1), Node(7, Node(4, Node(3), Node(6, Node(5))), Node(8)))
ls = []
inorder_traversal(root)
print(ls)
ls.clear()
delete_node_bst(root, None, 2)
inorder_traversal(root)
print(ls)
ls.clear()
