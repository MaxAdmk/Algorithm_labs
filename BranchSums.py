from collections import deque


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(root):
    if root is None:
        return 0

    queue = deque([(root, False)])
    total_sum = 0

    while queue:
        node, is_right = queue.popleft()

        if is_right and node.right is None and node.left is None:
            total_sum += node.value

        if node.left:
            queue.append((node.left, False))
        if node.right:
            queue.append((node.right, True))

    return total_sum

root = BinaryTree(3)
root.left = BinaryTree(9)
root.right = BinaryTree(20)
root.right.left = BinaryTree(15)
root.right.right = BinaryTree(7)

result = branchSums(root)
print(result)