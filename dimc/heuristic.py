import graphs
import state
from calculation import cal
import graph_matrix

def heuristic1(g1: graphs.Graphs):
    states = g1.get_states()
    transition_names = g1.get_transitions_names()
    for i in transition_names:
        if transition_names.count(i+'->'+i)  == 1:
            if g1.get_transition(i+'->'+i).can_be_deactivated == True:
                g1.get_transition(i+'->'+i).deactivate()
    #deactivate all the self-loop
    for i in states:
        if i.is_final_state == False:
            if i.transition_as_source_num == 0:
                sources = i.source_states
                key = i.get_id()
                for j in sources:
                    if transition_names.count(j.get_id()+'->'+key) == 1:
                        if g1.get_transition(j.get_id()+'->'+key).can_be_deactivated == True:
                            g1.get_transition(j.get_id()+'->'+key).deactivate()
    #deactivate all the transitions that don't connected to final state and the target have no ways to go out.
    g1.update()
    result = cal(g1)
    return result  


def dejkstra(g1:graphs.Graphs):
    transfer_matrix = graph_matrix.graph_to_matrix(g1)
    start = g1.state_index_dict.get(g1.initial_state_name)
    end = g1.state_index_dict.get(g1.final_state_name)
    states_num = g1.states_num
    # visited 代表哪些顶点加入过
    visited = [0] * states_num
    # 初始顶点到其余顶点的距离
    dis = {node: G[start][node] for node in range(states_num)}
    # parents 代表最终求出最短路径后，每个顶点的上一个顶点是谁，初始化为 -1，代表无上一个顶点
    parents = {node: -1 for node in range(states_num)}
    # 起始点加入进 visited 数组
    visited[start] = 1
    # 最开始的上一个顶点为初始顶点
    last_point = start

    for i in range(states_num - 1):
        # 求出 dis 中未加入 visited 数组的最短距离和顶点
        min_dis = inf
        for j in range(states_num):
            if visited[j] == 0 and dis[j] < min_dis:
                min_dis = dis[j]
                # 把该顶点做为下次遍历的上一个顶点
                last_point = j
        # 最短顶点假加入 visited 数组
        visited[last_point] = 1
        # 对首次循环做特殊处理，不然在首次循环时会没法求出该点的上一个顶点
        if i == 0:
            parents[last_point] = start + 1
        for k in range(states_num):
            if G[last_point][k] < inf and dis[k] > dis[last_point] + G[last_point][k]:
                # 如果有更短的路径，更新 dis 和 记录 parents
                dis[k] = dis[last_point] + G[last_point][k]
                parents[k] = last_point + 1

    # 因为从 0 开始，最后把顶点都加 1
    return {key + 1: values for key, values in dis.items()}, {key + 1: values for key, values in parents.items()}


def heuristic2(g1: graphs.Graphs):
    pass