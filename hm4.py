import networkx as nx
import matplotlib.pyplot as plt

"""K-shell"""


def hm4(ingraph):
    graph = nx.Graph(ingraph)
    degree = 1
    color_map = [0 for x in range(0, graph.number_of_nodes())]
    k_shell_list = []
    while(True):
        temp_list = []
        while(True):
            remove_list = []
            cnt = graph.number_of_nodes()
            #for i in range(1:degree+1):
            for node in graph.nodes:

                if(graph.degree(node)<=degree):
                    remove_list.append(node)

            graph.remove_nodes_from(remove_list)
                #temp_list.append(remove_list)
            if remove_list:
                temp_list += remove_list
            if not remove_list:
                k_shell_list.append(temp_list)
                break

        if graph.number_of_nodes() == 0:
            break
        degree += 1

    for i in range(0, len(k_shell_list)):
        for node in k_shell_list[i]:
            color_map[int(node)] = i*3
    nx.draw_spring(ingraph,  node_color=color_map, node_size=10, edge_color="white")

    plt.show()






