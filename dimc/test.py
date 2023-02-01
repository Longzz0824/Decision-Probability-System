import calculation
import graph_matrix
import graphs
import heuristic
import brute_force
g1 = graph_matrix.random_graph_generate(8)

#print(g1.ability_matrix)
#print(g1.adjacency_matrix)
graphs.show_graph(g1)
calculation.print_result(g1)
heuristic.deactivate_all_useless_transitions(g1)
heuristic.dijkstra2(g1)
brute_force.brute_force(g1)