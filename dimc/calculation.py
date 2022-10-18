import graphs
from z3 import *
from state import State
import fractions

def cal(g: graphs.Graphs):
    states = g.get_states()
    init_state = g.initial_state.key
    equation_list = []
    for i in states:
        if i.get_probability_equation() is not None:
            equation_list.append(i.get_probability_equation())
    stn = g.get_states_names()
#    print(equationlist)

    state_dic = {}
    for i in stn:
        state_dic.update({i : Real(i)})
        exec(i + "= Real(i)")
    solver = Solver()
    for q in equation_list:
        solver.add(eval(q))
    if solver.check() == sat:
        result = solver.model()
    if result[state_dic[init_state]] != None:
        probability = result[state_dic[init_state]].as_fraction()
        return probability
    else:
        return Fraction(0,1)
   



def calc(g:graphs.Graphs):
    pass