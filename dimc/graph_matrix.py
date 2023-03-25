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

def random_unit(prob:float):
    assert prob >= 0 and prob <= 1
    if prob == 0:
        return False
    if prob == 1:
        return True
    prob_digits = len(str(prob).split(".")[1])
    begin = 1
    end = pow(10,prob_digits)
    R = random.randint(begin,end)
    if float(R/end) < prob:
        return True
    else:
        return False

def random_graph_generate(num: int):
    p1 = 0.1
    p2 = 0.6
    p3 = 0.3
    admx = np.zeros((num,num))
    ability_matrix = np.full((num,num),'undefined' )
    have_connection = np.full(num,False)
    #random.randint(1,100)
    for i in range(num):
        for j in range(num):
            if j <= i and random_unit(p1):                          # have transition i->j with prob p1
                admx[i][j] = np.random.randint(1,10)
                have_connection[j] = True                      
            if j > i:
                if have_connection[j] == False and random_unit(p2): # if j has not been connected, have transition i->j with prob p2
                    admx[i][j] = np.random.randint(1,10)
                    have_connection[j] = True
                if have_connection[j] == True and random_unit(p3):
                    admx[i][j] = np.random.randint(1,10)
                    have_connection[j] = True

    for i in range(num):
        sum = np.sum(admx[i])
        for j in range(num):
            if sum != 0:
                admx[i][j] /= sum
#                print(sum,a[i][j])
                if admx[i][j] != 0:
                    ability_matrix[i][j] = random_ability_set()

            else:
                break                            

    new_graph = graphs.Graphs(num)
    for i in range(num):
        new_graph.add_state('s'+str(i))
    
    new_graph.set_initial_state('s'+str(0))
    new_graph.set_final_state('s'+str(np.random.randint(1,num)))
    
    for i in range(num):
        for j in range(num):
            if admx[i][j] != 0:
                new_graph.add_transition('s'+str(i)+'->'+'s'+str(j), admx[i][j],ability_matrix[i][j])
    return new_graph

'''def random_graph(num: int):
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





