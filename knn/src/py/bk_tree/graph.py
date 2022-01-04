#-*- coding:utf-8 -*-

import turtle
import math

text = turtle.Turtle()
text.ht()

RADIUS = 5

def draw_node(node):
    node.clear()
    node.penup()
    node.setposition(node.x, node.y)
    node.pendown()
    node.begin_fill()
    node.circle(RADIUS);
    node.end_fill()


def draw_tree_with_node(node):
    draw_node(node)
    print(node.data)
    start = 0
    for i in range(start, len(node.children)):
        if not node.children[i]:
            continue
        turtle.penup()
        turtle.setposition(node.x, node.y + RADIUS)
        turtle.pendown()
        next_x, next_y = node.children[i].x, node.children[i].y
        turtle.setposition(next_x, next_y + RADIUS)
        draw_tree_with_node(node.children[i])


def reset_color_with_node(node):
    if node.pencolor() != 'black':
        node.color('black')
        draw_node(node)
    for child in node.children:
        if child:
            reset_color_with_node(child)

def reset_color(tree):
    turtle.tracer(False)
    reset_color_with_node(tree)
    turtle.tracer(True)


def draw_tree(tree, x, y, depth):
    turtle.ht()
    screen = turtle.getscreen()
    turtle.setup(1400, 800)
    screen.screensize(1400, 800)

    turtle.speed(0)
    tree.x = x
    tree.y = y
    node_dist = 20
    level_width = 0
    current_row = [tree]
    all_nodes = [tree]
    while current_row:
        next_row = []
        depth += 1
        for node in current_row:
            for child in node.children:
                if child:
                    next_row.append(child)
        level_width = max(level_width + 50, (len(next_row) - 1) * node_dist)
        next_x = x - level_width / 2
        gap = level_width / max(1, len(next_row))
        y -= 120
        for child in next_row:
            child.x, child.y = next_x, y
            next_x += gap
            all_nodes.append(child)
        current_row = next_row

    def draw_text(x, y):
        turtle.tracer(False)
        text.clear()
        text.penup()
        text.setposition(-30, 350)
        text.pendown()
        t = ''
        for node in all_nodes:
            d = math.sqrt((x - node.x) * (x - node.x) + (y - node.y - RADIUS) * (y - node.y - RADIUS))
            if d <= RADIUS:
                t = node.data
                break
        print('Draw text', t)
        text.write(t, font=("Arial", 15, "bold"))
        turtle.tracer(True)
    screen.onclick(draw_text)


    draw_tree_with_node(tree)



