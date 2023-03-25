from fractions import Fraction
import transitions
class State():
    def __init__(self, key):
        self.key = key
        self.in_transitions = []
        self.out_transitions = []
        self.out_states = []
        self.transition_as_source_num = 0
        self.all_connected_transition_dict = {}  # [Transition a->b : 0.4 ,Transition a->c : 0.2 ,Transition a->d : 0.4]
        self.current_activated_target_states = {} # { 'b':0.4, 'c':0.2}  0.4/(0.4+0.2)
        self.current_transitions_as_source = {}
        self.is_final_state = False
        self.is_initial_state = False
    
    
    def transition_num_count(self):
        self.transition_as_source_num += 1

        #self.out_transitions.append(self.key + '->' + )
    
        

    def update_activated_states(self):
        self.current_activated_target_states.clear()
        activated_connected_state_list = []
        initial_probability_list = []
        current_probability_list = []
        activated_transition_list = []
        sum = 0
        for i in self.all_connected_transition_dict:
            if i.is_activated == True:
                activated_connected_state_list.append(i.target)
                initial_probability_list.append(self.all_connected_transition_dict[i])
                sum +=  self.all_connected_transition_dict[i]
                activated_transition_list.append(i)
            else:
                self.current_transitions_as_source.update({i.key:0})
        for i in initial_probability_list:
            current_probability_list.append(i/sum)

        for i in range(len(activated_connected_state_list)):
            self.current_activated_target_states.update({activated_connected_state_list[i]:current_probability_list[i]})
            activated_transition_list[i].current_probability = current_probability_list[i]
            self.current_transitions_as_source.update({activated_transition_list[i].key:current_probability_list[i]})
            

    def get_all_transitions_tuple(self):       # Use tuple to save every transition then use list to save them.
        nbrlist = list(self.current_activated_target_states.keys())
        tranlist = []
        for i in nbrlist:
            tranlist.append((self.key, i.get_id(), self.current_activated_target_states.get(i)))
        return tranlist

    def get_id(self):
        return self.key      
            
    def get_probability_equation(self):
        if self.is_final_state == False:
            if self.transition_as_source_num == 0:
                return self.key +'=='+ str(0)
            else:    
                nbrlist = list(self.current_activated_target_states.keys())
                tranlist = []
                if len(nbrlist):
                    for i in nbrlist:
                        tranlist.append(i.get_id()+'*'+str(self.current_activated_target_states.get(i)))
                    add = '+'
                    right_side_of_equation = add.join(tranlist)
                    return self.key +'=='+ right_side_of_equation
                else:
                    return self.key +'=='+ str(0)
        else:
            return self.key +'=='+ str(1)


     