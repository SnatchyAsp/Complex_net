
import networkx as nx
import csv

"""basic info"""


def hm1():
    csv_file = csv.reader(open('3-facebook_combined.csv', 'r'))
    graph = nx.Graph()
    for line in csv_file:
        graph.add_edge(*tuple(line))
    print(nx.info(graph))
    print("Average_clustering:  " + str(nx.average_clustering(graph)))
    print("Average_path_length:   "+str(nx.average_shortest_path_length(graph)))
    return graph
