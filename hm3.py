import networkx as nx
import matplotlib.pyplot as plt
import math
from scipy import optimize
"""等级性"""

def f_1(x, A, B):
    return A*x + B

def hm3(ingraph):
    graph = nx.Graph(ingraph)
    degree_distribute = nx.degree_histogram(graph)
    max_num = 0;
    degrees = nx.degree(graph)
    clusters = nx.clustering(graph)

    ck = []
    k = []
    for i in range(0, len(degree_distribute)):
        total_cluster = 0.0
        cnt = 0
        for j in range(0, graph.number_of_nodes()):
            if degrees[str(j)] == i:
                total_cluster += clusters[str(j)]
                cnt += 1

        if cnt == 0:
            continue
        ck.append(total_cluster / cnt)
        k.append(i)

    log_x = []
    log_y = []
    for i in range(1, len(k)):
        log_x.append(math.log(k[i]))
        log_y.append(math.log(ck[i]))
    A, B = optimize.curve_fit(f_1, log_x, log_y)[0]
    _X = [x for x in log_x]
    _Y = [B + A * x for x in _X]
    plt.plot(_X, _Y, "black")
    plt.plot(log_x, log_y, 'ro')
    plt.xlabel("log(k)")
    plt.ylabel("log(C(k))")
    plt.title(u"等级性", fontproperties="SimHei")
    plt.show()
