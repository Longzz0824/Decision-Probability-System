import graphs
import transitions
from calculation import cal

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
    trans = g.get_transitions_names()
    ln = len(trans)
    lst = []
    num = 2**ln - 1
    res = []
    for i in range(num,-1,-1):
        lst = list(bin(i)[2:].rjust(ln,'0'))

        for j in range(ln):
            m = trans[j]
            if lst[j] == '1':
#                print('1')
                g.get_transition(m).activate()
            else:
#                print('0')
                g.get_transition(m).deactivate()

        prob = cal(g)
        dic1 ={}
        dic1.update(g.get_transitions_dict())
        dic1.update({'Probability' : prob})
        res.append(dic1)
#        print(dic1)
#    print(res)
    pr_list = []
    for i in range(num+1):
        resp = res[i]
        pr = resp['Probability']
        pr_list.append(pr)
    
    index = max_index(pr_list)
    res_list = []
    for i in index:
        n = res[i]
        res_list.append(n)
    
    for i in range(len(res_list)):
        print('Result %d is: ' %(i+1))
        res_print(res_list[i])
        




