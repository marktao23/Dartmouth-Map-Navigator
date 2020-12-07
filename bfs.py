# Author: Mark Tao
# Date: 6 March 2020
# Purpose: BFS

from collections import deque
from vertex import *


def bfs(starting_vertex, ending_vertex):
    # building the deque
    queue = deque()
    queue.append(starting_vertex)

    # building the dictionary
    back_pointers_dict = {}
    back_pointers_dict[starting_vertex] = None

    # if queue is not none, popleft (take the left-most term)
    while len(queue) != 0:
        v = queue.popleft()

        for key in v.adj:

            # if the key is not already in dictionary, append it to the queue and gave it its corresponding vertex
            if key not in back_pointers_dict:

                back_pointers_dict[key] = v
                queue.append(key)

    vertex_tracker = ending_vertex

    map_path = []

    # if there is an associated value with the new ending vertex's key, append it to an empty list
    while back_pointers_dict[vertex_tracker]:
        map_path.append(vertex_tracker)
        vertex_tracker = back_pointers_dict[vertex_tracker]

    # appending starting vertices, return the empty list
    map_path.append(starting_vertex)
    return map_path
