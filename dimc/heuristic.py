import graphs
import state
from calculation import cal
from calculation import print_result
from heapq import *
from collections import defaultdict



def deactivate_all_useless_transitions(g1: graphs.Graphs):
    end = g1.final_state_name
    state_names = g1.get_states_names()
    state_names.remove(end)
    transition_names = g1.get_transitions_names()
    for i in transition_names:
        if transition_names.count(i+'->'+i)  == 1:
            if g1.get_transition(i+'->'+i).can_be_deactivated == True:
                g1.get_transition(i+'->'+i).deactivate()
    #deactivate all the self-loops which are controllable
    for i in state_names:
        if g1.is_reachable(i,end) == False:
            current_state = g1.get_state(i)
            for j in current_state.in_transitions:
                useless_transition1 = g1.get_transition(j)
                if useless_transition1.can_be_deactivated == True:
                    g1.get_transition(j).deactivate()
            for j in current_state.out_transitions:
                useless_transition2 = g1.get_transition(j)
                if useless_transition2.can_be_deactivated == True:
                    g1.get_transition(j).deactivate()
    #deactivate all forward transitions for states that don't have a path to the final state.
    g1.update()
    print_result(g1)
#    result = cal(g1)
#    return result  


'''def dejkstra(g1:graphs.Graphs):
    start = g1.initial_state_name # the index of the initial state
    end = g1.final_state_name # the index of the final state
    adjacency_matrix = g1.adjacency_matrix  
    queue = [(-1, start)]
    visited = {start}
    not_visited = {x for x in range(g1.states_num)}
    while queue:
        prob, node = heappop(queue)
        if node == end:
            return -prob
        visited.add(node)
        if node in not_visited:
            not_visited.remove(node)
        for next in not_visited:
            heappush(queue, (prob * adjacency_matrix[node][next], next))
    return
    '''

def dijkstra2(g1:graphs.Graphs):
    start = g1.initial_state_name # the index of the initial state
    end = g1.final_state_name # the index of the final state     
    dic = defaultdict(list)
    transitions = list(g1.transition_current_probability_dict.keys())
    for i in transitions:
        two_states = i.split('->')
        source_name = two_states[0]
        target_name = two_states[1]
        dic[source_name].append((g1.transition_current_probability_dict.get(i), target_name))
    q, seen, mins = [(-1, start, [])], set(), {start: 0}
    while q:
        (probability, s1, path) = heappop(q)
        if s1 not in seen:
            seen.add(s1)
            path = [s1] + path
            if s1 == end:
                break

            for c, s2 in dic.get(s1, ()):
                if s2 in seen:
                    continue
                prev = mins.get(s2, None)
                next = float(probability) * float(c)
                if prev is None or next < prev:
                    mins[s2] = next
                    heappush(q, (next, s2, path))
    path.reverse()
    print(path)
    must_be_activated_trans = []
    for i in range(len(path) - 1):
        must_be_activated_trans.append(path[i] + '->' + path[i + 1])
    for i in list(g1.transition_dict.keys()):
        if i not in must_be_activated_trans:
            g1.transition_dict.get(i).deactivate()
    
    g1.update()
    print_result(g1)





