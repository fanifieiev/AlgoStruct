from typing import TypeVar, Generic, List

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

    def __init__(self, value: V):
        self.root = BinaryNode(value)

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

    def nodeOf(self, value: V) -> BinaryNode[V]:
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

    def max(self) -> BinaryNode[V]:
        def _max(node: BinaryNode[V]) -> BinaryNode[V]:
            if node.right is None:
                return node
            else:
                return _max(node.right)

        return _max(self.root)

    def min(self) -> BinaryNode[V]:
        def _min(node: BinaryNode[V]) -> BinaryNode[V]:
            if node.left is None:
                return node
            else:
                return _min(node.left)

        return _min(self.root)

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

    def _in_order(self, node: BinaryNode[V], action):
        if node.left:
            self._in_order(node.left, action)
        action(node)
        if node.right:
            self._in_order(node.right, action)

    def _pre_order(self, node: BinaryNode[V], action):
        action(node)
        if node.left:
            self._pre_order(node.left, action)

        if node.right:
            self._pre_order(node.right, action)

    def _post_order(self, node: BinaryNode[V], action):
        if node.left:
            self._post_order(node.left, action)
        if node.right:
            self._post_order(node.right, action)
        action(node)


class PreOrderIterator(Generic[V]):
    """
    """

    def __init__(self, tree: BinaryTree[V]) -> None:
        self.stack = [tree.root]

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
        self.node = tree.root
        self.stack = []
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
