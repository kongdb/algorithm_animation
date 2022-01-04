#-*- coding:utf-8 -*-

import turtle
import math

RADIUS =10 

class Point(turtle.Turtle):
    def __init__(self, x, y, color='black'):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.ht()
        self.color(color)
        self.x = x
        self.y = y

    def draw(self):
        self.penup()
        self.setposition(self.x, self.y - RADIUS)
        self.pendown()
        self.begin_fill()
        self.circle(RADIUS)
        self.end_fill()

    def reset_color(self, color='black'):
        self.clear()
        self.color(color)
        self.draw()

    def draw_partition_circle(self, radius):
        self.penup()
        self.setposition(self.x, self.y - radius)
        self.pendown()
        self.circle(radius)

    def draw_tau(self, tau, p):
        self.penup()
        self.color('black')
        self.setposition(self.x, self.y)
        self.pendown()
        self.setposition(p.x, p.y)

        self.penup()
        self.setposition((self.x + p.x) / 2, (self.y + p.y) / 2)
        self.pendown()
        self.write('dist', font=("Arial", 10, "bold"))

        self.penup()
        self.setposition(self.x, self.y - tau)
        self.pendown()
        self.circle(tau)

        self.penup()
        self.setposition(self.x, self.y)
        self.pendown()
        self.setposition(self.x, self.y - tau)

        self.penup()
        self.setposition(self.x, self.y - tau / 2)
        self.pendown()
        self.write('tau', font=("Arial", 10, "bold"))


    def dist(self, other):
        return math.sqrt((self.x - other.x) * (self.x - other.x) + (self.y - other.y) * (self.y - other.y))


class VPNode(turtle.Turtle):
    def __init__(self, index, radius, left=None, right=None):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.ht()
        self.x = 0
        self.y = 0

        self.index = index
        self.radius = radius

        self.left = left
        self.right = right

    def draw(self, color='black'):
        self.clear()
        self.penup()
        self.setposition(self.x, self.y - RADIUS)
        self.pendown()
        self.color(color)
        self.begin_fill()
        self.circle(RADIUS)
        self.end_fill()

HEIGHT = 80

def draw_partition_circle(tree, candidates):
    point = candidates[tree.index]
    point.reset_color('blue')
    point.draw_partition_circle(tree.radius)
    reset_color(tree.left, candidates, 'gray')
    reset_color(tree.right, candidates, 'orange')

def find_node(p, root):
    nodes = [root]
    while nodes:
        current = nodes.pop()
        if p.dist(Point(current.x, current.y)) <= RADIUS:
            return current
        else:
            for n in [current.left, current.right]:
                if n != None:
                    nodes.append(n)


def reset_tree_color(node):
    if node == None:
        return
    node.draw()
    reset_tree_color(node.left)
    reset_tree_color(node.right)


def reset_color(node, candidates, color):
    if node == None:
        return
    candidates[node.index].reset_color(color)
    reset_color(node.left, candidates, color)
    reset_color(node.right, candidates, color)



def find_and_reset_color(x, y, root, candidates):
    turtle.tracer(False)
    node = find_node(Point(x, y), root)
    if node == None:
        return
    reset_color(root, candidates, 'black')
    draw_partition_circle(node, candidates)
    turtle.tracer(True)



def draw_tree(root, candidates):
    def click_func(x, y):
        return find_and_reset_color(x, y, root, candidates)
    screen = turtle.getscreen()
    screen.onclick(click_func)
    root.x, root.y = 600, 300
    space = 300
    draw_tree_with_node(root, space)

def drawline(start_x, start_y, end_x, end_y):
    turtle.penup()
    turtle.setposition(start_x, start_y)
    turtle.pendown()
    turtle.setposition(end_x, end_y)

def draw_tree_with_node(node, space):
    node.draw()
    if node.left:
        node.left.x = node.x - space / 2
        node.left.y = node.y - HEIGHT
        draw_tree_with_node(node.left, space / 2)
        drawline(node.x, node.y, node.left.x, node.left.y)
    if node.right:
        node.right.x = node.x + space / 2
        node.right.y = node.y - HEIGHT
        draw_tree_with_node(node.right, space / 2)
        drawline(node.x, node.y, node.right.x, node.right.y)

