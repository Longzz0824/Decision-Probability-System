import graphs
import brute_force
from calculation import cal
from calculation import result_GUI
from heapq import *
from collections import defaultdict
from queue import Queue


def deactivate_all_useless_transitions(g1: graphs.Graphs):
    g1.activate_all_the_transitions()
    end = g1.final_state_name
    state_names = g1.get_states_names()
    state_names.remove(end)
    transition_names = g1.get_controllable_transitions()
    for i in transition_names:
        if transition_names.count(i+'->'+i)  == 1:
            g1.get_transition(i+'->'+i).deactivate()
    #deactivate all the self-loops which are controllable
    for i in state_names:
        if g1.is_reachable(i,end) == False:
            current_state = g1.get_state(i)
            for j in current_state.in_transitions:
                g1.get_transition(j).deactivate()
            
            for j in current_state.out_transitions:
                g1.get_transition(j).deactivate()

    #deactivate all forward transitions for states that don't have a path to the final state.
    g1.update()
    return result_GUI(g1)
#    result = cal(g1)
#    return result  


def deactivate_all_useless_transitions_probability(g1: graphs.Graphs):
    g1.activate_all_the_transitions()
    end = g1.final_state_name
    state_names = g1.get_states_names()
    state_names.remove(end)
    transition_names = g1.get_controllable_transitions()
    for i in transition_names:
        if transition_names.count(i+'->'+i)  == 1:
            g1.get_transition(i+'->'+i).deactivate()
    #deactivate all the self-loops which are controllable
    for i in state_names:
        if g1.is_reachable(i,end) == False:
            current_state = g1.get_state(i)
            for j in current_state.in_transitions:
                g1.get_transition(j).deactivate()
            
            for j in current_state.out_transitions:
                g1.get_transition(j).deactivate()
                
    #deactivate all forward transitions for states that don't have a path to the final state.
    g1.update()
    return cal(g1)



def brute_force_after_daut(g1:graphs.Graphs):
    g1.activate_all_the_transitions()
    end = g1.final_state_name
    state_names = g1.get_states_names()
    state_names.remove(end)
    transition_names = g1.get_controllable_transitions()
    for i in transition_names:
        if transition_names.count(i+'->'+i)  == 1:
            g1.get_transition(i+'->'+i).deactivate()
    #deactivate all the self-loops which are controllable
    for i in state_names:
        if g1.is_reachable(i,end) == False:
            current_state = g1.get_state(i)
            for j in current_state.in_transitions:
                g1.get_transition(j).deactivate()
            
            for j in current_state.out_transitions:
                g1.get_transition(j).deactivate()
                
    #deactivate all forward transitions for states that don't have a path to the final state.
    g1.update()
    return brute_force.brute_force_part(g1)



def brute_force_after_daut_evaluation(g1:graphs.Graphs):
    g1.activate_all_the_transitions()
    end = g1.final_state_name
    state_names = g1.get_states_names()
    state_names.remove(end)
    transition_names = g1.get_controllable_transitions()
    for i in transition_names:
        if transition_names.count(i+'->'+i)  == 1:
            g1.get_transition(i+'->'+i).deactivate()
    #deactivate all the self-loops which are controllable
    for i in state_names:
        if g1.is_reachable(i,end) == False:
            current_state = g1.get_state(i)
            for j in current_state.in_transitions:
                g1.get_transition(j).deactivate()
            
            for j in current_state.out_transitions:
                g1.get_transition(j).deactivate()
                
    #deactivate all forward transitions for states that don't have a path to the final state.
    g1.update()
    return brute_force.brute_force_part_probability(g1)


def dijkstra(g1:graphs.Graphs):
    g1.activate_all_the_transitions()
    start = g1.initial_state_name # the index of the initial state
    end = g1.final_state_name # the index of the final state     
    dic = defaultdict(list)
    path_dic = defaultdict(list)
    transitions = list(g1.transition_current_probability_dict.keys())
    for i in transitions:
        two_states = i.split('->')
        source_name = two_states[0]
        target_name = two_states[1]
        dic[source_name].append((g1.transition_current_probability_dict.get(i), target_name))
        
 #   print(dic)
    q, seen, mins = [(-1, start, [])], set(), {start: 0}
    count = 1
    while q:
#        print('queue: ',q)
        (probability, sleft, path) = heappop(q)
        if sleft not in seen:
            seen.add(sleft)
            path = [sleft] + path
            path_dic.update({sleft:path})
#            if s1 == end:
#                break
#            print('current:',sleft)
#            print('path: ',path)
            for c, sright in dic.get(sleft, ()):
                print(sright,count)
                count+=1
                if sright in seen:
                    continue
                prev = mins.get(sright, None)
                next = float(probability) * float(c)
                print(prev,next)
                if prev is None or next < prev:
                    mins[sright] = next
                    heappush(q, (next, sright, path))
                    print(path)
    path_dic[end].reverse()
#    print(path_dic)
#    print('path1111:',path_dic[end])
    must_be_activated_trans = []
    for i in range(len(path_dic[end]) - 1):
        must_be_activated_trans.append(path_dic[end][i] + '->' + path_dic[end][i + 1])
#    print(must_be_activated_trans)
    for i in list(g1.transition_dict.keys()):
        if i not in must_be_activated_trans:
            g1.transition_dict.get(i).deactivate()
    
    g1.update()
    return result_GUI(g1)

def dijkstra_probability(g1:graphs.Graphs):
    g1.activate_all_the_transitions()
    start = g1.initial_state_name # the index of the initial state
    end = g1.final_state_name # the index of the final state     
    dic = defaultdict(list)
    path_dic = defaultdict(list)
    transitions = list(g1.transition_current_probability_dict.keys())
    for i in transitions:
        two_states = i.split('->')
        source_name = two_states[0]
        target_name = two_states[1]
        dic[source_name].append((g1.transition_current_probability_dict.get(i), target_name))
        
#    print(dic)
    q, seen, mins = [(-1, start, [])], set(), {start: 0}
    count = 1
    while q:
#        print('queue: ',q)
        (probability, sleft, path) = heappop(q)
        if sleft not in seen:
            seen.add(sleft)
            path = [sleft] + path
            path_dic.update({sleft:path})
#            if s1 == end:
#                break
#            print('current:',sleft)
#            print('path: ',path)
            for c, sright in dic.get(sleft, ()):
#                print(sright,count)
                count+=1
                if sright in seen:
                    continue
                prev = mins.get(sright, None)
                next = float(probability) * float(c)
#print(prev,next)
                if prev is None or next < prev:
                    mins[sright] = next
                    heappush(q, (next, sright, path))
                    print(path)
    path_dic[end].reverse()
#    print('path1111:',path_dic[end])
    must_be_activated_trans = []
    for i in range(len(path_dic[end]) - 1):
        must_be_activated_trans.append(path_dic[end][i] + '->' + path_dic[end][i + 1])
#print(must_be_activated_trans)
    for i in list(g1.transition_dict.keys()):
        if i not in must_be_activated_trans:
            g1.transition_dict.get(i).deactivate()
    
    g1.update()
    return cal(g1)


def step_by_step_selection_probability(g1:graphs.Graphs):
    states = g1.get_states_names()
    deact_transitions = set()
    for i in states:
        g1.activate_all_the_transitions()
        trans = g1.get_state(i).out_transitions
        controllable_trans = []
        for j in trans:
            if g1.get_transition(j).controllable:
                controllable_trans.append(j)
        part1 = brute_force.brute_force_for_sbss(g1, controllable_trans)
        de_trans = part1[0].get('Deactivated Transitions')
        for j in de_trans:
            deact_transitions.add(j)
    g1.activate_all_the_transitions()
    for i in deact_transitions:
        g1.get_transition(i).deactivate()

    g1.update()
    return cal(g1)


def step_by_step_selection(g1:graphs.Graphs):
    states = g1.get_states_names()
    deact_transitions = set()
    for i in states:
        g1.activate_all_the_transitions()
        trans = g1.get_state(i).out_transitions
        controllable_trans = []
        for j in trans:
            if g1.get_transition(j).controllable:
                controllable_trans.append(j)
        part1 = brute_force.brute_force_for_sbss(g1, controllable_trans)
        de_trans = part1[0].get('Deactivated Transitions')
        for j in de_trans:
            deact_transitions.add(j)
    g1.activate_all_the_transitions()
    for i in deact_transitions:
        g1.get_transition(i).deactivate()

    g1.update()
    return result_GUI(g1)


                



