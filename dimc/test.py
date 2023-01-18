import calculation
import graph_matrix
import graphs
g1 = graph_matrix.random_graph_generate(6)

print(g1.ability_matrix)
print(g1.adjacency_matrix)
graphs.show_graph(g1)
calculation.print_result(g1)