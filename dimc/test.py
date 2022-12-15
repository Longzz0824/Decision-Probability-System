import test_graph
import calculation
import graphs
import brute_force
import input
import graph_matrix
'''#G1 = tt.g1()
G1 = input.system_input()
graphs.show_graph(G1)
s = calculation.cal(G1)
print('The Probability from initial state to final state is: ',s)
brute_force.brute_force(G1)'''


a, b = graph_matrix.random_graph(6)
G1 = graph_matrix.matrix_to_graph(a,b)
print('The initial state : ',G1.initial_state_name)
print('The final state : ',G1.final_state_name)
graphs.show_graph(G1)
print(calculation.cal(G1))
brute_force.brute_force(G1)

'''
G1 = test_graph.g1()
graphs.show_graph(G1)
matrix = graph_matrix.graph_to_matrix(G1)
print(list(G1.state_index_dict.keys()))
print(matrix)
'''