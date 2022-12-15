import graphs

def g1():
    G1 = graphs.Graphs(4)
    G1.add_state('x')
    G1.add_state('y')
    G1.add_state('z')
    G1.add_state('u')
    G1.add_transition('x->x','0.25','can')
    G1.add_transition('x->y','0.55','cannot')
    G1.add_transition('x->z','0.2','can')
    G1.add_transition('y->x','0.2','cannot')
    G1.add_transition('y->z','0.8','can')
    G1.add_transition('z->u','1','can')
#    G1.add_transition('u->z','1','cannot')
    G1.set_final_state('y')
    G1.set_initial_state('x')
    return G1

