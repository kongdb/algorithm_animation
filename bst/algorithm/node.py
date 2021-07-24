# -*- coding:utf-8 -*-

from graph.element import GraphNode

class TreeNode(GraphNode):
    def __init__(self, value, left=None, right=None, p=None):
        self.value = value
        self.left = left
        self.right = right
        self.p = p
        GraphNode.__init__(self)


class AvlNode(TreeNode):
    def __init__(self, value, left=None, right=None, p=None):
        TreeNode.__init__(self, value, left, right, p)
        self.height = 1


class RBNode(TreeNode):
    def __init__(self, value, left=None, right=None, p=None, is_nil=False, color='red'):
        TreeNode.__init__(self, value, left, right, p)
        # color conflict with turtle color api
        self.node_color = color
        self.bh = 0 if is_nil else 1
        self.is_nil = is_nil

    def __bool__(self):
        return not self.is_nil