# -*- coding:utf-8 -*-

from algorithm.bst import BinarySearchTree
from algorithm.node import RBNode

class RBTree(BinarySearchTree):
    def __init__(self):
        BinarySearchTree.__init__(self)
        self.NIL = RBNode(0, is_nil=True, color='black')
        self.NIL.is_nil = True
        self.root = self.NIL


    def insert(self, value):
        if self.root == self.NIL:
            z = self.root = self._create_node(value, self.NIL)
        else:
            current = self.root
            parent = self.NIL
            while current != self.NIL:
                parent = current
                self.graph.insert_tree_node(current, value)
                if value < current.value:
                    current = current.left
                else:
                    current = current.right
            if value < parent.value:
                z = parent.left  = self._create_node(value, parent)
            else:
                z = parent.right = self._create_node(value, parent)
        self._rb_insert_fixup(z)
        self.graph.reset_style(self.root)


    def _rb_insert_fixup(self, z):
        while z.p.node_color == 'red':
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y.node_color == 'red':
                    '''
                            z.p.p(B)                z'.p.p(R)  <- new z
                           /       \                /      \
                         z.p(R)    y(R)  =>       z'.p(B)   y(B)
                        /                         /
                      z(R)                      z'(R)
                    '''
                    self.update_color(z.p, 'black')
                    self.update_color(y, 'black')
                    self.adjust_bh(z.p.p, 1)
                    self.update_color(z.p.p, 'red')
                    z = z.p.p
                else:
                    if z == z.p.right:
                        '''
                                  z.p.p(B)                             z'.p.p(B)
                                 /       \                            /       \
                              z.p(R)     y(B)      =>              z'(R)      y(B)
                                   \                               / 
                                   z(R)                         z'.p(R)   <- new z
                        '''
                        self._left_rotate_rb(z.p)
                        z = z.left
                    '''     
                               z.p.p(B)                       z'.p(B)
                             /        \                      /      \
                           z.p(R)     y(B)         =>      z'(R)    z'.p.p(R)
                           /                                           \
                         z(R)                                           y(B)
                    '''
                    self.update_color(z.p, 'black')
                    self.update_color(z.p.p, 'red')
                    self._right_rotate_rb(z.p.p)

            else:
                y = z.p.p.left
                if y.node_color == 'red':
                    '''
                         z.p.p(B)                 z'.p.p(R)      <- new z
                        /      \                 /       \
                      y(R)    z.p(R)      =>    y(B)     z'.p(B)
                                 \                          \
                                 z(R)                       z'(R)
                    '''
                    self.update_color(z.p, 'black')
                    self.update_color(y, 'black')
                    self.adjust_bh(z.p.p, 1)
                    self.update_color(z.p.p, 'red')
                    z = z.p.p
                else:
                    if z == z.p.left:
                        '''
                             z.p.p(B)                  z.p.p(B)
                            /       \                  /     \
                         y(B)       z.p(R)     =>     y(B)    z'(R)
                                   /                            \
                                 z(R)                           z'.p(R)
                        '''
                        z = z.p
                        self._right_rotate_rb(z)
                    '''
                              z.p.p(B)                    z'.p(B)
                              /      \                    /    \
                            y(B)     z.p(R)    =>   z'.p.p(R)  z'(R)
                                       \                /
                                       z(R)           y(B)
                    '''
                    self.update_color(z.p, 'black')
                    self.update_color(z.p.p, 'red')
                    self._left_rotate_rb(z.p.p)

        self.update_color(self.root, 'black')

    def update_color(self, node, color):
        if not node:
            return
        node.node_color = color
        self.graph.update_node(node)

    def adjust_bh(self, node, count):
        if not node:
            return
        node.bh += 1


    def delete(self, value):
        z = self._search_node(value)
        if not z:
            print('Can not find node with value:', value)
        else:
            y = z
            y_original_color = y.node_color
            if z.left == self.NIL:
                x = z.right
                self._translate(z, x, True)
            elif z.right == self.NIL:
                x = z.left
                self._translate(z, x, True)
            else:
                y = self._min_node(z.right)
                y_original_color = y.node_color
                x = y.right
                right_min_equal_to_right = True
                if y.p == z:
                    '''
                           z                 y
                         /   \             /  \
                        a     y       =>  a    x   
                               \
                                x 
                    '''
                    x.p = y
                else:
                    '''
                            z                 z
                          /   \             /   \
                         a     b           a     b
                              /  \    =>        /  \
                             y    c            x   c
                              \
                               x
                    '''
                    self._translate(y, x, True, True)
                    y.right = z.right
                    y.right.p = y
                    right_min_equal_to_right = False

                self._translate(z, y, right_min_equal_to_right)
                y.left = z.left
                y.left.p = y
                self.adjust_bh(y, z.bh - y.bh)
                self.update_color(y, z.node_color)

            if y_original_color == 'black':
                self._rb_delete_fixup(x)

        self.graph.reset_style(self.root)


    def _right_rotate_rb(self, node):
        left = self._right_rotate(node)
        node.bh = node.left.bh + (1 if node.left.node_color == 'black' else 0)
        self.graph.update_position(left)
        return left

    def _left_rotate_rb(self, node):
        right = self._left_rotate(node)
        node.bh = node.left.bh + (1 if node.left.node_color == 'black' else 0)
        self.graph.update_position(right)
        return right


    def _rb_delete_fixup(self, x):
        while x != self.root and x.node_color == 'black':
            if x == x.p.left:
                w = x.p.right
                if w.node_color == 'red':
                    '''
                              x.p(1B)                                  w'(1B)
                           /          \                           /            \
                          x(2B)       w(R)                     x.p(R)          w'.r(1B)   
                         /    \    /       \                  /       \         /   \
                       a(3) b(3)  w.l(1B) w.r(1B)     =>    x(2B)  w'.l(1B)   e(2)  f(2)
                                 /    \    /   \           /   \    /    \
                                c(2) d(2) e(2) f(2)       a(3) b(3) c(2) d(2)
                    '''
                    self.update_color(w, 'black')
                    self.update_color(x.p, 'red')
                    self._left_rotate_rb(x.p)
                    w = x.p.right
                if w.left.node_color == 'black' and w.right.node_color == 'black':
                    '''
                                     x.p(c1)                                        x'.p(1+c1) <- new x
                              /                 \                                 /          \
                           x(2B)                w(B)                           x'(B)           w(R)
                          /     \         /              \                   /    \         /           \
                    a(2+c1) b(2+c1)   w.l(B)           w.r(B)         =>  a(2+c1) b(2+c1) w.l(B)        w.r(B)
                                    /      \           /       \                         /    \        /       \
                                c(2+c1) d(2+c1)    e(2+c1) f(2+c1)                    c(2+c1) d(2+c1) e(2+c1) f(2+c1)
                    '''
                    self.update_color(w, 'red')
                    x = x.p
                    self.adjust_bh(x, -1)
                    self.graph.update_node(x)
                else:
                    if w.right.node_color == 'black':
                        '''
                                    x.p(c1)                                           x.p(c1)
                                 /             \                                  /               \
                            x(2B)               w(B)                            x(2B)            w'.l(B)     <- new w
                           /    \           /         \                        /    \          /         \
                         a(2+c1) b(2+c1)  w.l(R)        w.r(B)        =>    a(2+c1) b(2+c1)   c(1+c1)   w'(R)
                                        /     \       /       \                                        /    \
                                      c(1+c1) d(1+c1) e(2+c1) f(2+c1)                               d(1+c1) w'.r(B)
                                                                                                           /     \
                                                                                                         e(2+c1) f(2+c1)
                        '''
                        self.update_color(w.left, 'black')
                        self.update_color(w, 'red')
                        self._right_rotate_rb(w)
                        w = x.p.right
                    '''
                                    x.p(c1)                                                        w'(c1) 
                               /                \                                        /                        \
                          x(2B)                 w(B)                                 x'.p(B)                    w'.r(B)
                         /    \            /             \               =>          /         \                /     \
                      a(2+c1) b(2+c1)    w.l(c2)          w.r(R)                   x'(B)       w.l(c2)       e(1+c1) f(1+c1)
                                        /      \          /      \                /   \        /         \
                                   c(1+c1+c2) d(1+c1+c2) e(1+c1) f(1+c1)      a(2+c1) b(2+c1) c(1+c1+c2) d(1+c1+c2)
                    '''
                    self.adjust_bh(x.p, -1)
                    self.update_color(x.p, 'black')
                    self.update_color(w.right, 'black')
                    self.adjust_bh(w, 1)
                    self.update_color(w, x.p.node_color)
                    self._left_rotate_rb(x.p)
                    x = self.root
            else:
                w = x.p.left
                if w.node_color == 'red':
                    '''
                                 x.p(1B)                                    w'(1B)
                              /             \                              /       \
                            w(R)             x(2B)                     w'.l(1B)     x.p(R)
                         /        \         /    \                    /     \     /        \
                       w.l(1B)  w.r(1B)    e(3)  f(3)        =>    a(2)    b(2) w.r(1B)    x(2B)
                       /    \    /   \                                         /     \     /   \
                     a(2) b(2) c(2) d(2)                                      c(2)   d(2) e(3) f(3)
                    '''
                    self.update_color(w, 'black')
                    self.update_color(x.p, 'red')
                    self._right_rotate_rb(x.p)
                    w = w.p.left
                if w.left.node_color == 'black' and w.right.node_color == 'black':
                    '''
                                     x.p(c1)                                            x'.p(1+c1)  <- new x
                                /                   \                             /                \
                             w(B)                    x(2B)                      w(R)                 x'(B)
                        /              \            /      \                   /         \           /     \
                       w.l(B)           w.r(B)     e(2+c1) f(2+c1)     =>    w.l(B)      w.r(B)    e(2+c1) f(2+c1)
                       /      \         /       \                          /    \       /      \
                    a(2+c1) b(2+c1)  c(2+c1) d(2+c1)                   a(2+c1) b(2+c1) c(2+c1) d(2+c1)
                    '''
                    self.update_color(w, 'red')
                    x = x.p
                    self.adjust_bh(x, -1)
                    self.graph.update_node(x)
                else:
                    if w.left.node_color == 'black':
                        '''
                                        x.p(c1)                                           x.p(c1)
                                    /               \                                   /           \
                                  w(B)                 x(2B)                         w'.r(B)         x(2B)
                                /         \          /      \                       /     \         /     \
                            w.l(B)        w.r(R)   e(2+c1) f(2+c1)   =>           w'(R)   d(1+c1)  e(2+c1) f(2+c1)
                            /     \       /       \                               /     \
                        a(2+c1) b(2+c1) c(1+c1) d(1+c1)                         w'.l(B) c(1+c1)
                                                                                /    \ 
                                                                            a(2+c1) b(2+c1)                         
                                                                                                         
                        '''
                        self.update_color(w.right, 'black')
                        self.update_color(w, 'red')
                        self._left_rotate_rb(w)
                        w = x.p.left
                    '''
                                               x.p(c1)                                      w'(c1) 
                                           /                 \                           /             \
                                       w(B)                   x(2B)                  w'.l(B)          x'.p(B)
                                 /             \             /     \                 /     \         /          \
                              w.l(R)          w.r(c2)      e(2+c1)  f(2+c1)      a(1+c1)  b(1+c1) w.r(c2)       x'(B)
                            /      \          /      \                                           /     \        /    \
                      a(1+c1) b(1+c1) c(1+c1+c2) d(1+c1+c2)                            c(1+c1+c2) d(1+c1+c2) e(2+c1) f(2+c1)
                    '''
                    self.adjust_bh(x.p, -1)
                    self.update_color(x.p, 'black')
                    self.update_color(w.left, 'black')
                    self.adjust_bh(w, 1)
                    self.update_color(w, x.p.node_color)
                    self._right_rotate_rb(x.p)
                    x = self.root


        self.update_color(x, 'black')

    def _create_node(self, value, parent):
        node = RBNode(value, p = parent)
        node.left = node.right = self.NIL
        node.draw(line_status=-1)
        return node