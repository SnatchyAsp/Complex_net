import networkx as nx
import matplotlib.pyplot as plt
import random



def get_nodes_by_degree(ingraph, num):
    graph = ingraph
    nodes_degree = list(graph.degree())
    nodes_degree.sort(key=lambda x: x[1], reverse=True)
    return [node for node, _ in nodes_degree[:num]]


def get_nodes_by_random(ingraph, num):
    graph = nx.Graph(ingraph)
    res = []
    graph_nodes = list(graph.nodes())
    while len(res) < num:
        i = int(random.random() * len(graph_nodes))
        node = graph_nodes[i]
        if node in res:
            continue
        res.append(node)
    return res



def get_nodes_by_kshell(num, k_shell_list):

    return [node for node in k_shell_list[len(k_shell_list)-1][20:num+20]]


def one_iter(ingraph, node_state, beta, gamma):
    graph = nx.Graph(ingraph)
    new_node_state = {k: v for k, v in node_state.items()}

    for k, v in node_state.items():
        if v == 1:
            for nei in list(nx.all_neighbors(graph, k)):
                if node_state[str(nei)] == 0:
                    if random.random() <= beta:
                        new_node_state[str(nei)] = 1

            if random.random() <= gamma:
                new_node_state[k] = 2

    return new_node_state


def show_state(node_state):
    s, i, r = 0, 0, 0
    for k, v in node_state.items():
        if v == 0:
            k += 1
        elif v == 1:
            i += 1
        else:
            r += 1
    print(s, i, r)
    return (s, i, r)


def get_ir_sum(node_state):
    res = 0
    for _, v in node_state.items():
        if v:
            res += 1
    return res / len(node_state)


def hm6(ingraph, num, beta, gamma, time_step, k_shell_list):

    list1=[0]*time_step
    list2=[0]*time_step
    list3=[0]*time_step
    for cnt in range(100):
        graph = nx.Graph(ingraph)
        node_state = {str(i): 0 for i in graph.nodes()}
        origin1 = get_nodes_by_degree(graph, num)
        ir_sum_list1 = []
        for node in origin1:
            node_state[node] = 1
        for i in range(time_step):
            ir_sum = get_ir_sum(node_state)
            ir_sum_list1.append(ir_sum)
            a = one_iter(graph, node_state, beta, gamma)
            node_state = a
            # show_state(node_state)

        node_state = {str(i): 0 for i in graph.nodes()}
        origin2 = get_nodes_by_kshell(graph, num, k_shell_list)
        ir_sum_list2 = []
        for node in origin2:
            node_state[node] = 1
        for i in range(time_step):
            ir_sum = get_ir_sum(node_state)
            ir_sum_list2.append(ir_sum)
            node_state = one_iter(graph, node_state, beta, gamma)

        node_state = {str(i): 0 for i in graph.nodes()}
        origin3 = get_nodes_by_random(graph, num)
        ir_sum_list3 = []
        for node in origin3:
            node_state[node] = 1
        for i in range(time_step):
            ir_sum = get_ir_sum(node_state)
            ir_sum_list3.append(ir_sum)
            node_state = one_iter(graph, node_state, beta, gamma)
        list1=[list1[i]+ ir_sum_list1[i] for i in range(0,time_step)]
        list2=[list2[i]+ ir_sum_list2[i] for i in range(0,time_step)]
        list3=[list3[i]+ ir_sum_list3[i] for i in range(0,time_step)]

    x = list(range(time_step))

    plt.plot(x, [list1[i]/100 for i in range(time_step)], 'red')
    plt.plot(x, [list2[i]/100 for i in range(time_step)], 'green')
    plt.plot(x, [list3[i]/100 for i in range(time_step)], 'blue')
    plt.legend((u'degree', u'k-shell', u'random'), loc='best')
    plt.xlabel("time steps")
    plt.ylabel("proportion of infected nodes")
    plt.title(u"SIR", fontproperties="SimHei")
    plt.show()


