import numpy as np
from math import sqrt as sqrt
import graphs
import random
import transitions

def random_ability_set():
    if random.randint(0,1) == 1:
        return 'can'
    else:
        return 'cannot'

def random_graph(num: int):
    b = np.random.randint(-10,9,(num, num))
    graph_matrix = np.maximum(b,0)
    graph_matrix = graph_matrix.astype(np.float64)
    ability_matrix = np.full((num,num),'undefined' )
#    print(a)
    for i in range(num):
        sum = np.sum(graph_matrix[i])
        for j in range(num):
            if sum != 0:
                graph_matrix[i][j] /= sum
#                print(sum,a[i][j])
                if graph_matrix[i][j] == 1/sum or graph_matrix[i][j] == 2/sum or graph_matrix[i][j] == 3/sum:
                    #print(a[i])
                    graph_matrix[i] = np.zeros(num)
                    graph_matrix[i][j] = 1
                    ability_matrix[i][j] = random_ability_set()
                    break
                elif graph_matrix[i][j] != 0:
                    ability_matrix[i][j] = random_ability_set()

            else:
                #a[i][i] = 1
                break
    print(graph_matrix)
    print(ability_matrix)
    return graph_matrix, ability_matrix

'''
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
    return matrix_list '''

def matrix_to_graph(matrix_a:np.ndarray, matrix_b: np.ndarray):
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



