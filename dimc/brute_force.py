import graphs
import transitions
from calculation import cal
import time

def max_index(lst:list):
    index = []
    max_n = max(lst)
    for i in range(len(lst)):
        if lst[i] == max_n:
            index.append(i)
    return index

def res_print(dic:dict):
    for i,j in dic.items():
        sss = i +': '+str(j)
        print(sss)


def brute_force(g:graphs.Graphs):
    trans = g.get_controllable_transitions()
    transitions_num = len(trans)
    lst = []
    num = 2**transitions_num - 1
    res = []
    for i in range(num,-1,-1):
        lst = list(bin(i)[2:].rjust(transitions_num,'0'))

        for j in range(transitions_num):
            m = trans[j]
            if lst[j] == '1':
#                print('1')
                g.get_transition(m).activate()
            elif lst[j] == '0':
#                print('0')
                g.get_transition(m).deactivate()
#            elif lst[j] == '0' and g.get_transition(m).controllable == False:
#                break
        else:    
            prob_str = cal(g)
            dic1 ={}
            dic1.update(g.get_transitions_status())
            dic1.update({'Probability' : prob_str})
            res.append(dic1)
        print(dic1)
    print(res)
    pr_list = []
    for i in range(len(res)):
        resp = res[i]
        pr = resp['Probability']
        aa = float(pr.strip('%')) 
        bb = aa/100.0
        pr_list.append(bb)
#    print(pr_list)
    index = max_index(pr_list)
#    print(index)
    res_list = []
    for i in index:
        n = res[i]
        res_list.append(n)
    
    for i in range(len(res_list)):
        print('\nBrute force result is: ')
        print('Result %d is: ' %(i+1))
        res_print(res_list[i])

def brute_force_probability(g:graphs.Graphs):  #same with brute_force, but it only return the probability

    trans = g.get_controllable_transitions()
    transitions_num = len(trans)
    lst = []
    num = 2**transitions_num - 1
    res = []
    targ = 0
    for i in range(num,-1,-1):
        lst = list(bin(i)[2:].rjust(transitions_num,'0'))
        targ= targ +1

        for j in range(transitions_num):
            m = trans[j]
            if lst[j] == '1':
#                print('1')
                g.get_transition(m).activate()
            elif lst[j] == '0':
#                print('0')
                g.get_transition(m).deactivate()
#            elif lst[j] == '0' and g.get_transition(m).controllable == False:
#                break
        else:    
            prob_str = cal(g)
            dic1 ={}
            dic1.update(g.get_transitions_status())
            dic1.update({'Probability' : prob_str})
            res.append(dic1)
#        print(dic1)
#    print(res)
    pr_list = []
    for i in range(len(res)):
        resp = res[i]
        pr = resp['Probability']
        aa = float(pr.strip('%')) 
        bb = aa/100.0
        pr_list.append(bb)
#    print(pr_list)
    highest_probability = max(pr_list)
    highest_probability = "%.2f%%" % (highest_probability * 100)
    return highest_probability


        



def brute_force_part(g:graphs.Graphs):
    trans = g.get_activated_controllable_transitions()
    transitions_num = len(trans)
    lst = []
    num = 2**transitions_num - 1
    res = []
    for i in range(num,-1,-1):
        lst = list(bin(i)[2:].rjust(transitions_num,'0'))

        for j in range(transitions_num):
            m = trans[j]
            if lst[j] == '1':
#                print('1')
                g.get_transition(m).activate()
            elif lst[j] == '0':
#                print('0')
                g.get_transition(m).deactivate()
#            elif lst[j] == '0' and g.get_transition(m).controllable == False:
#                break
        else:    
            prob_str = cal(g)
            dic1 ={}
            dic1.update(g.get_transitions_status())
            dic1.update({'Probability' : prob_str})
            res.append(dic1)
#        print(dic1)
#    print(res)
    pr_list = []
    for i in range(len(res)):
        resp = res[i]
        pr = resp['Probability']
        aa = float(pr.strip('%')) 
        bb = aa/100.0
        pr_list.append(bb)
#    print(pr_list)
    index = max_index(pr_list)
#    print(index)
    res_list = []
    for i in index:
        n = res[i]
        res_list.append(n)
    
    for i in range(len(res_list)):
        print('\nBrute force after daut result is: ')
        print('Result %d is: ' %(i+1))
        res_print(res_list[i])



def brute_force_part_probability(g:graphs.Graphs):  #same with brute_force, but it only return the probability

    trans = g.get_activated_controllable_transitions()
    transitions_num = len(trans)
    lst = []
    num = 2**transitions_num - 1
    res = []
    for i in range(num,-1,-1):
        lst = list(bin(i)[2:].rjust(transitions_num,'0'))
        for j in range(transitions_num):
            m = trans[j]
            if lst[j] == '1':
#                print('1')
                g.get_transition(m).activate()
            elif lst[j] == '0':
#                print('0')
                g.get_transition(m).deactivate()
#            elif lst[j] == '0' and g.get_transition(m).controllable == False:
#                break
        else:    
            prob_str = cal(g)
            dic1 ={}
            dic1.update(g.get_transitions_status())
            dic1.update({'Probability' : prob_str})
            res.append(dic1)
#        print(dic1)
#    print(res)
    pr_list = []
    for i in range(len(res)):
        resp = res[i]
        pr = resp['Probability']
        aa = float(pr.strip('%')) 
        bb = aa/100.0
        pr_list.append(bb)

    highest_probability = max(pr_list)
    highest_probability = "%.2f%%" % (highest_probability * 100)
    return highest_probability


def brute_force_for_sbss(g:graphs.Graphs, transitions:list):
    trans = transitions
    transitions_num = len(trans)
    lst = []
    num = 2**transitions_num - 1
    res = []
    for i in range(num,-1,-1):
        lst = list(bin(i)[2:].rjust(transitions_num,'0'))
        for j in range(transitions_num):
            m = trans[j]
            if lst[j] == '1':
#                print('1')
                g.get_transition(m).activate()
            elif lst[j] == '0':
#                print('0')
                g.get_transition(m).deactivate()
#            elif lst[j] == '0' and g.get_transition(m).controllable == False:
#                break
        else:    
            prob_str = cal(g)
            dic1 ={}
            dic1.update(g.get_transitions_status())
            dic1.update({'Probability' : prob_str})
            res.append(dic1)
#        print(dic1)
#    print(res)
    pr_list = []
    for i in range(len(res)):
        resp = res[i]
        pr = resp['Probability']
        aa = float(pr.strip('%')) 
        bb = aa/100.0
        pr_list.append(bb)
#    print(pr_list)
    index = max_index(pr_list)
#    print(index)
    res_list = []
    for i in index:
        n = res[i]
        res_list.append(n)
    return res_list

def brute_force_gui(g:graphs.Graphs):
    t0 = time.process_time()
    trans = g.get_controllable_transitions()
    transitions_num = len(trans)
    lst = []
    num = 2**transitions_num - 1
    res = []
    for i in range(num,-1,-1):
        lst = list(bin(i)[2:].rjust(transitions_num,'0'))

        for j in range(transitions_num):
            m = trans[j]
            if lst[j] == '1':
#                print('1')
                g.get_transition(m).activate()
            elif lst[j] == '0':
#                print('0')
                g.get_transition(m).deactivate()
#            elif lst[j] == '0' and g.get_transition(m).controllable == False:
#                break
        else:    
            prob_str = cal(g)
            dic1 ={}
            dic1.update(g.get_transitions_status())
            dic1.update({'Probability' : prob_str})
            res.append(dic1)
        print(dic1)
    print(res)
    pr_list = []
    for i in range(len(res)):
        resp = res[i]
        pr = resp['Probability']
        aa = float(pr.strip('%')) 
        bb = aa/100.0
        pr_list.append(bb)
#    print(pr_list)
    index = max_index(pr_list)
#    print(index)
    res_list = []
    for i in index:
        n = res[i]
        res_list.append(n)
    t1 = time.process_time()
    time_consumed = t1 - t0
    return res_list, time_consumed