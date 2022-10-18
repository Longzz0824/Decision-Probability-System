import state
import transitions
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pygraphviz as pgv

class Graphs():
    
    def __init__(self, num: int):
        self.state_list = {}
        # Use dictionary to save state infomation, likes{ key: State}
        self.transition_list = {}
        # Use dictionary to save state infomation, likes{ key: Transition}
        self.states_num = num
        # Calculate the current number of states
        self.final_states = []

    def add_state(self, key):
        self.state_list.update({key: state.State(key)})
    
    def get_state(self, key):                # Return Type: State
        state = self.state_list.get(key)
        return state            
    
    def set_initial_state(self, s: str):
        self.initial_state = self.get_state(s)
        self.get_state(s).is_initial_state = True
    
    def set_final_state(self, s: str):
        self.final_states.append(self.get_state(s))
        self.get_state(s).is_final_state = True
    
    def add_transition(self, f, t):
        f1, t1 = self.get_state(f), self.get_state(t)
        f1.add_target_state(t1)
        self.transition_list.update({f+'->'+t: transitions.Transition(f1, t1)})

    def get_transition(self, key):            # Return Type: Transition
        transition = self.transition_list.get(key)
        return transition


    def get_states_names(self):   # Get the names of all the states
        return list(self.state_list.keys())

    def get_states(self):
        return list(self.state_list.values())
    
    def get_transitions(self):  # Use list to save  all the transitions of graph, likes [(s1, s2, 0.5),(s2, s3, 1)]
        transList = []
        for i in self.get_states_names():
            s = self.get_state(i)
            if s.transition_num:
                transList.extend(s.get_out_transitions())
        return transList    

    def get_transitions_names(self):
        return list(self.transition_list.keys())

    def get_transitions_dict(self):
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


def show_graph(graphs: Graphs):      #input nx.Graph
    G = nx.DiGraph()
    states = graphs.get_states_names()
    trans = graphs.get_transitions()
#    print(states)
#    print(trans)
    G.add_nodes_from(states)
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
    plt.show()
    g = nx.nx_agraph.to_agraph(G)
    g.layout()
    g.draw("graph.png")





    

