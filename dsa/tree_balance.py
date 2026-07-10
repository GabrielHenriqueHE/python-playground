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


def avl_tree(root: TreeNode) -> TreeNode: ...


def red_black_tree(root: TreeNode) -> TreeNode: ...
