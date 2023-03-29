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
    b = input("Please select one of the states as the final state, input it's name: ").split()
    for i in b:
        G1.set_final_state(i)
    print("Then let's start inputting the transitions!")

    while(True):   
            transitions_list = input("Please input a transition, it's initial probability and whether it is controllable or not, just like a->b 0.5 can, b->c 0.2 cannot. if all the transitions have been input, please input 'completed'  ")
            if transitions_list.strip() == 'completed':
                break
            else:
                each_transition_list = transitions_list.split(',')   # ['a->b 0.5 can' , 'b->c 0.2 cannot']
                for i in each_transition_list:
                    this_transition = i.split()
                    G1.add_transition(this_transition[0], this_transition[1], this_transition[2])
                    
        
    return G1

def manual_input(num:int, initial_state:str, final_state:str, transitions:str): 
    num = int(num)
    G1 = graphs.Graphs(num)
    for i in range(num):
        G1.add_state('s'+str(i))
    G1.set_initial_state(initial_state)
    G1.set_final_state(final_state)
    each_transition_list = transitions.split(',')   # ['a->b 0.5 can' , 'b->c 0.2 cannot']
    for i in each_transition_list:
        this_transition = i.split()
        G1.add_transition(this_transition[0], this_transition[1], this_transition[2])   
    return G1