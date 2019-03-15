import networkx as nx
import math
import matplotlib.pyplot as plt

"""幂律分布&&广延指数分布"""
def hm2(ingraph):
    graph = nx.Graph(ingraph)

    sum_degree = 0
    degrees = nx.degree(graph)
    degree_distribute = nx.degree_histogram(graph)
    for degree in degrees:
        sum_degree += degree[1]

    log_k = [math.log(k) for k in range(1, len(degree_distribute))]

    p_k = []
    x_stk = 0
    for i in range(1, len(log_k)+1):
        p_k.append(1 - x_stk / sum_degree)
        x_stk += degree_distribute[i]

    log_p_k = [math.log(p) for p in p_k]
    log_minus_log_p_k = [math.log(-logpx) for logpx in log_p_k[1:]]

    plt.plot(log_k, log_p_k, color="red",linewidth=2)
    plt.title(u"幂律分布", fontproperties="SimHei")
    plt.xlabel("log(k)")
    plt.ylabel("log(P(x>=k))")
    plt.show()

    plt.plot(log_k[1:], log_minus_log_p_k, color="blue", linewidth=2)
    plt.title(u"广延指数分布", fontproperties="SimHei")
    plt.xlabel("log(k)")
    plt.ylabel("log(-(log(P(x>=k)))")
    plt.show()