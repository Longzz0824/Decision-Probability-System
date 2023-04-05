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
    time_consumption_bf = []
    time_consumption_daut = []
    time_consumption_dijk = []
    time_consumption_bfad = []
    time_consumption_sbss = []
    time_consumption = []
    count_bf = []
    count_daut = []
    count_dijk = []
    count_bfad = []
    count_sbss = []
    count = []

    for j in range(10):
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

        count = []
        for i in range(num):
            probabilities = []
            print("is calculate situation:",i+1)
            states_num = j+1
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
        
        time_consumption_bf.append(time1)  
        time_consumption_daut.append(time2)  
        time_consumption_dijk.append(time3)  
        time_consumption_bfad.append(time4)
        time_consumption_sbss.append(time5)
        
        count_bf.append(brute_force_count)   
        count_daut.append(deactivate_all_useless_transitions_count)   
        count_dijk.append(dijkstra_count)   
        count_bfad.append(brute_force_after_daut_count)   
        count_sbss.append(step_by_step_selection_count)

    time_consumption.append(time_consumption_bf)
    time_consumption.append(time_consumption_daut)
    time_consumption.append(time_consumption_dijk)
    time_consumption.append(time_consumption_bfad)
    time_consumption.append(time_consumption_sbss)

    count.append(count_bf)
    count.append(count_daut)
    count.append(count_dijk)
    count.append(count_bfad)
    count.append(count_sbss)

    statistical_chart(time_consumption,count)


def statistical_chart(time_consumption:list, count:list):

    method = ['brute_force','deactivate_all_useless_transitions','dijkstra','brute_force_after_daut','step_by_step_selection']
    x = range(1,11)
    z1 = time_consumption[0]
    z2 = time_consumption[1]
    z3 = time_consumption[2]
    z4 = time_consumption[3]
    z5 = time_consumption[4]
    y1 = count[0]
    y2 = count[1]
    y3 = count[2]
    y4 = count[3]
    y5 = count[4]
    fig, axes = plt.subplots(2, 1)
    axes[0].plot(x, y1,color='blue',label='brute force')
    axes[0].plot(x, y2,color='red',label='deactivate all useless transitions')
    axes[0].plot(x, y3,color='yellow',label='dijkstra')
    axes[0].plot(x, y4,color='green',label='brute force after daut')
    axes[0].plot(x, y5,color='black',label='step by step selection')
    axes[0].set_title("Success rate evaluation")
    axes[0].set_xlabel('The size of system')
    axes[0].set_ylabel('The number of times')
    axes[0].legend()

    axes[1].plot(x, z1,color='blue',label='brute force')
    axes[1].plot(x, z2,color='red',label='deactivate all useless transitions')
    axes[1].plot(x, z3,color='yellow',label='dijkstra')
    axes[1].plot(x, z4,color='green',label='brute force after daut')
    axes[1].plot(x, z5,color='black',label='step by step selection')
    axes[1].set_title("Time consumption evaluation")
    axes[1].set_xlabel('The size of system')
    axes[1].set_ylabel('Time consumption')
    axes[1].set_yscale('log')
    axes[1].legend()
    fig.suptitle("Evaluation")

    plt.tight_layout()
    plt.savefig('chart.png', format='png')
    plt.show()

