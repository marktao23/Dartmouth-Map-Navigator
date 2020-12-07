# Author: Mark Tao
# Date: 6 March 2020
# Purpose: Load the graph

from vertex import Vertex


def load_graph(file_name):
    vertex_dictionary = {}
    in_file = open(file_name, "r")

    # first pass
    for j in in_file:
        # removing whitespace from name
        names = j.split(";")[0].strip()

        # removing commas from the coordinates
        coordinates = j.split(";")[2].split(",")

        # removing whitespace
        x_coordinate = coordinates[0].strip()
        y_coordinate = coordinates[1].strip()

        v = Vertex(names, x_coordinate, y_coordinate)

        # adding to the dictionary
        vertex_dictionary[v.name] = v

    in_file.close()
    in_file_2 = open(file_name, "r")

    # second pass
    for i in in_file_2:
        # removing the commas (was not done earlier)
        adj_list = i.split(";")[1].split(",")

        # reassigning names
        names = i.split(";")[0].strip()

        # creating vertex objects
        v = vertex_dictionary[names]

        # appending objects into adj_list
        for k in adj_list:
            v.adj.append(vertex_dictionary[k.strip()])

    in_file_2.close()

    return vertex_dictionary


load_graph("dartmouth_graph.txt")
