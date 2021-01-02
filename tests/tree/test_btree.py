import unittest


from algostruct.tree.btree import *


class TestBTree(unittest.TestCase):

    def test_max_1(self):
        tree = BinaryTree[int](BinaryNode[int](5))
        self.assertEqual(tree.max().value, 5)

    def test_max_2(self):
        tree = BinaryTree[int](BinaryNode[int](5))
        tree.add(3)
        tree.add(1)
        tree.add(4)
        tree.add(0)
        self.assertEqual(tree.max().value, 5)

    def test_max_3(self):
        tree = BinaryTree[int](BinaryNode[int](5))
        tree.add(3)
        tree.add(6)
        self.assertEqual(tree.max().value, 6)

    def test_min_1(self):
        tree = BinaryTree[int](BinaryNode[int](5))
        self.assertEqual(tree.min().value, 5)

    def test_min_2(self):
        tree = BinaryTree[int](BinaryNode[int](5))
        tree.add(6)
        tree.add(7)
        tree.add(8)
        tree.add(1)
        self.assertEqual(tree.min().value, 1)

    def test_node_of_1(self):
        tree = BinaryTree[int](BinaryNode[int](5))
        tree.add(6)
        self.assertEqual(tree.node_of(6).value, 6)

    def test_node_of_2(self):
        tree = BinaryTree[int](BinaryNode[int](5))
        tree.add(6)
        node = tree.node_of(10)
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
        tree = BinaryTree[int](BinaryNode[int](5))
        tree.add(4)
        tree.add(3)
        tree.add(6)
        tree.add(7)
        tree.add(8)
        height = tree.height()
        self.assertEqual(height, 4)

    def test_sorted(self):
        tree = BinaryTree[int](BinaryNode[int](5))
        tree.add(4)
        tree.add(3)
        tree.add(6)
        tree.add(7)
        tree.add(8)
        sorting = tree.sorted()
        self.assertEqual(sorting, [3, 4, 5, 6, 7, 8])

    def test_in_order_iterator_1(self):
        #     5
        #   /   \
        #  3     7
        #   \   / \
        #    4 6   8
        tree = BinaryTree[int](BinaryNode[int](5))
        tree.add(3)
        tree.add(4)
        tree.add(7)
        tree.add(6)
        tree.add(8)
        iterator = InOrderIterator(tree)
        values = []
        for node in iterator:
            values.append(node.value)
        print(values)
        self.assertEqual(values, [3, 4, 5, 6, 7, 8])
        
    def test_post_order_iterator_1(self):
        #     5
        #   /   \
        #  3     7
        #   \   / \
        #    4 6   8
        # tree = BinaryTree[int](BinaryNode[int](5))
        # tree.add(3)
        # tree.add(4)
        # tree.add(7)
        # tree.add(6)
        # tree.add(8)
        # iterator = PostOrderIterator(tree)
        # values = []
        # for node in iterator:
        #     values.append(node.value)
        # print(values)
        # self.assertEqual(values, [4, 3, 6, 8, 7, 5])
        pass    

    def test_pre_order_iterator_1(self):
        #     5
        #    / \
        #   4   6
        #  /     \
        # 3       7
        #          \
        #           8
        tree = BinaryTree[int](BinaryNode[int](5))
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

    def test_breadth_first_iterator_1(self):
        #     5
        #   /   \
        #  3     7
        #   \   / \
        #    4 6   8
        tree = BinaryTree[int](BinaryNode[int](5))
        tree.add(3)
        tree.add(4)
        tree.add(7)
        tree.add(6)
        tree.add(8)
        iterator = BreadFirstIterator(tree)
        values = []
        for node in iterator:
            values.append(node.value)
        print(values)
        self.assertEqual(values, [5, 3, 7, 4, 6, 8])

    def test_remove_node_1(self):
        #     5
        #    / \
        #   4   6
        #  /     \
        # 3(d)    7
        #          \
        #           8
        tree = BinaryTree[int](BinaryNode[int](5))
        tree.add(4)
        tree.add(3)
        tree.add(6)
        tree.add(7)
        tree.add(8)
        tree.remove(3)
        node = tree.node_of(4)
        self.assertEqual(node.left, None)

    def test_remove_node_2(self):
        #     5
        #    / \
        #   4   6
        #  /     \
        # 3       7(d)
        #          \
        #           8
        tree = BinaryTree[int](BinaryNode[int](5))
        tree.add(4)
        tree.add(3)
        tree.add(6)
        tree.add(7)
        tree.add(8)
        tree.remove(7)

    def test_remove_node_3(self):
        #     5
        #    / \
        #   4   9
        #  /   / \
        # 3   8   11
        #         /
        #        10
        tree = BinaryTree[int](BinaryNode[int](5))
        tree.add(4)
        tree.add(3)
        tree.add(9)
        tree.add(8)
        tree.add(11)
        tree.add(10)
        tree.remove(9)

        node = tree.node_of(10)
        self.assertEqual(node.right.value, 11)
        self.assertEqual(node.left.value, 8)

    def test_remove_node_4(self):
        #     5
        #    / \
        #   4   9
        #  /   / \
        # 3   8   11
        #         /
        #        10
        tree = BinaryTree[int](BinaryNode[int](5))
        tree.add(4)
        tree.add(3)
        tree.add(9)
        tree.add(8)
        tree.add(11)
        tree.add(10)
        tree.remove(5)

        node8 = tree.node_of(8)
        self.assertEqual(node8.right.value, 9)
        self.assertEqual(node8.left.value, 4)
        node9 = node8.right
        self.assertEqual(node9.right.value, 11)
        self.assertEqual(node9.left, None)
        
    def test_clone_1(self):
        #     5
        #    / \
        #   4   9
        tree = BinaryTree[int](BinaryNode[int](5))
        tree.add(4)
        tree.add(9)

        cloned_tree = tree.clone()
        self.assertEqual(cloned_tree.head().right.value, 9)

    def test_reverted_1(self):
        #     5
        #    / \
        #   4   9
        #  /   / \
        # 3   8   11
        #         /
        #        10
        tree = BinaryTree[int](BinaryNode[int](5))
        tree.add(4)
        tree.add(3)
        tree.add(9)
        tree.add(8)
        tree.add(11)
        tree.add(10)

        reverted: BinaryTree[int] = tree.reverted()
        #     5
        #   /   \
        #  9     4
        # / \     \
        # 11  8     3
        #     \
        #      10
        node1 = reverted.node_of(5)
        self.assertEqual(node1.right.value, 4)
        self.assertEqual(node1.left.value, 9)
