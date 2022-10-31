import graphs
import calculation

def system_input():
    
    print("Let's start inputting a probabilishe system!")
    num = input('Please input the number of states:')
    num = int(num)
    G1 = graphs.Graphs(num)
    
    key = input('Please input the name of all the states: ').split()
    for i in key:
        G1.add_state(i)

    a = input("Please select one of the states as the initial state, input it's name: ").strip()
    G1.set_initial_state(a)
    b = input("Please select some of the states as the final state, input it's name: ").split()
    for i in b:
        G1.set_final_state(i)
    print("Then let's start inputting the transitions!")
    '''    state_list = G1.get_states_names()
    for j in state_list:
        nbr = input("Please input the neibor of state " + str(j)+ ': ').split()
        for m in nbr: 
            G1.add_transition(j, m)
    ''' 
    while(True):   
            transitions_list = input("Please input a transition, it's initial probability and can be deactivated or not just like a->b 0.5 yes, b->c 0.2 no. if all the transitions have been input, please input 'completed'  ")
            if transitions_list.strip() == 'completed':
                break
            else:
                each_transition_list = transitions_list.split(',')   # ['a->b 0.5 yes' , 'b->c 0.2 no']
                for i in each_transition_list:
                    this_transition = i.split()
                    G1.add_transition(this_transition[0], this_transition[1], this_transition[2])
                    
        
    return G1
