from typing import Tuple, TypeVar, Generic, List
from collections import deque

V = TypeVar("V")


class BinaryNode(Generic[V]):
    """
    docstring
    """

    def __init__(self, value: V):
        self.value = value
        self.left: BinaryNode[V] = None
        self.right: BinaryNode[V] = None


class BinaryTree(Generic[V]):
    """
    docstring
    """

    def __init__(self, node: BinaryNode[V]):
        self.root = node

    def head(self) -> BinaryNode:
        return self.root

    def add(self, value: V) -> None:
        self._add_to(self.root, value)

    def _add_to(self, node: BinaryNode[V], value: V) -> None:
        if node.value > value:
            if node.left is None:
                node.left = BinaryNode(value)
            else:
                self._add_to(node.left, value)
        else:
            if node.right is None:
                node.right = BinaryNode(value)
            else:
                self._add_to(node.right, value)

    def node_of(self, value: V) -> BinaryNode[V]:
        def _nodeOf(node: BinaryNode[V], value: V):
            if node is None:
                return None
            elif node.value == value:
                return node
            elif node.value > value:
                return _nodeOf(node.left, value)
            else:
                return _nodeOf(node.right, value)
        return _nodeOf(self.root, value)

    def node_and_parent_of(self, value: V) -> Tuple[BinaryNode[V], BinaryNode[V]]:
        def _nodeOf(node, parent, value):
            if node is None:
                return None
            elif node.value == value:
                return (node, parent)
            elif node.value > value:
                return _nodeOf(node.left, node, value)
            else:
                return _nodeOf(node.right, node, value)
        return _nodeOf(self.root, None, value)

    def max(self) -> BinaryNode[V]:
        node = self.root
        while node.right:
            node = node.right
        return node

    def min(self) -> BinaryNode[V]:
        return self.min_of(self.root)

    def min_of(self, node: BinaryNode[V]) -> BinaryNode[V]:
        while node.left:
            node = node.left
        return node

    def is_empty(self) -> bool:
        return self.root is None or self.root.value is None

    def height(self) -> int:
        def _height(node: BinaryNode[V]):
            if node:
                return max(_height(node.left), _height(node.right)) + 1
            else:
                return 0
        return _height(self.root)

    def sorted(self) -> List[V]:
        values = []
        iterator = InOrderIterator(self)
        for node in iterator:
            values.append(node.value)
        return values

    def remove(self, value: V):
        def _remove_node(node, value):
            if node is None:
                return None
            elif value < node.value:
                node.left = _remove_node(node.left, value)
            elif value > node.value:
                node.right = _remove_node(node.right, value)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                else:
                    leftmost = self.min_of(node.right)
                    node.value = leftmost.value
                    node.right = _remove_node(node.right, leftmost.value)
            return node
        _remove_node(self.root, value)

    def reverted(self):
        def revert(node):
            if node:
                node.left, node.right = node.right, node.left
                revert(node.left)
                revert(node.right)
        cloned = self.clone()
        revert(cloned.root)
        return cloned

    def clone(self):
        def clone_node(node):
            if node:
                new_node = BinaryNode(node.value)
                new_node.left = clone_node(node.left)
                new_node.right = clone_node(node.right)
                return new_node
            return None
        cloned = clone_node(self.root)
        return BinaryTree(cloned)


class BreadFirstIterator(Generic[V]):
    """
    Breadth first traversing iterator
    """

    def __init__(self, tree: BinaryTree[V]) -> None:
        self.queue = deque()
        self.queue.append(tree.head())

    def __iter__(self):
        return self

    def __next__(self) -> BinaryNode[V]:
        if len(self.queue) > 0:
            node = self.queue.popleft()
            if node.left:
                self.queue.append(node.left)
            if node.right:
                self.queue.append(node.right)    
            return node
        else:
            raise StopIteration


class PreOrderIterator(Generic[V]):
    """
    """

    def __init__(self, tree: BinaryTree[V]) -> None:
        self.stack = deque()
        self.stack.append(tree.root)

    def __iter__(self):
        return self

    def __next__(self) -> BinaryNode[V]:
        if len(self.stack) > 0:
            node = self.stack.pop()
            if node.right:
                self.stack.append(node.right)
            if node.left:
                self.stack.append(node.left)
            return node
        else:
            raise StopIteration


class InOrderIterator(Generic[V]):
    """
    In order traversal iterator based on stack
    """

    def __init__(self, tree: BinaryTree[V]) -> None:
        self.node = tree.head()
        self.stack = deque()
        self._push_left(self.node)

    def __iter__(self):
        return self

    def __next__(self) -> BinaryNode[V]:
        if len(self.stack) > 0:
            node = self.stack.pop()
            self._push_left(node.right)
            return node
        else:
            raise StopIteration

    def _push_left(self, node: BinaryNode[V]):
        while node:
            self.stack.append(node)
            node = node.left


class PostOrderIterator(Generic[V]):
    """
    Post order traversal iterator based on stack
    """

    def __init__(self, tree: BinaryTree[V]) -> None:
        self.stack = deque()
        self.node = tree.head()
        self.previous = None

    def __iter__(self):
        return self

    def __next__(self) -> BinaryNode[V]:
        if self.node != None or len(self.stack) != 0:
            if self.node != None:
                self.stack.append(self.node)
                self.node.left
            else:
                self.node = self.stack[-1]
                if self.node.right == None or self.node == self.previous:
                    pass
                else:
                    pass
        else:
            raise StopIteration
