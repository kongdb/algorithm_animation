# -*- coding:utf-8 -*-

import time
import turtle
import math

from graph import const
from graph.element import GraphNode

PAUSE = 1
ANIMATION_STEPS = 20

class BinaryTreeGraph:

    def __init__(self):
        turtle.ht()
        screen = turtle.getscreen()
        turtle.setup(const.SCREEN_WIDTH, const.SCREEN_HEIGHT)
        screen.screensize(const.SCREEN_WIDTH, const.SCREEN_HEIGHT)
        print(f'Screen size {screen.screensize()}')
        


    def search_tree_node(self, node, value):
        node.clear()
        node.color('gray')
        if node.value == value:
            node.tag = f'{value} =, matched'
            node.color('green')
        elif value < node.value:
            node.tag = f'{value} <, move left'
        else:
            node.tag = f'{value} >, move right'
        
        node.draw()
        
        time.sleep(PAUSE)


    def insert_tree_node(self, node, value):
        node.clear()
        node.color('gray')
        if value < node.value:
            if node.left:
                node.tag = f'{value} <, move left'
            else:
                node.tag = f'Insert {value} as left child'
        else:
            if node.right:
                node.tag = f'{value} >, move right'
            else:
                node.tag = f'Insert {value} as right child'
        
        node.draw()
        
        time.sleep(PAUSE)


    def predecessor(self, node):
        if not node:
            return
        node.clear()
        node.color('green')
        node.tag = 'Predecessor'
        node.draw()
        time.sleep(PAUSE)


    def successor(self, node):
        if not node:
            return
        node.clear()
        node.color('green')
        node.tag = 'Successor'
        node.draw()
        time.sleep(PAUSE)


    def reset_style(self, node):
        if not node:
            return
        time.sleep(PAUSE)
        turtle.tracer(False)
        nodes = [node]
        while nodes:
            n = nodes.pop(0)
            if hasattr(node, 'node_color'):
                n.color(getattr(node, 'node_color'))
            else:
                n.color('black')
            n.tag = ''
            n.clear()
            n.draw()
            if n.left:
                nodes.append(n.left)
            if n.right:
                nodes.append(n.right)
        turtle.tracer(True)
        time.sleep(PAUSE)


    def move_to(self, node, dest_x, dest_y, bring_child):
        if not node:
            return
        turtle.tracer(False)

        src_x, src_y = node.center_x, node.center_y
        theta, d = GraphNode.calc_theta_and_dist(src_x, src_y, dest_x, dest_y)
        if not bring_child:
            node.line.clear()

        for i in range(ANIMATION_STEPS):
            node.move(theta, d / ANIMATION_STEPS, bring_child)
            turtle.update()
            time.sleep(0.1)

        turtle.tracer(True)



    def update_position(self, node):
        if not node:
            return
        turtle.tracer(False)
        nodes = [node]
        while nodes:
            n = nodes.pop(0)
            n.init_position()
            n.clear()
            n.line.clear()
            n.draw()
            if n.left:
                nodes.append(n.left)
            if n.right:
                nodes.append(n.right)
        turtle.tracer(True)


    def find_min(self, node):
        node.clear()
        node.color('gray')
        if node.left:
            node.tag = 'move left'
        else:
            node.color('green')
            node.tag = f'found min'
        
        node.draw()
        
        time.sleep(PAUSE)


    def find_max(self, node):
        node.clear()
        node.color('gray')
        if node.right:
            node.tag = 'move right'
        else:
            node.color('green')
            node.tag = f'found max'
        
        node.draw()
        
        time.sleep(PAUSE)


    def delete_tree_node(self, node):
        turtle.tracer(False)
        if node.left:
            node.left.line.clear()
        if node.right:
            node.right.line.clear()
        node.clear()
        node.line.clear()
        node.color('gray')
        node.tag = 'To be deleted'
        node.draw(line_status=-1)

        turtle.tracer(True)

        time.sleep(PAUSE*2)

        node.clear()
        node.line.clear()

    
    def right_rotate(self, left, current):
        '''
               A                 B
             /   \             /   \
            B     C           D     A
           / \               /     / \
          D   E         =>  F     E   C
         /
        F
        '''

        left_x, left_y = left.center_x, left.center_y
        left_left_x, left_left_y = GraphNode.get_position(left.row + 1, 2 * left.index)
        left_right_x, left_right_y = GraphNode.get_position(left.row + 1, 2 * left.index + 1)
        current_x, current_y = current.center_x, current.center_y
        right_row, right_index = current.row + 1, 2 * current.index + 1
        right_x, right_y = GraphNode.get_position(right_row, right_index)
        right_left_x, right_left_y = GraphNode.get_position(right_row + 1, 2 * right_index)
        right_right_x, right_right_y = GraphNode.get_position(right_row + 1, 2 * right_index + 1)

        # move left to current
        theta1, d1 = GraphNode.calc_theta_and_dist(left_x, left_y, current_x, current_y)
        # move left.left to left
        theta2, d2 = GraphNode.calc_theta_and_dist(left_left_x, left_left_y, left_x, left_y)
        # move left.right to right.left
        theta3, d3 = GraphNode.calc_theta_and_dist(left_right_x, left_right_y, right_left_x, right_left_y)
        theta3 = 0 # horizontal right
        # move current to right
        theta4, d4 = GraphNode.calc_theta_and_dist(current_x, current_y, right_x, right_y)
        theta4 += 180 # down
        # move right to right.right
        theta5, d5 = GraphNode.calc_theta_and_dist(right_x, right_y, right_right_x, right_right_y)
        theta5 += 180 # down

        turtle.tracer(False)
        for i in range(ANIMATION_STEPS):
            left.move(theta1, d1 / ANIMATION_STEPS)
            if left.left:
                left.left.move(theta2, d2 / ANIMATION_STEPS, bring_child=True)
            if left.right:
                left.right.move(theta3, d3 / ANIMATION_STEPS, bring_child=True)
            current.move(theta4, d4 / ANIMATION_STEPS)
            if current.right:
                current.right.move(theta5, d5 / ANIMATION_STEPS, bring_child=True)
            turtle.update()
            time.sleep(0.1)
        turtle.tracer(True)


    def left_rotate(self, right, current):
        '''
             C                  A
           /   \              /   \
          A     E            B     C
         / \     \    <=          / \
        B   D     F              D   E
                                      \
                                       F

        '''

        right_x, right_y = right.center_x, right.center_y
        right_left_x, right_left_y = GraphNode.get_position(right.row + 1, 2 * right.index)
        right_right_x, right_right_y = GraphNode.get_position(right.row + 1, 2 * right.index + 1)
        current_x, current_y = current.center_x, current.center_y
        left_row, left_index = current.row + 1, 2 * current.index
        left_x, left_y = GraphNode.get_position(left_row, left_index)
        left_left_x, left_left_y = GraphNode.get_position(left_row + 1, 2 * left_index)
        left_right_x, left_right_y = GraphNode.get_position(left_row + 1, 2 * left_index + 1)

        # move right to current
        theta1, d1 = GraphNode.calc_theta_and_dist(right_x, right_y, current_x, current_y)
        # move right.right to right
        theta2, d2 = GraphNode.calc_theta_and_dist(right_right_x, right_right_y, right_x, right_y)
        # move right.left to left.right
        theta3, d3 = GraphNode.calc_theta_and_dist(right_left_x, right_left_y, left_right_x, left_right_y)
        theta3 = 180 # horizontal left
        # move current to left
        theta4, d4 = GraphNode.calc_theta_and_dist(current_x, current_y, left_x, left_y)
        theta4 += 180 # down
        # move left to left.left
        theta5, d5 = GraphNode.calc_theta_and_dist(left_x, left_y, left_left_x, left_left_y)
        theta5 += 180 # down

        turtle.tracer(False)
        for i in range(ANIMATION_STEPS):
            right.move(theta1, d1 / ANIMATION_STEPS)
            if right.right:
                right.right.move(theta2, d2 / ANIMATION_STEPS, bring_child=True)
            if right.left:
                right.left.move(theta3, d3 / ANIMATION_STEPS, bring_child=True)
            current.move(theta4, d4 / ANIMATION_STEPS)
            if current.left:
                current.left.move(theta5, d5 / ANIMATION_STEPS, bring_child=True)
            turtle.update()
            time.sleep(0.1)
        turtle.tracer(True)


    def update_node(self, node):
        node.clear()
        node.draw(line_status=0)
        time.sleep(PAUSE)


    def clear(self, node):
        if not node:
            return
        node.clear()
        node.line.clear()
        self.clear(node.left)
        self.clear(node.right)
        

    def loop(self):
        turtle.done()

