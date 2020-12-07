# Author: Mark Tao
# Date: 6 March 2020
# Purpose: Plot the map

from load_graph import *
from bfs import *

dartmouth_map = load_image("dartmouth_map.png")

WIDTH = 1012
HEIGHT = 811
V_RADIUS = 6

starting_vertex = None
ending_vertex = None
clicked = False

vertex_dict = load_graph("dartmouth_graph.txt")
found = False


def draw_map():
    draw_image(dartmouth_map, 0, 0)

    # drawing all edges for each key in dictionary
    for key in vertex_dict:
        vertex_dict[key].draw_all_edges(1, 0, 0)

    for key in vertex_dict:

        # if there is both an identified starting and ending vertex, draw those circles in green/blue
        if starting_vertex is vertex_dict[key] or ending_vertex is vertex_dict[key]:
            vertex_dict[key].draw_vertex(0, 1, 0)
        else:
            vertex_dict[key].draw_vertex(1, 0, 0)


def m_press(mx, my):
    global clicked, starting_vertex

    # for each key in the dictionary, if the mouse clicks on a vertex, starting vertex becomes that vertex.
    for key in vertex_dict:
        v = vertex_dict[key]
        if v.in_vertex(mx, my, V_RADIUS):
            starting_vertex = v
            clicked = True
            break
        else:
            starting_vertex = None


def m_move(mx, my):
    global ending_vertex, found, clicked

    # if there is a starting vertex,
    if clicked:

        # for each key in the dictionary, if the mouse hovers over a vertex, ending vertex becomes that vertex.
        for key in vertex_dict:
            v = vertex_dict[key]
            if v.in_vertex(mx, my, V_RADIUS):
                ending_vertex = v
                found = True
                break
            else:
                ending_vertex = None


def breadth_first_search():
    global starting_vertex, ending_vertex

    # if there is a starting/ending vertex
    if starting_vertex is not None and ending_vertex is not None:

        # create the list that contains all backpointer references
        map_path = bfs(starting_vertex, ending_vertex)

        # for each item in the list, draw corresponding vertices/edges
        for path in range(0, len(map_path) - 1):
            map_path[path].draw_edge(0, 1, 0, map_path[path + 1])
            map_path[path].draw_vertex(0, 0, 1)


def main():
    draw_map()
    breadth_first_search()


start_graphics(main, width=WIDTH, height=HEIGHT, mouse_move=m_move, mouse_press=m_press)
