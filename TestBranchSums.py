import unittest
from BranchSums import BinaryTree, branchSums

class TestBranchSums(unittest.TestCase):

    def test_tree(self):
        root = BinaryTree(3)
        root.left = BinaryTree(9)
        root.right = BinaryTree(20)
        root.right.left = BinaryTree(15)
        root.right.right = BinaryTree(7)
        self.assertEqual(branchSums(root), 24)

if __name__ == "__main__":
    unittest.main()
