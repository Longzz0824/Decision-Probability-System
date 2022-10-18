import graphs
import calculation

def system_input():
    
    print("Let's start inputting a probabilishe system!")
    num = input('Please input the number of states:')
    num = int(num)
    G1 = graphs.Graphs(num)
    for i in range(num):
        key = input('Please input the name of state ' + str(i)+': ')
        G1.add_state(key)
    a = input("Please select one of the states as the initial state, input it's name: ")
    G1.set_initial_state(a)
    b = input("Please select some of the states as the final state, input it's name: ").split()
    for i in b:
        G1.set_final_state(i)
    print("Then let's start inputting the transitions!")
    state_list = G1.get_states_names()
    for j in state_list:
        nbr = input("Please input the neibor of state " + str(j)+ ': ').split()
        for m in nbr: 
            G1.add_transition(j, m)
    
    return G1

