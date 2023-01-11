import graphs
import state
from calculation import cal
import graph_matrix
import heapq

def heuristic1(g1: graphs.Graphs):
    states = g1.get_states()
    transition_names = g1.get_transitions_names()
    for i in transition_names:
        if transition_names.count(i+'->'+i)  == 1:
            if g1.get_transition(i+'->'+i).can_be_deactivated == True:
                g1.get_transition(i+'->'+i).deactivate()
    #deactivate all the self-loops which are controllable
    for i in states:
        if i.is_final_state == False:
            if i.transition_as_source_num == 0 or i.transition_as_source_num == 1 and i.get_id == list(i.target_states.keys())[0]:
                sources = i.source_states
                key = i.get_id()
                for j in sources:
                    if transition_names.count(j.get_id()+'->'+key) == 1:
                        if g1.get_transition(j.get_id()+'->'+key).can_be_deactivated == True:
                            g1.get_transition(j.get_id()+'->'+key).deactivate()
    #deactivate all the transitions that don't connected to final state and the target have no ways to go out.
    g1.update()
    result = cal(g1)
    return result  


def dejkstra(g1:graphs.Graphs):
    start = g1.state_index_dict.get(g1.initial_state_name) # the index of the initial state
    end = g1.state_index_dict.get(g1.final_state_name) # the index of the final state
    adjacency_matrix = g1.adjacency_matrix  
    queue = [(-1, start)]
    visited = {start}
    not_visited = {x for x in range(g1.states_num)}
    while queue:
        prob, node = heapq.heappop(queue)
        print(node)
        if node == end:
            return -prob
        visited.add(node)
        if node in not_visited:
            not_visited.remove(node)
        for next in not_visited:
            heapq.heappush(queue, (prob * adjacency_matrix[node][next], next))
    



def heuristic2(g1: graphs.Graphs):
    start = g1.initial_state
    end = g1.final_state
    path = []
    0.  , c 