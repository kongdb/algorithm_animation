#-*- coding:utf-8 -*-

import random
import time
import turtle
import graph

from utils import edit_distance


class BKNode(turtle.Turtle):
    def __init__(self, d):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.ht()
        self.width(3)
        self.x = 0
        self.y = 0
        self.data = d
        self.children = []
    

class BKTree:
    def __init__(self, candidates):
        self.root = None
        self._build_tree(candidates)

    def search(self, target, radius):
        result = []
        self._search(self.root, target, radius, result)
        return result

    def _build_tree(self, candidates):
        #random.shuffle(candidates)
        self.root = BKNode(candidates[0])
        for i in range(1, len(candidates)):
            self._insert(self.root, candidates[i])

    def _insert(self, node, candidate):
        distance = edit_distance(node.data, candidate)
        if len(node.children) <= distance:
            node.children.extend([None] * (distance + 1 - len(node.children)))
        if node.children[distance] == None:
            node.children[distance] = BKNode(candidate)
        else:
            self._insert(node.children[distance], candidate)

    def _search(self, node, target, radius, result):
        if not node:
            return
        distance = edit_distance(node.data, target)
        if distance <= radius:
            result.append((node.data, distance))
            node.color('red')
        else:
            node.color('green')
        graph.draw_node(node)
        for i in range(max(1, distance - radius), min(len(node.children), (distance + radius) + 1)):
            self._search(node.children[i], target, radius, result);


def brute_force(candidates, target, radius):
    result = []
    for candidate in candidates:
        distance = edit_distance(target, candidate)
        if distance <= radius:
            result.append((candidate, distance))
    return result


if __name__ == '__main__':
    turtle.tracer(False)
    #names = [name.strip() for name in open('1.txt').readlines()]
    names = [name.strip() for name in open('../../../data/DoctorNames.txt').readlines()]
    radius = 1
    t1 = time.time()
    tree = BKTree(names)
    t2 = time.time()
    print('BKTree construct cost time:', (t2 - t1) * 1000, 'ms')
    graph.draw_tree(tree.root, 0, 300, 0)
    turtle.tracer(True)
    while True:
        target = input('Please input name..\n')
        graph.reset_color(tree.root)
        t3 = time.time()
        res1 = brute_force(names, target, radius)
        t4 = time.time()
        res2 = tree.search(target, radius)
        t5 = time.time()
        #print('Brute force result:', res1, ' cost time:', (t4 - t3) * 1000, 'ms')
        #print('BKTree      result:', res2, ' cost time:', (t5 - t4) * 1000, 'ms')

