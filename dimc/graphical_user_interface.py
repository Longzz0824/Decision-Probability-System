import tkinter as tk
from tkinter import messagebox
from input import manual_input
from graphs import show_graph
from PIL import ImageTk, Image
from tkinter import ttk
import heuristic
import brute_force
from graph_matrix import random_graph_generate

window = tk.Tk()
window.title('Optimal Decision-making in Probabilistic Systems')

width = 800
height = 600
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
size_geo = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)
window.geometry(size_geo)

label1 = tk.Label(window,text="Welcome to Optimal Decision-making in Probabilistic Systems!",font=("Arial",20))
empty_label = tk.Label(window)
label2 = tk.Label(window,text="First you need to determine how the system will be generated.",font=("Arial",15))
label3 = tk.Label(window,text="We offer the following two generation methods, please make your choice.",font=("Arial",15))

def create_new_window_for_manual_input():
    new_window1 = tk.Toplevel(window)
    new_window1.geometry(size_geo)
    label1_0 = tk.Label(new_window1, text = "Please input the following data to generate a controllable probability system.")
    label1_1 = tk.Label(new_window1, text = "Number of states:")
    label1_2 = tk.Label(new_window1, text = "Initial state:")
    label1_3 = tk.Label(new_window1, text = "Final state:")
    label1_4 = tk.Label(new_window1, text = "Input all transitions:")
    label1_5 = tk.Label(new_window1, text = "All states will be automatically \nnamed s0, s1, ..., sn-1")
    label1_6 = tk.Label(new_window1, text = "Input form is like:\n a->b 0.5 can, b->c 0.2 cannot \n can means controllable \ncannot means uncontrollable\n 0.5 and 0.2 mean the \ninitial probability of transition")

    def manual_input_gui():
        num = int(entry1_1.get())
        i_s = entry1_2.get()
        f_s = entry1_3.get()
        trans = entry1_4.get()
        g1 = manual_input(num,i_s,f_s,trans)
        show_graph(g1)
        img = Image.open("graph.png")
        img = img.resize((250, int(250/img.width * img.height)))
        img.save("resized_graph.png")
        photo = ImageTk.PhotoImage(img)
        label_graph1 = tk.Label(new_window1, image=photo,width=250,height=375)
        label_graph1.image = photo
        label_graph1.grid(row=6,column= 0,sticky='w')
        label1_7 = tk.Label(new_window1, text="The system image is as follows:").grid(row=5,sticky='w')
        label1_8 = tk.Label(new_window1, text="Select an algorithm:").grid(row=6,column=1)
        
        

        def b_f():
            res, t = brute_force.brute_force_gui(g1)
            new_window1_1 = tk.Toplevel(new_window1)
            new_window1_1.geometry(size_geo)
            label_bf1 = tk.Label(new_window1_1, text="The result of Brute Force is as follows:",font=("Arial",20))
            empty_label_bf = tk.Label(new_window1_1)
            label_bf2 = tk.Label(new_window1_1, text="The arrival probability is:",font=("Arial",15))
            label_bf_probability = tk.Label(new_window1_1, text= res,font=("Arial",15))
            label_bf_3 = tk.Label(new_window1_1, text="The deactivated transitions are:",font=("Arial",15))
            label_bf_strategy = tk.Text(new_window1_1,font=("Arial",15),height=10, width=50)

            label_bf1.grid(row=0, column=0,  sticky="w")
            empty_label_bf.grid(row=1, column=0, rowspan=3)
            label_bf2.grid(row=4, column=0,  sticky="w")
            label_bf_probability.grid(row=4, column=1,  sticky="w")
            label_bf_3.grid(row=5, column=0,  sticky="w")
            label_bf_strategy.insert(tk.END, t)
            label_bf_strategy.grid(row=6, column=0,  sticky="w")

        def deactivate_all_useless_transitions():
            res, t = heuristic.deactivate_all_useless_transitions(g1)
            new_window1_1 = tk.Toplevel(new_window1)
            new_window1_1.geometry(size_geo)
            label_bf1 = tk.Label(new_window1_1, text="The result of DAUT is as follows:",font=("Arial",20))
            empty_label_bf = tk.Label(new_window1_1)
            label_bf2 = tk.Label(new_window1_1, text="The arrival probability is:",font=("Arial",15))
            label_bf_probability = tk.Label(new_window1_1, text= res,font=("Arial",15))
            label_bf_3 = tk.Label(new_window1_1, text="The deactivated transitions are:",font=("Arial",15))
            label_bf_strategy = tk.Text(new_window1_1,font=("Arial",15),height=10, width=50)

            label_bf1.grid(row=0, column=0,  sticky="w")
            empty_label_bf.grid(row=1, column=0, rowspan=3)
            label_bf2.grid(row=4, column=0,  sticky="w")
            label_bf_probability.grid(row=4, column=1,  sticky="w")
            label_bf_3.grid(row=5, column=0,  sticky="w")
            label_bf_strategy.insert(tk.END, t)
            label_bf_strategy.grid(row=6, column=0,  sticky="w")
        
        def brute_force_after_DAUT():
            res, t = heuristic.brute_force_after_daut(g1)
            new_window1_1 = tk.Toplevel(new_window1)
            new_window1_1.geometry(size_geo)
            label_bf1 = tk.Label(new_window1_1, text="The result of Brute Force After DAUT is as follows:",font=("Arial",20))
            empty_label_bf = tk.Label(new_window1_1)
            label_bf2 = tk.Label(new_window1_1, text="The arrival probability is:",font=("Arial",15))
            label_bf_probability = tk.Label(new_window1_1, text= res,font=("Arial",15))
            label_bf_3 = tk.Label(new_window1_1, text="The deactivated transitions are:",font=("Arial",15))
            label_bf_strategy = tk.Text(new_window1_1,font=("Arial",15),height=10, width=50)

            label_bf1.grid(row=0, column=0,  sticky="w")
            empty_label_bf.grid(row=1, column=0, rowspan=3)
            label_bf2.grid(row=4, column=0,  sticky="w")
            label_bf_probability.grid(row=4, column=1,  sticky="w")
            label_bf_3.grid(row=5, column=0,  sticky="w")
            label_bf_strategy.insert(tk.END, t)
            label_bf_strategy.grid(row=6, column=0,  sticky="w")

        def dijkstra():
            res, t = heuristic.dijkstra(g1)
            new_window1_1 = tk.Toplevel(new_window1)
            new_window1_1.geometry(size_geo)
            label_bf1 = tk.Label(new_window1_1, text="The result of Dijkstra is as follows:",font=("Arial",20))
            empty_label_bf = tk.Label(new_window1_1)
            label_bf2 = tk.Label(new_window1_1, text="The arrival probability is:",font=("Arial",15))
            label_bf_probability = tk.Label(new_window1_1, text= res,font=("Arial",15))
            label_bf_3 = tk.Label(new_window1_1, text="The deactivated transitions are:",font=("Arial",15))
            label_bf_strategy = tk.Text(new_window1_1,font=("Arial",15),height=10, width=50)

            label_bf1.grid(row=0, column=0,  sticky="w")
            empty_label_bf.grid(row=1, column=0, rowspan=3)
            label_bf2.grid(row=4, column=0,  sticky="w")
            label_bf_probability.grid(row=4, column=1,  sticky="w")
            label_bf_3.grid(row=5, column=0,  sticky="w")
            label_bf_strategy.insert(tk.END, t)
            label_bf_strategy.grid(row=6, column=0,  sticky="w")

        def step_by_step_selection():
            res, t = heuristic.step_by_step_selection(g1)
            print(res,t)
            new_window1_1 = tk.Toplevel(new_window1)
            new_window1_1.geometry(size_geo)
            label_bf1 = tk.Label(new_window1_1, text="The result of Step By Step Selection is as follows:",font=("Arial",20))
            empty_label_bf = tk.Label(new_window1_1)
            label_bf2 = tk.Label(new_window1_1, text="The arrival probability is:",font=("Arial",15))
            label_bf_probability = tk.Label(new_window1_1, text= res,font=("Arial",15))
            label_bf_3 = tk.Label(new_window1_1, text="The deactivated transitions are:",font=("Arial",15))
            label_bf_strategy = tk.Text(new_window1_1,font=("Arial",15),height=10, width=50)

            label_bf1.grid(row=0, column=0,  sticky="w")
            empty_label_bf.grid(row=1, column=0, rowspan=3)
            label_bf2.grid(row=4, column=0,  sticky="w")
            label_bf_probability.grid(row=4, column=1,  sticky="w")
            label_bf_3.grid(row=5, column=0,  sticky="w")
            label_bf_strategy.insert(tk.END, t)
            label_bf_strategy.grid(row=6, column=0,  sticky="w")

        def select_option(event):
            selected_option = cbox.get()
            if selected_option == "Brute force":
                b_f()
            elif selected_option == "Deactivate all useless transitions":
                deactivate_all_useless_transitions()
            elif selected_option == "Brute force after DAUT":
                brute_force_after_DAUT()
            elif selected_option == "Dijkstra":
                dijkstra()
            elif selected_option == "Step by step selection":
                step_by_step_selection()

        

        cbox = ttk.Combobox(new_window1,values=['Brute force','Deactivate all useless transitions','Brute force after DAUT','Dijkstra','Step by step selection'])
        cbox.bind("<<ComboboxSelected>>", select_option)
        cbox.grid(row = 6, column=2)
        

    

    entry1_1 = tk.Entry(new_window1)
    entry1_2 = tk.Entry(new_window1)
    entry1_3 = tk.Entry(new_window1)
    entry1_4 = tk.Entry(new_window1)
    button1_1 = tk.Button(new_window1, text = "Generate",bg='#7CCD7C',command=manual_input_gui)

    label1_0.grid(row=0,sticky="w")
    label1_1.grid(row=1,sticky="w")
    label1_5.grid(row=1,column=2,sticky="w")
    label1_2.grid(row=2,sticky="w")
    label1_3.grid(row=3,sticky="w")
    label1_4.grid(row=4,sticky="w")
    label1_6.grid(row=4,column=2,sticky="w")
    entry1_1.grid(row=1, column=1)
    entry1_2.grid(row=2, column=1)
    entry1_3.grid(row=3, column=1)
    entry1_4.grid(row=4, column=1)
    button1_1.grid(row=5,column=1)
 






def create_new_window_for_random_generation():
    new_window1 = tk.Toplevel(window)
    new_window1.geometry(size_geo)
    label1_0 = tk.Label(new_window1, text = "Randomly generate a controllable probability system",font=("Arial",20))
    label1_1 = tk.Label(new_window1, text = "The number of states:")
    entry1_1 = tk.Entry(new_window1)

    def random_generation():
        num = int(entry1_1.get())
        g1= random_graph_generate(num)
        initial_state = g1.initial_state_name
        final_state = g1.final_state_name
        show_graph(g1)
        img = Image.open("graph.png")
        img = img.resize((250, int(250/img.width * img.height)))
        img.save("resized_graph.png")
        photo = ImageTk.PhotoImage(img)
        label_graph1 = tk.Label(new_window1, image=photo,width=250,height=375)
        label_graph1.image = photo
        label1_2 = tk.Label(new_window1, text = "The initial state:").grid(row=3,sticky='e')
        label1_3 = tk.Label(new_window1, text = "The final state:").grid(row=4,sticky='e')
        label1_22 = tk.Label(new_window1, text = initial_state).grid(row=3,column=1,sticky='e')
        label1_32 = tk.Label(new_window1, text = final_state).grid(row=4,column=1,sticky='e')


        label1_7 = tk.Label(new_window1, text="The system image is as follows:").grid(row=5,sticky='w')
        label_graph1.grid(row=6,column= 0,sticky='w')
        label1_8 = tk.Label(new_window1, text="Select an algorithm:").grid(row=5,column=1,sticky='w')

        def b_f():
            res, t = brute_force.brute_force_gui(g1)
            new_window1_1 = tk.Toplevel(new_window1)
            new_window1_1.geometry(size_geo)
            label_bf1 = tk.Label(new_window1_1, text="The result of Brute Force is as follows:",font=("Arial",20))
            empty_label_bf = tk.Label(new_window1_1)
            label_bf2 = tk.Label(new_window1_1, text="The arrival probability is:",font=("Arial",15))
            label_bf_probability = tk.Label(new_window1_1, text= res,font=("Arial",15))
            label_bf_3 = tk.Label(new_window1_1, text="The deactivated transitions are:",font=("Arial",15))
            label_bf_strategy = tk.Text(new_window1_1,font=("Arial",15),height=10, width=50)

            label_bf1.grid(row=0, column=0,  sticky="w")
            empty_label_bf.grid(row=1, column=0, rowspan=3)
            label_bf2.grid(row=4, column=0,  sticky="w")
            label_bf_probability.grid(row=4, column=1,  sticky="w")
            label_bf_3.grid(row=5, column=0,  sticky="w")
            label_bf_strategy.insert(tk.END, t)
            label_bf_strategy.grid(row=6, column=0,  sticky="w")

        def deactivate_all_useless_transitions():
            res, t = heuristic.deactivate_all_useless_transitions(g1)
            new_window1_1 = tk.Toplevel(new_window1)
            new_window1_1.geometry(size_geo)
            label_bf1 = tk.Label(new_window1_1, text="The result of DAUT is as follows:",font=("Arial",20))
            empty_label_bf = tk.Label(new_window1_1)
            label_bf2 = tk.Label(new_window1_1, text="The arrival probability is:",font=("Arial",15))
            label_bf_probability = tk.Label(new_window1_1, text= res,font=("Arial",15))
            label_bf_3 = tk.Label(new_window1_1, text="The deactivated transitions are:",font=("Arial",15))
            label_bf_strategy = tk.Text(new_window1_1,font=("Arial",15),height=10, width=50)

            label_bf1.grid(row=0, column=0,  sticky="w")
            empty_label_bf.grid(row=1, column=0, rowspan=3)
            label_bf2.grid(row=4, column=0,  sticky="w")
            label_bf_probability.grid(row=4, column=1,  sticky="w")
            label_bf_3.grid(row=5, column=0,  sticky="w")
            label_bf_strategy.insert(tk.END, t)
            label_bf_strategy.grid(row=6, column=0,  sticky="w")
        
        def brute_force_after_DAUT():
            res, t = heuristic.brute_force_after_daut(g1)
            new_window1_1 = tk.Toplevel(new_window1)
            new_window1_1.geometry(size_geo)
            label_bf1 = tk.Label(new_window1_1, text="The result of Brute Force After DAUT is as follows:",font=("Arial",20))
            empty_label_bf = tk.Label(new_window1_1)
            label_bf2 = tk.Label(new_window1_1, text="The arrival probability is:",font=("Arial",15))
            label_bf_probability = tk.Label(new_window1_1, text= res,font=("Arial",15))
            label_bf_3 = tk.Label(new_window1_1, text="The deactivated transitions are:",font=("Arial",15))
            label_bf_strategy = tk.Text(new_window1_1,font=("Arial",15),height=10, width=50)

            label_bf1.grid(row=0, column=0,  sticky="w")
            empty_label_bf.grid(row=1, column=0, rowspan=3)
            label_bf2.grid(row=4, column=0,  sticky="w")
            label_bf_probability.grid(row=4, column=1,  sticky="w")
            label_bf_3.grid(row=5, column=0,  sticky="w")
            label_bf_strategy.insert(tk.END, t)
            label_bf_strategy.grid(row=6, column=0,  sticky="w")

        def dijkstra():
            res, t = heuristic.dijkstra(g1)
            new_window1_1 = tk.Toplevel(new_window1)
            new_window1_1.geometry(size_geo)
            label_bf1 = tk.Label(new_window1_1, text="The result of Dijkstra is as follows:",font=("Arial",20))
            empty_label_bf = tk.Label(new_window1_1)
            label_bf2 = tk.Label(new_window1_1, text="The arrival probability is:",font=("Arial",15))
            label_bf_probability = tk.Label(new_window1_1, text= res,font=("Arial",15))
            label_bf_3 = tk.Label(new_window1_1, text="The deactivated transitions are:",font=("Arial",15))
            label_bf_strategy = tk.Text(new_window1_1,font=("Arial",15),height=10, width=50)

            label_bf1.grid(row=0, column=0,  sticky="w")
            empty_label_bf.grid(row=1, column=0, rowspan=3)
            label_bf2.grid(row=4, column=0,  sticky="w")
            label_bf_probability.grid(row=4, column=1,  sticky="w")
            label_bf_3.grid(row=5, column=0,  sticky="w")
            label_bf_strategy.insert(tk.END, t)
            label_bf_strategy.grid(row=6, column=0,  sticky="w")

        def step_by_step_selection():
            res, t = heuristic.step_by_step_selection(g1)
            print(res,t)
            new_window1_1 = tk.Toplevel(new_window1)
            new_window1_1.geometry(size_geo)
            label_bf1 = tk.Label(new_window1_1, text="The result of Step By Step Selection is as follows:",font=("Arial",20))
            empty_label_bf = tk.Label(new_window1_1)
            label_bf2 = tk.Label(new_window1_1, text="The arrival probability is:",font=("Arial",15))
            label_bf_probability = tk.Label(new_window1_1, text= res,font=("Arial",15))
            label_bf_3 = tk.Label(new_window1_1, text="The deactivated transitions are:",font=("Arial",15))
            label_bf_strategy = tk.Text(new_window1_1,font=("Arial",15),height=10, width=50)

            label_bf1.grid(row=0, column=0,  sticky="w")
            empty_label_bf.grid(row=1, column=0, rowspan=3)
            label_bf2.grid(row=4, column=0,  sticky="w")
            label_bf_probability.grid(row=4, column=1,  sticky="w")
            label_bf_3.grid(row=5, column=0,  sticky="w")
            label_bf_strategy.insert(tk.END, t)
            label_bf_strategy.grid(row=6, column=0,  sticky="w")

        def select_option(event):
            selected_option = cbox.get()
            if selected_option == "Brute force":
                b_f()
            elif selected_option == "Deactivate all useless transitions":
                deactivate_all_useless_transitions()
            elif selected_option == "Brute force after DAUT":
                brute_force_after_DAUT()
            elif selected_option == "Dijkstra":
                dijkstra()
            elif selected_option == "Step by step selection":
                step_by_step_selection()

        

        cbox = ttk.Combobox(new_window1,values=['Brute force','Deactivate all useless transitions','Brute force after DAUT','Dijkstra','Step by step selection'])
        cbox.bind("<<ComboboxSelected>>", select_option)
        cbox.grid(row = 6, column=1,sticky="nw")

    label1_0.grid(row=0,sticky="w")
    label1_1.grid(row=1,sticky="w")
    entry1_1.grid(row=1, column=1)
    button1_1 = tk.Button(new_window1, text = "Generate",bg='#7CCD7C',command=random_generation)
    button1_1.grid(row=2, column=1,sticky="e")





Button1 = tk.Button(window,text="Manual input",bg='#7CCD7C',command=create_new_window_for_manual_input)
Button2 = tk.Button(window,text="Random Generation",bg='#6495ED',command=create_new_window_for_random_generation)


window.columnconfigure(0, weight=1)
label1.grid(row=0, column=0,  sticky="nsew")
empty_label.grid(row=1, column=0, rowspan=3)
label2.grid(row=5, column=0, sticky="w")
label3.grid(row=6, column=0, sticky="w")


Button1.grid(rowspan=3, columnspan=1,row=7, column=0, sticky="nsew")
Button2.grid(rowspan=3, columnspan=1,row=10, column=0, sticky="nsew")
window.mainloop()