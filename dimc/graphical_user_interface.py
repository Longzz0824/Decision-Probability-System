import tkinter as tk
from tkinter import messagebox
from input import manual_input
from graphs import show_graph
from PIL import ImageTk, Image
from tkinter import ttk
import heuristic
import brute_force

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
    label1_1 = tk.Label(new_window1, text = "The number of states:")
    label1_2 = tk.Label(new_window1, text = "The initial state:")
    label1_3 = tk.Label(new_window1, text = "The final state:")
    label1_4 = tk.Label(new_window1, text = "Input all the transitions:")
    label1_5 = tk.Label(new_window1, text = "All states will be automatically \nnamed s0, s1, ..., sn-1")
    label1_6 = tk.Label(new_window1, text = "Input form is like:\n a->b 0.5 can, b->c 0.2 cannot \n can means controllable \ncannot means uncontrollable\n 0.5 and 0.2 mean the \ninitial probability of transition")

    def manual_input_gui():
        num = entry1_1.get()
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
        label_graph1.grid(row=6,column= 0,sticky='w')
        label1_7 = tk.Label(new_window1, text="The system image is as follows:").grid(row=5,sticky='w')
        label1_8 = tk.Label(new_window1, text="Select an algorithm:").grid(row=6,column=1)
        
        def b_f():
            res, t = brute_force.brute_force_gui(g1)
            

        def deactivate_all_useless_transitions():
            print("Option 1 selected")
        
        def brute_force_after_DAUT():
            print("Option 1 selected")

        def dijkstra():
            print("Option 1 selected")

        def step_by_step_selection():
            print("Option 1 selected")

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

        cbox = ttk.Combobox(new_window1,values=['Brute force','Deactivate all useless transitions','Brute force after DAUT','Dijkstra','Step_by_step_selection'])
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
    new_window2 = tk.Toplevel(window)
    new_window2.geometry(size_geo)
    labelExample = tk.Label(new_window2, text = "New Window")
    buttonExample = tk.Button(new_window2, text = "New Window button")

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