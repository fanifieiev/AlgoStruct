import unittest


from algostruct.tree.btree import *


class TestBTree(unittest.TestCase):

    def test_max_1(self):
        tree = BinaryTree(5)
        self.assertEqual(tree.max().value, 5)

    def test_max_2(self):
        tree = BinaryTree(5)
        tree.add(3)
        tree.add(1)
        tree.add(4)
        tree.add(0)
        self.assertEqual(tree.max().value, 5)

    def test_max_3(self):
        tree = BinaryTree(5)
        tree.add(3)
        tree.add(6)
        self.assertEqual(tree.max().value, 6)

    def test_min_1(self):
        tree = BinaryTree(5)
        self.assertEqual(tree.min().value, 5)

    def test_min_2(self):
        tree = BinaryTree(5)
        tree.add(6)
        tree.add(7)
        tree.add(8)
        tree.add(1)
        self.assertEqual(tree.min().value, 1)

    def test_nodeOf_1(self):
        tree = BinaryTree(5)
        tree.add(6)
        self.assertEqual(tree.nodeOf(6).value, 6)

    def test_nodeOf_2(self):
        tree = BinaryTree(5)
        tree.add(6)
        node = tree.nodeOf(10)
        print(node)
        self.assertEqual(node, None)

    def test_is_empty(self):
        tree = BinaryTree(None)
        self.assertEqual(tree.is_empty(), True)

    def test_height_1(self):
        #     5
        #    / \
        #   4   6
        #  /     \
        # 3       7
        #          \
        #           8
        tree = BinaryTree(5)
        tree.add(4)
        tree.add(3)
        tree.add(6)
        tree.add(7)
        tree.add(8)
        height = tree.height()
        self.assertEqual(height, 4)

    def test_sorted(self):
        tree = BinaryTree(5)
        tree.add(4)
        tree.add(3)
        tree.add(6)
        tree.add(7)
        tree.add(8)
        sorting = tree.sorted()
        self.assertEqual(sorting, [3, 4, 5, 6, 7, 8])

    def test_in_order_iterator_1(self):
        #     5
        #    / \
        #   4   6
        #  /     \
        # 3       7
        #          \
        #           8
        tree = BinaryTree(5)
        tree.add(4)
        tree.add(3)
        tree.add(6)
        tree.add(7)
        tree.add(8)
        iterator = InOrderIterator(tree)
        values = []
        for node in iterator:
            values.append(node.value)
        self.assertEqual(values, [3, 4, 5, 6, 7, 8])

    def test_pre_order_iterator_1(self):
        #     5
        #    / \
        #   4   6
        #  /     \
        # 3       7
        #          \
        #           8
        tree = BinaryTree(5)
        tree.add(4)
        tree.add(3)
        tree.add(6)
        tree.add(7)
        tree.add(8)
        iterator = PreOrderIterator(tree)
        values = []
        for node in iterator:
            values.append(node.value)
        self.assertEqual(values, [5, 4, 3, 6, 7, 8])
