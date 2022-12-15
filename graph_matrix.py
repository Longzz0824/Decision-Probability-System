import numpy as np
from math import sqrt as sqrt
import graphs
import random
import transitions

def random_graph_matrix(num: int):
    b = np.random.randint(-10,8,(num,num))
    a = np.maximum(b,0)
    a = a.astype(np.float64)
#    print(a)
    for i in range(num):
        sum = np.sum(a[i])
        for j in range(num):
            if sum != 0:
                a[i][j] /= sum
#                print(sum,a[i][j])
                if a[i][j] == 5/sum or a[i][j] == 6/sum or a[i][j] == 7/sum:
                    #print(a[i])
                    a[i] = np.zeros(num)
                    a[i][j] = 1
                    break
            else:
                #a[i][i] = 1
                break
    print(a)
    return(a)


def random_ability_matrix(num: int):
    matrix_np = np.random.randint(-7,2,(num,num))
    matrix_list = matrix_np.tolist()
    for i in range(num):
        for j in range(num):
            if matrix_list[i][j] == 1:
                matrix_list[i][j] = 'can'
            elif matrix_list[i][j] <= 0:
                matrix_list[i][j] = 'cannot'
    print(matrix_list)
    return matrix_list

def matrix_to_graph(matrix_a:np.ndarray, matrix_b: list):
    num = int(sqrt(matrix_a.size))
    new_graph = graphs.Graphs(num)
    for i in range(num):
        new_graph.add_state('s'+str(i))
    
    rand_2_states=random.sample(range(0, num), 2)
    new_graph.set_initial_state('s'+str(rand_2_states[0]))
    new_graph.set_final_state('s'+str(rand_2_states[1]))
    
    for i in range(num):
        for j in range(num):
            if matrix_a[i][j] != 0:
                new_graph.add_transition('s'+str(i)+'->'+'s'+str(j), matrix_a[i][j],matrix_b[i][j])

    return new_graph

def graph_to_matrix(graph: graphs.Graphs):
    states_name_list = graph.get_states_names()
    graph.state_index_dict
    graph_matrix = np.zeros((graph.states_num,graph.states_num))
    for i in states_name_list:
        state = graph.get_state(i)
        source_index = graph.get_state_index(i)
        connected_transtions_list = list(state.connected_transition_dict.keys())
        if len(connected_transtions_list) != 0:
            for j in connected_transtions_list:
                target = j.target.get_id()
                prob = j.current_probability 
                target_index = graph.get_state_index(target)
                graph_matrix[source_index][target_index] = prob
        else:
            pass
    return graph_matrix



