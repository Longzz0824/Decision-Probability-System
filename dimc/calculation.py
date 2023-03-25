import graphs
from z3 import *
from state import State


def cal(g: graphs.Graphs):
    states = g.get_states()
    init_state = g.initial_state.key
#    print(init_state)
    equation_list = []
    for i in states:
        i.update_activated_states()
        if i.get_probability_equation() is not None:
            equation_list.append(i.get_probability_equation())
    stn = g.get_states_names()
#    print(equation_list)
    for i in stn:
        equation_list.append(i+'<=1')
        equation_list.append(i+'>=0')

    state_dic = {}
    for i in stn:
        state_dic.update({i : Real(i)})
        exec(i + "= Real(i)")
    solver = Solver()
    for q in equation_list:
        solver.add(eval(q))

    set_option(precision = 8)
    if solver.check() == sat:
        result = solver.model()
    if result[state_dic[init_state]] != None:
        probability = result[state_dic[init_state]].as_fraction()
        probability_float = float(probability)
        probability = "%.2f%%" % (probability_float * 100)
#        print(result[state_dic[init_state]])
        return probability
    else:
        return Fraction(0,1)
   
def print_special_states(g1:graphs.Graphs):
    print('initial state: ',g1.initial_state_name)
    print('final state: \n',g1.final_state_name)
 

def print_result(g1:graphs.Graphs):
    result = cal(g1)
    activated_transitions, deactivated_transitions = g1.transitions_status()
    print('the probability is: ' + str(result))
    print('activated transitions: ', end='')
    print(activated_transitions)
    print('deactivated transitions: ', end='')
    print(deactivated_transitions)

