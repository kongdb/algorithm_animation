#-*- coding:utf-8 -*-

import random
from time import sleep

from graph import Point, VPNode, draw_tree, reset_tree_color, reset_color, draw_partition_circle
import turtle

MAX = 1 << 31

class VPTree:
    class Cmp:
        def __init__(self, candidates, center):
            self.center = center
            self.candidates = candidates
        def __call__(self, i, j):
            center = self.candidates[self.center]
            return center.dist(self.candidates[i]) <= center.dist(self.candidates[j])

    # candidate and target need dist API
    def __init__(self, candidates):
        self.candidates = candidates
        self.root = self._build_tree(0, len(candidates))
        self.tau = MAX
        self.result = None

    def search(self, target, radius):
        self.tau = radius
        self.result = None

        turtle.tracer(False)
        reset_tree_color(self.root)
        turtle.tracer(True)
        self._search(self.root, target)
        
        return (self.result, self.tau)

    def _search(self, node, target):
        if node == None:
            return

        turtle.tracer(False)
        node.draw(color='green')
        target.reset_color('red')
        reset_color(self.root, self.candidates, 'black')
        draw_partition_circle(node, self.candidates)
        target.draw_tau(self.tau, self.candidates[node.index])
        turtle.tracer(True)
        input('next step..')
        
        dist = target.dist(self.candidates[node.index])
        if dist <= self.tau:
            self.tau = dist
            self.result = node
        if dist <= node.radius:
            self._search(node.left, target)
            if dist + self.tau >= node.radius:
                self._search(node.right, target)
        else:
            self._search(node.right, target)
            if dist - self.tau <= node.radius:
                self._search(node.left, target)


    def _build_tree(self, first, last):
        if last <= first:
            return None
        elif last - first == 1:
            return VPNode(first, MAX);
        rand_index = random.randint(first, last - 1)
        self._swap(first, rand_index)
        mid = (first + last) // 2
        self._nth_element(first + 1, mid, last, VPTree.Cmp(self.candidates, first))
        return VPNode(first, self.candidates[first].dist(self.candidates[mid]),
                      self._build_tree(first + 1, mid + 1), self._build_tree(mid + 1, last))
    
    def _nth_element(self, first, nth, last, compare):
        if last - first <= 1:
            return
        le_last = first
        for i in range(first + 1, last):
            if compare(i, first):
                le_last += 1
                self._swap(le_last, i)
        self._swap(first, le_last)
        if le_last > nth:
            self._nth_element(first, nth, le_last, compare)
        elif le_last < nth:
            self._nth_element(le_last + 1, nth, last, compare)


    def _swap(self, i, j):
        t = self.candidates[i]
        self.candidates[i] = self.candidates[j]
        self.candidates[j] = t




def main():
    turtle.tracer(False)
    turtle.ht()
    points = []
    left, right, top, bottom = -800, 100, 300, -300
    for i in range(15):
        x = random.randint(left, right)
        y = random.randint(bottom, top)
        p = Point(x, y)
        points.append(p)
        p.draw()

    tree = VPTree(points)
    draw_tree(tree.root, points)

    turtle.tracer(True)


    while True:
        input('Enter to generate random point..')
        x = random.randint(left, right)
        y = random.randint(bottom, top)
        target = Point(x, y, color='red')
        target.draw()
        result, dist = tree.search(target, 200)
        if result != None:
            result.draw(color='orange')
            points[result.index].reset_color('orange')
        target.reset_color('red')
        input('Enter to continue..')
        target.clear()

        


if __name__ == '__main__':
    main()
