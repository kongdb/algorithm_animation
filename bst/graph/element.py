# -*- coding:utf-8 -*-

import turtle
import math
import time

from graph import const

class Element(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.ht()
        self.width(3)
        self.speed(0)

    @staticmethod
    def calc_theta_and_dist(from_x, from_y, to_x, to_y):
        theta = math.atan((to_y - from_y) / (to_x - from_x)) / math.pi * 180
        if theta < 0:
            theta += 180
        d = math.dist([from_x, from_y], [to_x, to_y])
        return theta, d



class Line(Element):
    def __init__(self):
        Element.__init__(self)
    
    def draw(self, from_x, from_y, to_x, to_y, is_dotted):
        d = math.dist([from_x, from_y], [to_x, to_y])
        self.penup()
        self.setposition(from_x, from_y)
        theta, _ = self.calc_theta_and_dist(from_x, from_y, to_x, to_y)
        # print('Theta ', theta)
        self.setheading(theta)
        self.forward(const.RADIUS)
        d -= 2 * const.RADIUS
        
        if is_dotted:
            SEG = 10
            for _ in range(int(d // (SEG * 2))):
                self.penup()
                self.forward(SEG)
                self.pendown()
                self.forward(SEG)
        else:
            self.pendown()
            self.forward(d)

        self.setheading(0)



class GraphNode(Element):
    def __init__(self):
        Element.__init__(self)
        self.tag = ''
        self.line = Line()
        self.init_position()


    def init_position(self):
        if not self.p:
            self.row = self.index = 0
        else:
            self.row = self.p.row + 1
            self.index = self.p.index * 2
            if self == self.p.left:
                pass
            elif self == self.p.right or self.value >= self.p.value:
                self.index += 1

        self.center_x, self.center_y = GraphNode.get_position(self.row, self.index)


    @staticmethod
    def get_position(row, index):
        count = pow(2, row)
        gap = const.SCREEN_WIDTH * 0.9 / count
        center_index = 0 if row == 0 else count / 2.0 - 0.5
        center_x = (index - center_index) * gap
        center_y = const.SCREEN_HEIGHT / 2 - (row + 1) * 100
        return center_x, center_y


    def draw(self, line_status=1):
        # line_status, -1: dotted, 0: not draw, 1, solid
        self.penup()
        y = self.center_y - const.RADIUS
        self.setposition(self.center_x, y)

        if hasattr(self, 'node_color'):
            self.color(getattr(self, 'node_color'))

        self.pendown()
        self.circle(const.RADIUS)
        self.setheading(0)
        value = str(self.value)
        self.penup()
        self.sety(y+3)
        self.pendown()
        self.write(value, align="center", font=("Arial", 15, "bold"))
        
        self._draw_tag()
        self._draw_height()

        self.penup()
        self.setposition(self.center_x, self.center_y)
        self.pendown()

        self.draw_line(line_status)


    def move(self, theta, dist, bring_child=False):
        self.setheading(theta)
        self.clear()
        if self.left:
            self.left.line.clear()
        if self.right:
            self.right.line.clear()
        self.penup()
        self.forward(dist)
        self.center_x, self.center_y = self.position()
        self.pendown()
        self.setheading(0)
        if bring_child:
            if self.left:
                self.left.move(theta, dist, bring_child)
                self.left.draw_line(line_status=1)
            if self.right:
                self.right.move(theta, dist, bring_child)
                self.right.draw_line(line_status=1)
        self.draw(line_status=0)



    def _draw_tag(self):
        if not self.tag:
            return
        self.penup()
        self.sety(self.center_y - 3 * const.RADIUS)
        self.pendown()
        self.write(self.tag, align="center", font=("Arial", 15))


    def _draw_height(self):
        if hasattr(self, 'height') or hasattr(self, 'bh'):
            height = getattr(self, 'height') if hasattr(self, 'height') else getattr(self, 'bh')
            self.penup()
            self.setposition(self.center_x - 1.5 * const.RADIUS, self.center_y)
            self.pendown()
            self.write(str(height), align="center", font=("Arial", 10, 'italic bold'))


    def draw_line(self, line_status):
        if not self.p or line_status == 0:
            return
        self.line.draw(self.center_x, self.center_y, self.p.center_x, self.p.center_y, line_status == -1)
        

