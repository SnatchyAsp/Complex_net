import networkx as nx
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize



def f_1(x, A, B):
    return A*x + B

"""幂律分布&&广延指数分布"""
def hm2(ingraph):
    graph = nx.Graph(ingraph)
    sum_degree = 0
    degrees = nx.degree(graph)
    degree_distribute = nx.degree_histogram(graph)
    for degree in degrees:
        sum_degree += degree[1]

    log_k = []
    for k in range(1,len(degree_distribute)):
        log_k.append(math.log(k))

    p_k = []
    x_stk = 0
    for i in range(1, len(log_k)+1):
        p_k.append(1 - x_stk / graph.number_of_nodes())
        x_stk += degree_distribute[i]
    log_p_k = []
    for p in p_k:
        log_p_k.append(math.log(p))
    log_minus_log_p_k = []
    for logpk in log_p_k[1:]:
        log_minus_log_p_k.append(math.log(-logpk))

    for i in range(len(log_k)):
        if log_k[i] > 4:
            split_point1 = i
            break
    for i in range(len(log_k)):
        if log_k[i] > 5.4:
            split_point2 = i
            break


    A1, B1 = optimize.curve_fit(f_1, log_k[:split_point1], log_p_k[:split_point1])[0]
    A2, B2 = optimize.curve_fit(f_1, log_k[split_point1:split_point2], log_p_k[split_point1:split_point2])[0]
    A3, B3 = optimize.curve_fit(f_1, log_k[split_point2:], log_p_k[split_point2:])[0]
    _X1 = [x for x in log_k[0:split_point1]]
    _X2 = [x for x in log_k[split_point1:split_point2]]
    _X3 = [x for x in log_k[split_point2:]]
    _Y1 = [B1 + A1 * x for x in _X1]
    _Y2 = [B2 + A2 * x for x in _X2]
    _Y3 = [B3 + A3 * x for x in _X3]


    plt.plot(_X1, _Y1, "black")
    plt.plot(_X2, _Y2, "black")
    plt.plot(_X3, _Y3, "black")
    plt.plot(log_k, log_p_k,'ro', color="red")
    plt.title(u"幂律分布", fontproperties="SimHei")
    plt.xlabel("log(k)")
    plt.ylabel("log(P(x>=k))")
    plt.text(0, -7, "r1 = {}".format(abs(A1 - 1)))
    plt.text(0, -8, "r2 = {}, r3 = {}".format(abs(A2 - 1), abs(A3 - 1)))
    plt.show()

    A, B = optimize.curve_fit(f_1, log_k[1:], log_minus_log_p_k)[0]
    _X = [x for x in log_k[1:]]
    _Y = [B + A* x for x in _X]
    plt.plot(_X, _Y, "black")
    plt.plot(log_k[1:], log_minus_log_p_k, 'ro', linewidth=2)
    plt.title(u"广延指数分布", fontproperties="SimHei")
    plt.xlabel("log(k)")
    plt.ylabel("log(-(log(P(x>=k)))")
    plt.show()