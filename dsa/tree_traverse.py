from typing import Union


class TreeNode:
    def __init__(
        self,
        val: int | None,
        left: Union["TreeNode", None] = None,
        right: Union["TreeNode", None] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


def preorder(node: Union[TreeNode, None]) -> None:
    if node is None:
        return

    print(node.val)

    if node.left is not None:
        preorder(node.left)

    if node.right is not None:
        preorder(node.right)


def inorder(node: Union[TreeNode, None]) -> None:
    if node is None:
        return

    if node.left is not None:
        inorder(node.left)

    print(node.val)

    if node.right is not None:
        inorder(node.right)


def postorder(node: Union[TreeNode, None]) -> None:
    if node is None:
        return

    if node.right is not None:
        postorder(node.right)

    if node.left is not None:
        postorder(node.left)

    print(node.val)


root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(2)

inorder(node=root)
