# Author: Mark Tao
# Date: 4 March 2020
# Purpose: Build a vertex class
from cs1lib import *


class Vertex:
    # initializing variables
    def __init__(self, name, x, y):
        self.name = name
        self.x = int(x)
        self.y = int(y)
        self.adj = []

    # method to draw individual vertex
    def draw_vertex(self, r, g, b):
        set_fill_color(r, g, b)
        draw_circle(self.x, self.y, 7)

    # method to draw an individual edge
    def draw_edge(self, r, g, b, vertex_obj):
        enable_stroke()
        set_stroke_color(r, g, b)
        set_stroke_width(2)
        draw_line(self.x, self.y, vertex_obj.x, vertex_obj.y)

    # method looping through and connecting each vertex
    def draw_all_edges(self, r, g, b):
        for vertex in self.adj:
            self.draw_edge(r, g, b, vertex)

    # checking to see if mouse is within range of vertex
    def in_vertex(self, mx, my, radius):
        if (abs(self.x - mx) <= radius) and (abs(self.y - my) <= radius):
            return True
