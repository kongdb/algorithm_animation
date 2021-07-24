# -*- coding:utf-8 -*-

from algorithm.bst import BinarySearchTree
from algorithm.node import AvlNode

class AvlTree(BinarySearchTree):
    def __init__(self):
        BinarySearchTree.__init__(self)


    def insert(self, value):
        parent = self._insert_node(value)
        self.balance(parent)
        self.graph.reset_style(self.root)


    def delete(self, value):
        _, balance_node = self._delete_node(value)
        # buggy
        self.balance(balance_node)
        self.graph.reset_style(self.root)


    def _create_node(self, value, parent):
        node = AvlNode(value, p = parent)
        node.draw(line_status=-1)
        return node

    def _height(self, node):
        return 0 if not node else node.height

    def balance(self, node):
        while node:
            left_height  = self._height(node.left)
            right_height = self._height(node.right)
            if left_height - right_height > 1:
                if self._height(node.left.left) < self._height(node.left.right):
                    self._left_rotate_avl(node.left)
                node = self._right_rotate_avl(node)
            elif right_height - left_height > 1:
                if self._height(node.right.right) < self._height(node.right.left):
                    self._right_rotate_avl(node.right)
                node = self._left_rotate_avl(node)
            node.height = max(self._height(node.left), self._height(node.right)) + 1
            node = node.p


    def _right_rotate_avl(self, node):
        left = self._right_rotate(node)
        node.height = max(self._height(node.left), self._height(node.right)) + 1
        self.graph.update_position(left)
        return left

    def _left_rotate_avl(self, node):
        right = self._left_rotate(node)
        node.height = max(self._height(node.left), self._height(node.right)) + 1
        self.graph.update_position(right)
        return right

