import state
import transitions
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pygraphviz as pgv
import fractions
from decimal import Decimal
class Graphs():
    
    def __init__(self, num: int):
        self.state_dict = {}
        # Use dictionary to save state infomation, likes{ key: State}
        self.state_index_dict = {}
        
        self.transition_dict = {}
        # Use dictionary to save state infomation, likes{ key: Transition}
        self.states_num = num
        # Calculate the current number of states
        self.final_states = []
#        self.sorted_states_names_list = []
        self.state_counter = 0

    def add_state(self, key):
        self.state_dict.update({key: state.State(key)})    
        self.state_index_dict.update({key:self.state_counter})
        self.state_counter += 1

    def get_state(self, key ) -> state.State:                # Return Type: State
        state = self.state_dict.get(key)
        return state            
    
    def get_state_index(self, key):
        index = self.state_index_dict.get(key)
        return index

    def set_initial_state(self, s: str):
        self.initial_state = self.get_state(s)
        self.initial_state_name = s
        self.get_state(s).is_initial_state = True
    
    def set_final_state(self, s: str):
        self.final_states.append(self.get_state(s))
        self.final_state_name = s
        self.get_state(s).is_final_state = True
    
    def add_transition(self, key:str, ipr, ability):
        fraction_initial_probility = fractions.Fraction(Decimal(ipr))
        two_states = key.split('->')
        source_name = two_states[0]
        target_name = two_states[1]
        source_state, target_state = self.get_state(source_name), self.get_state(target_name)
        source_state.add_target_state(target_state, fraction_initial_probility)
        self.transition_dict.update({key: transitions.Transition(source_state, target_state, fraction_initial_probility, ability)})
        source_state.connected_transition_dict.update({self.transition_dict.get(key): fraction_initial_probility})

    def get_transition(self, key):            # Return Type: Transition
        transition = self.transition_dict.get(key)
        return transition


    def get_states_names(self):   # Get the names of all the states
        return list(self.state_dict.keys())

    def get_states(self):
        return list(self.state_dict.values())
    
    def get_transitions(self):  # Use list to save  all the transitions of graph, likes [(s1, s2, 0.5),(s2, s3, 1)]
        transList = []
        for i in self.get_states_names():
            s = self.get_state(i)
            if s.transition_as_source_num:
                transList.extend(s.get_all_transitions_tuple())
        return transList    

    def get_transitions_names(self):
        return list(self.transition_dict.keys())

    def get_transitions_dict(self):   #use it only for bet
        lst = self.get_transitions_names()
        lac = []
        lde = []
        for i in lst:
            if(self.get_transition(i).is_activated == True):
                lac.append(i)
            else:
                lde.append(i)
        dic = {'Activated Transitions' : lac, 'Deactivated Transitions' : lde}
        return dic

    def update(self):
        states = self.get_states()
        for i in states:
            i.update_activated_states()

def show_graph(graphs: Graphs):      #input nx.Graph
    G = nx.DiGraph()
    states_name = graphs.get_states_names()
    states = graphs.get_states()
    for i in states:
        i.update_activated_states()
    trans = graphs.get_transitions()
#    print(states)
#    print(trans)
    G.add_nodes_from(states_name)
    G.add_weighted_edges_from(trans)
    options = {
    "font_size": 36,
    "node_size": 3000,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 5,
    "width": 5,
    }
    posi = nx.nx_agraph.graphviz_layout(G)
    nx.draw_networkx(G, pos=posi, arrows=True, with_labels= True,**options)
#    plt.show()
    g = nx.nx_agraph.to_agraph(G)
    g.layout()
    g.draw("graph.png")
    plt.cla()
    img = plt.imread('graph.png')
    plt.imshow(img)
    plt.show()
 





    

