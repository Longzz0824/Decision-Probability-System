import brute_force
import graph_matrix
import heuristic
import random
import time
import statistics
import calculation
import graphs
def evaluate(num:int): #num : The number of runs of the program used for evaluation
    brute_force_count = 0
    brute_force_time = []
    deactivate_all_useless_transitions_count = 0
    deactivate_all_useless_transitions_time = []
    dijkstra_count = 0
    dijkstra_time = []
    for i in range(num):
        probabilities = []
        
        states_num = random.randint(5,10)
        test_graph = graph_matrix.random_graph_generate(states_num)
        t0 = time.process_time()
        pro1 = brute_force.brute_force_probability(test_graph)
        t1 = time.process_time()
        brute_force_time.append(t1 - t0) 
        probabilities.append(pro1)
        
        test_graph.activate_all_the_transitions()
        t0 = time.process_time()
        pro2 = heuristic.deactivate_all_useless_transitions_probability(test_graph)
        t1 = time.process_time()
        deactivate_all_useless_transitions_time.append(t1 - t0) 
        probabilities.append(pro2)
        

        t0 = time.process_time()
        pro3 = heuristic.dijkstra_probability(test_graph)        
        t1 = time.process_time()
        dijkstra_time.append(t1 - t0) 
        probabilities.append(pro3)


        print(probabilities)
        print('================')
        for i in range(3):
            aa = float(probabilities[i].strip('%')) 
            bb = aa/100.0
            probabilities[i] = bb
        
        
        index = brute_force.max_index(probabilities)
        if 0 in index:
            brute_force_count += 1
        if 1 in index:
            deactivate_all_useless_transitions_count += 1
        if 2 in index:
            dijkstra_count += 1
    
    time1 = statistics.mean(brute_force_time)
    time2 = statistics.mean(deactivate_all_useless_transitions_time)
    time3 = statistics.mean(dijkstra_time)
        
    print("The number of times to get the maximum probability by brute force method: ", brute_force_count)
    print("The number of times to get the maximum probability by deactivate all useless transitions method: ", deactivate_all_useless_transitions_count)
    print("The number of times to get the maximum probability by dijkstra method: ", dijkstra_count)
    print("Average running time of brute force method: ", time1)
    print("Average running time of deactivate all useless transitions method: ", time2)
    print("Average running time of dijkstra method: ", time3)
