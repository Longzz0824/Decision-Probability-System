from fractions import Fraction

class Transition():
    
    def __init__(self,s1, s2, ipr, ability):
        self.key = s1.get_id() +'->'+ s2.get_id()
        self.source = s1
        self.target = s2
        self.initial_probability = ipr
        self.current_probability = ipr
        self.is_activated = True
        self.is_deactivated = False
        if ability == 'can':
            self.can_be_deactivated = True
        elif ability == 'cannot':
            self.can_be_deactivated = False


    
    def activate(self):
        if(self.is_activated == False):
            self.is_activated = True
            self.is_deactivated = False

    def deactivate(self):
        if(self.is_deactivated == False and self.can_be_deactivated == True): 
            self.is_deactivated = True
            self.is_activated = False
            self.current_probability = 0


#    def get_trans_dic(self):
#        if self.isActivated == True:
#            return 

 #       return (self.fromstate, self.tostate)
    
    def get_trans_name(self):
        return (self.key)

#def getProbabilityEquation(self):
        