from fractions import Fraction
import transitions
class State():
    def __init__(self, key):
        self.key = key
        self.target_states = {}
        # Use dictionary to save transition information, likes{ State: initial_probability(fraction_type)}
        self.transition_num = 0
        self.activated_target_states = {} # { 'b':0.4, 'c':0.2}  0.4/(0.4+0.2)
        self.is_final_state = False
        self.is_initial_state = False
        self.connected_transition_dict = {}  # [Transition a->b : 0.4 ,Transition a->c : 0.2 ,Transition a->d : 0.4]
    
    def add_target_state(self, nbr, ipr):
        self.transition_num += 1
        self.target_states.update({nbr: ipr})
    
    def update_activated_states(self ):
        self.activated_target_states.clear()
        activated_connected_state_list = []
        initial_probability_list = []
        current_probability_list = []
        sum = 0
        for i in self.connected_transition_dict:
            if i.is_activated == True:
                activated_connected_state_list.append(i.target)
                initial_probability_list.append(self.connected_transition_dict[i])
                sum +=  self.connected_transition_dict[i]
        for i in initial_probability_list:
            current_probability_list.append(i/sum)
        for i in range(len(activated_connected_state_list)):
            self.activated_target_states.update({activated_connected_state_list[i]:current_probability_list[i]})
            

    def get_all_transitions_tuple(self):       # Use tuple to save every transition then use list to save them.
        nbrlist = list(self.activated_target_states.keys())
        tranlist = []
        for i in nbrlist:
            tranlist.append((self.key, i.get_id(), self.activated_target_states.get(i)))
        return tranlist

    def get_id(self):
        return self.key      
            
    def get_probability_equation(self):
        if self.is_final_state == False:
            if self.transition_num == 0:
                return self.key +'=='+ str(0)
            else:    
                nbrlist = list(self.activated_target_states.keys())
                tranlist = []
                if len(nbrlist):
                    for i in nbrlist:
                        tranlist.append(i.get_id()+'*'+str(self.activated_target_states.get(i)))
                    add = '+'
                    right_side_of_equation = add.join(tranlist)
                    return self.key +'=='+ right_side_of_equation
        else:
            return self.key +'=='+ str(1)


     