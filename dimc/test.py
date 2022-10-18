import tt
import calculation
import graphs
import brute_force
G1 = tt.g1()
graphs.show_graph(G1)
s = calculation.cal(G1)
print('The Probability from initial state to final state is: ',s)
brute_force.brute_force(G1)