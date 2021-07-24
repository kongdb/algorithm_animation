# -*- coding:utf-8 -*-

from graph.tree import BinaryTreeGraph
from algorithm.node import TreeNode

class BinarySearchTree:

    def __init__(self):
        self.graph = BinaryTreeGraph()
        self.root  = None

    def clear(self):
        self.graph.clear(self.root)
        self.root = None


    def search(self, value):
        node = self._search_node(value)
        if node:
            print(f'Find node with {value} success')
        else:
            print(f'Find node with {value} fail')
        self.graph.reset_style(self.root)

    def find_min(self):
        node = self._min_node(self.root)
        self.graph.reset_style(self.root)
        return node.value


    def find_max(self):
        node = self._max_node(self.root)
        self.graph.reset_style(self.root)
        return node.value

    def predecessor(self, value):
        node = self._search_node(value)
        pre = None
        if node:
            if node.left:
                pre = self._max_node(node.left)
            else:
                # my style
                while node:
                    if node.p and node == node.p.right:
                        pre = node.p
                        break
                    else:
                        node = node.p
        self.graph.predecessor(pre)
        self.graph.reset_style(self.root)
        return pre


    def successor(self, value):
        node = self._search_node(value)
        suc = None
        if node:
            if node.right:
                suc = self._min_node(node.right)
            else:
                # style in the book
                parent = node.p
                while parent and node == parent.right:
                    node = parent
                    parent = parent.p
                suc = parent
        self.graph.successor(suc)
        self.graph.reset_style(self.root)
        return suc


    def insert(self, value):
        self._insert_node(value)
        self.graph.reset_style(self.root)


    def delete(self, value):
        self._delete_node(value)
        self.graph.reset_style(self.root)


    def _insert_node(self, value):
        if not self.root:
            self.root = self._create_node(value, None)
            return None
        else:
            parent = None
            current = self.root
            while current:
                parent = current
                self.graph.insert_tree_node(current, value)
                if value < current.value:
                    current = current.left
                else:
                    current = current.right
            if value < parent.value:
                parent.left = self._create_node(value, parent)
            else:
                parent.right = self._create_node(value, parent)
            return parent


    def _delete_node(self, value):
        current = self._search_node(value)
        balance_node = None
        if not current:
            print('Can not find node with value', value)
        else:
            if not current.left:
                self._translate(current, current.right, True)
                balance_node = current.right if current.right else current.p
            elif not current.right:
                self._translate(current, current.left, True)
                balance_node = current.left if current.left else current.p
            else:
                right_min = self._min_node(current.right)
                right_min_equal_to_right = True
                balance_node = right_min
                if right_min != current.right:
                    balance_node = right_min.right if right_min.right else right_min.p
                    self._translate(right_min, right_min.right, True, True)
                    right_min.right = current.right
                    right_min.right.p = right_min

                    right_min_equal_to_right = False

                self._translate(current, right_min, right_min_equal_to_right)
                right_min.left = current.left
                right_min.left.p = right_min
        return current, balance_node


    def _translate(self, u, v, bring_child, move_u_beside=False):
        if not move_u_beside:
            self.graph.delete_tree_node(u)
        if u == self.root: # style in the book, u.p == None
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if v != None:
            v.p = u.p
        dest_x, dest_y = u.center_x, u.center_y
        if move_u_beside:
            self.graph.move_to(u, dest_x + 50, dest_y, False)
        self.graph.move_to(v, dest_x, dest_y, bring_child)
        self.graph.update_position(v)


    def _create_node(self, value, parent):
        node = TreeNode(value, p = parent)
        node.draw(line_status=-1)
        return node


    def _search_node(self, value):
        current = self.root
        while current:
            self.graph.search_tree_node(current, value)
            if current.value == value:
                break
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return current


    def _min_node(self, current):
        assert current, 'Root should not be empty'
        self.graph.find_min(current)
        while current.left:
            current = current.left
            self.graph.find_min(current)
        return current

    def _max_node(self, current):
        assert current, 'Root should not be empty'
        self.graph.find_max(current)
        while current.right:
            current = current.right
            self.graph.find_max(current)
        return current


    def _right_rotate(self, node):
        print(f'Right rotate {node.value}')
        left = node.left
        self.graph.right_rotate(left, node)

        if node == self.root:
            self.root = left
        elif node == node.p.left:
            node.p.left = left
        else:
            node.p.right = left
        left.p = node.p

        node.left = left.right
        if node.left != None:
            node.left.p = node

        left.right = node
        left.right.p = left

        return left

    def _left_rotate(self, node):
        print(f'Left rotate {node.value}')
        right = node.right
        self.graph.left_rotate(right, node)

        if node == self.root:
            self.root = right
        elif node == node.p.left:
            node.p.left = right
        else:
            node.p.right = right
        right.p = node.p

        node.right = right.left
        if node.right != None:
            node.right.p = node

        right.left = node
        right.left.p = right

        return right
