import brute_force
import graph_matrix
import heuristic
import random
import time
import statistics
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def evaluate(num:int): #num : The number of runs of the program used for evaluation
    brute_force_count = 0
    brute_force_time = []
    deactivate_all_useless_transitions_count = 0
    deactivate_all_useless_transitions_time = []
    dijkstra_count = 0
    dijkstra_time = []
    brute_force_after_daut_count = 0
    brute_force_after_daut_time = []
    step_by_step_selection_count = 0
    step_by_step_selection_time = []    
    method = ['brute_force','deactivate_all_useless_transitions','dijkstra','brute_force_after_daut','step_by_step_selection']
    time_consumption= []
    count = []
    for i in range(num):
        probabilities = []
        print("is calculate situation:",i+1)
        states_num = random.randint(5,10)
        print("states num",states_num)
        test_graph = graph_matrix.random_graph_generate(states_num)
        print('generate finish')
        t0 = time.process_time()
        pro1 = brute_force.brute_force_probability(test_graph)
        t1 = time.process_time()

        brute_force_time.append(t1 - t0) 
        probabilities.append(pro1)
        print('brute force finish')

        t0 = time.process_time()
        pro2 = heuristic.deactivate_all_useless_transitions_probability(test_graph)
        t1 = time.process_time()
        deactivate_all_useless_transitions_time.append(t1 - t0) 
        probabilities.append(pro2)
        print('daut finish')

        t0 = time.process_time()
        pro3 = heuristic.dijkstra_probability(test_graph)        
        t1 = time.process_time()
        dijkstra_time.append(t1 - t0) 
        probabilities.append(pro3)
        print('dijkstra finish')

        t0 = time.process_time()
        pro4 = heuristic.brute_force_after_daut_evaluation(test_graph)        
        t1 = time.process_time()
        brute_force_after_daut_time.append(t1 - t0) 
        probabilities.append(pro4)
        print('brute force after daut finish')


        t0 = time.process_time()
        pro5 = heuristic.step_by_step_selection_probability(test_graph)        
        t1 = time.process_time()
        step_by_step_selection_time.append(t1 - t0) 
        probabilities.append(pro5)
        print('step_by_step_selection finish')

        print(probabilities)
        print('================')
        for i in range(5):
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
        if 3 in index:
            brute_force_after_daut_count += 1
        if 4 in index:
            step_by_step_selection_count += 1
    
    time1 = statistics.mean(brute_force_time)
    time2 = statistics.mean(deactivate_all_useless_transitions_time)
    time3 = statistics.mean(dijkstra_time)
    time4 = statistics.mean(brute_force_after_daut_time)
    time5 = statistics.mean(step_by_step_selection_time)
    time_consumption.append(time1)  
    time_consumption.append(time2)  
    time_consumption.append(time3)  
    time_consumption.append(time4)
    time_consumption.append(time5)
    count.append(brute_force_count)   
    count.append(deactivate_all_useless_transitions_count)   
    count.append(dijkstra_count)   
    count.append(brute_force_after_daut_count)   
    count.append(step_by_step_selection_count)
    print("The number of times to get the maximum probability by brute force method: ", brute_force_count)
    print("The number of times to get the maximum probability by deactivate all useless transitions method: ", deactivate_all_useless_transitions_count)
    print("The number of times to get the maximum probability by dijkstra method: ", dijkstra_count)
    print("The number of times to get the maximum probability by brute force after daut method: ", brute_force_after_daut_count)
    print("The number of times to get the maximum probability by step_by_step_selection method: ", step_by_step_selection_count)
    print("Average running time of brute force method: ", time1)
    print("Average running time of deactivate all useless transitions method: ", time2)
    print("Average running time of dijkstra method: ", time3)  
    print("Average running time of brute force after daut method: ", time4)
    print("Average running time of step_by_step_selection method: ", time5)
    print(time_consumption)
    statistical_chart(method,time_consumption,count)


def statistical_chart(method:list, time_consumption:list, count:list):

    x = method
    y = time_consumption
    z = count
    fig, axes = plt.subplots(2, 1)
    axes[0].bar(x, z)
    axes[0].set_title("The number of times to get the maximum probability")
    axes[1].bar(x, y)
    axes[1].set_title("Average running time")
    fig.suptitle("Evaluation")
    plt.tight_layout()
    plt.show()

