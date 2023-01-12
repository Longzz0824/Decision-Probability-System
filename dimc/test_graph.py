import graphs
import heuristic
import calculation

def g1():
    G1 = graphs.Graphs(5)
    G1.add_state('s0')
    G1.add_state('s1')
    G1.add_state('s2')
    G1.add_state('s3')
    G1.add_state('s4')
    G1.add_transition('s0->s1','0.5','can')
    G1.add_transition('s0->s2','0.5','can')
    G1.add_transition('s1->s3','0.01','cannot')
    G1.add_transition('s1->s4','0.99','can')
    G1.add_transition('s2->s4','0.98','cannot')
    G1.add_transition('s2->s3','0.02','cannot')
    G1.add_transition('s4->s4','1','cannot')
    G1.set_final_state('s3')
    G1.set_initial_state('s0')
    return G1

G1 = g1()
print(G1.adjacency_matrix, G1.ability_matrix,G1.state_index_dict)
print(G1.is_reachable('s2','s3'))
print(calculation.cal(G1))
heuristic.deactivate_all_useless_transitions(G1)
heuristic.dijkstra2(G1)
