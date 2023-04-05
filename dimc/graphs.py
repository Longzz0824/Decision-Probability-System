import state
import transitions
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import pygraphviz as pgv
import fractions
from decimal import Decimal


class Graphs():
    
    def __init__(self, num: int):
        self.state_dict = {}
        # Use dictionary to save state information, likes{ key: State}
        self.state_index_dict = {}
        # Use dictionary to save state index pairs, likes { s0: 0, s1: 1}  s0 is string.
        self.transition_dict = {}
        # Use dictionary to save state infomation, likes{ key: Transition}
        
        self.transition_init_probability_dict = {}   # likes {'a->b': 0.3}
        self.transition_current_probability_dict = {}
        self.states_num = num
        # Calculate the current number of states
        self.state_counter = 0
        self.adjacency_matrix = np.zeros((num, num), dtype=np.float64)
        self.controllability_matrix = np.full((num,num),'undefined' )

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
        self.final_state = self.get_state(s)
        self.final_state_name = s
        self.get_state(s).is_final_state = True
    
    def add_transition(self, key:str, ipr, ability):
        fraction_initial_probability = fractions.Fraction(Decimal(ipr))
        two_states = key.split('->')
        source_name = two_states[0]
        target_name = two_states[1]
        
        self.adjacency_matrix[self.get_state_index(source_name), self.get_state_index(target_name)] = ipr
        self.controllability_matrix[self.get_state_index(source_name), self.get_state_index(target_name)] = ability
        source_state, target_state = self.get_state(source_name), self.get_state(target_name)

        source_state.transition_num_count()
        source_state.out_transitions.append(key)
        source_state.out_states.append(target_name)
        target_state.in_transitions.append(key)
        self.transition_dict.update({key: transitions.Transition(source_state, target_state, ability)})
        self.transition_init_probability_dict.update({key: ipr})
        self.transition_current_probability_dict.update({key: ipr})
        source_state.all_connected_transition_dict.update({self.transition_dict.get(key): fraction_initial_probability})
        source_state.current_transitions_as_source.update({key: fraction_initial_probability})

    def get_transition(self, key)->transitions.Transition:            # Return Type: Transition
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

    def get_transition_tuples(self):
        controllable_translist = []
        uncontrollable_translist = []
        for i in self.get_transitions_names():
            tup =[]
            s = self.get_transition(i)
            if s.controllable:
                tup.append(s.source.get_id())
                tup.append(s.target.get_id())
                tup.append(self.transition_init_probability_dict.get(i))
                controllable_translist.append(tuple(tup))
            else:
                tup.append(s.source.get_id())
                tup.append(s.target.get_id())
                tup.append(self.transition_init_probability_dict.get(i))
                uncontrollable_translist.append(tuple(tup))
        return controllable_translist,uncontrollable_translist  

    def get_transitions_names(self):
        return list(self.transition_dict.keys())

    def get_transitions_status(self):   #use it only for looks better
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
    
    def get_deactivated_transitions(self):
        lst = self.transition_dict.values()
        lde = []
        for i in lst:
            if i.is_deactivated == True:
                lde.append(i.key)
        return lde

    def update(self):
        states = self.get_states()
        for i in states:
            i.update_activated_states()
            self.transition_current_probability_dict.update(i.current_transitions_as_source)
#            self.ipradjacency_matrix[self.get_state_index(source_name), self.get_state_index(target_name)] = 

    def is_reachable(self, start: str, target: str): #Find if there is a path from state 'start' to state 'target'
        s = self.state_index_dict.get(start)
        d = self.state_index_dict.get(target)
        visited =[False]*(self.states_num)
        queue = []
        queue.append(s)
        visited[s] = True
        while(queue):
            n = queue.pop(0)
            if n == d:
                return True
            for i in range(self.states_num):
                if visited[i] == False and self.adjacency_matrix[n][i] != 0:
                    queue.append(i)
                    visited[i] = True
        return False
    
    def activate_all_the_transitions(self):
        trans_name = self.get_transitions_names()
        for i in trans_name:
            transition = self.transition_dict.get(i)
            transition.activate()
        self.update()

    def get_activated_transitions(self):
        activated_trans = set()
        for i in list(self.transition_dict.keys()):
            if self.transition_dict.get(i).is_activated:
                activated_trans.add(i)
        return list(activated_trans)

    def get_controllable_transitions(self):
        controllable_trans = set()
        for i in list(self.transition_dict.keys()):
            if self.transition_dict.get(i).controllable:
                controllable_trans.add(i)
        return list(controllable_trans)

    def get_activated_controllable_transitions(self):
        activated_controllable_transitions = set()
        for i in list(self.transition_dict.keys()):
            if self.transition_dict.get(i).controllable and self.transition_dict.get(i).is_activated:
                activated_controllable_transitions.add(i)
        return list(activated_controllable_transitions)        

    def transitions_status(self):
        activated_trans = set()
        deactivated_trans = set()
        for i in list(self.transition_dict.keys()):
            if self.transition_dict.get(i).is_activated:
                activated_trans.add(i)
            else:
                deactivated_trans.add(i)
        return activated_trans, deactivated_trans


def show_graph(graphs: Graphs):      #input nx.Graph
    G = nx.DiGraph()
    states_name = graphs.get_states_names()
    ctrans,utrans = graphs.get_transition_tuples()
#    print(states)
#    print(trans)
    G.add_nodes_from(states_name)

    for u, v, p in ctrans:
        G.add_edge(u, v, weight=p, color='lightblue', controllable=True)
    
    for u, v, p in utrans:
        G.add_edge(u, v, weight=p, color='black', controllable=False)

    edge_labels = {(u, v): str(d['weight']) for u, v, d in G.edges(data=True)}
    posi = nx.nx_agraph.graphviz_layout(G)
    nx.draw_networkx_nodes(G,posi,node_size=3000,node_color='white',linewidths=5)
    nx.draw_networkx_edges(G, posi,edgelist=ctrans,edge_color='lightblue',width=5)
    nx.draw_networkx_edges(G, posi,edgelist=utrans,edge_color='black',width=5)
    nx.draw_networkx_labels(G, posi, font_size=36, font_family='Arial')
    nx.draw_networkx_edge_labels(G, posi, edge_labels=edge_labels, font_size=20, font_family='Arial')

#    plt.show()
    g = nx.nx_agraph.to_agraph(G)
    g.layout()
    g.draw("graph.png")
'''    plt.cla()
    img = plt.imread('graph.png')
    plt.imshow(img)
    plt.show()'''
 
     




    

