import calculation
import graph_matrix
import graphs
import heuristic
import brute_force
g1 = graph_matrix.random_graph_generate(8)

#print(g1.ability_matrix)
#print(g1.adjacency_matrix)

calculation.print_special_states(g1)
print('the probability if all the transitions are activated: ')
calculation.print_result(g1)
print('\nthe result of deactivate all useless transitions :')
heuristic.deactivate_all_useless_transitions(g1)
print('\nthe result of dijkstra :')
heuristic.dijkstra(g1)
print(brute_force.brute_force(g1))