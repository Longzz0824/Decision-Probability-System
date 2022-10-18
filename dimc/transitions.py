import state
from fractions import Fraction

class Transition():
    
    def __init__(self,s1:state.State, s2:state.State):
        self.key = s1.get_id() +'->'+ s2.get_id()
        self.source = s1
        self.target = s2
        self.is_activated = True
        self.is_deactivated = False
    
    def activate(self):
        if(self.is_activated == False):
            self.is_activated = True
            self.is_deactivated = False
            self.source.add_target_state(self.target)

    def deactivate(self):
        if(self.is_deactivated == False): 
            self.is_deactivated = True
            self.is_activated = False
            self.source.transition_num -= 1
            self.source.target_states.pop(self.target)

#    def get_trans_dic(self):
#        if self.isActivated == True:
#            return 

 #       return (self.fromstate, self.tostate)
    
    def get_trans_name(self):
        return (self.key)

#def getProbabilityEquation(self):
        