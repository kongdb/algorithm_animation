# -*- coding:utf-8 -*-

import random

from algorithm.bst import BinarySearchTree
from algorithm.avl import AvlTree
from algorithm.rb  import RBTree


supported_trees = [BinarySearchTree, AvlTree, RBTree]

def main():
    tree_type = input('Choose tree type:\n[0]: BST\n[1]: AVL\n[2]: RB\n')
    tree = supported_trees[int(tree_type)]()
    print('- A val (Add node with val)\n- D val (Delete Node with val)\n'
          '- N [count] (Add count nodes with random value)')
    while True:
        method = input().strip().split(' ')
        if not method:
            continue
        method_type = method[0]
        method_value = 0 if len(method) == 1 else int(method[1])
        if method_type == 'A':
            tree.insert(method_value)
        elif method_type == 'N':
            values = []
            for i in range(method_value):
                v = random.randint(0, 99)
                tree.insert(v)
                values.append(v)
            print('Insert values ', values)
        elif method_type == 'B':
            break
        elif method_type == 'C':
            tree.clear()
        elif method_type == 'D':
            tree.delete(method_value)
        elif method_type == 'S':
            tree.search(method_value)
        elif method_type == 'MIN':
            print('Found min:', tree.find_min())
        elif method_type == 'MAX':
            print('Found max:', tree.find_max())
        elif method_type == 'PRE':
            pre = tree.predecessor(method_value)
            if pre:
                print('Found predecessor:', pre.value)
            else:
                print('Can not find predecessor')
        elif method_type == 'SUC':
            suc = tree.successor(method_value)
            if suc:
                print('Found successor:', suc.value)
            else:
                print('Can not find successor')
        else:
            print(f'Unsupported method {method_type}')


if __name__ == '__main__':
    main()