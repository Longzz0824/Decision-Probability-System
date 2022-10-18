import graphs

def g1():
    G1 = graphs.Graphs(4)
    G1.add_state('x')
    G1.add_state('y')
    G1.add_state('z')
    G1.add_state('u')
    G1.add_transition('x','x')
    G1.add_transition('x','y')
    G1.add_transition('x','z')
    G1.add_transition('z','u')
    G1.add_transition('u','z')
    G1.set_final_state('y')
    G1.set_initial_state('x')
    return G1