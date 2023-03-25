from fractions import Fraction

class Transition():
    
    def __init__(self,s1, s2, ability):
        self.key = s1.get_id() +'->'+ s2.get_id()
        self.source = s1
        self.target = s2
        self.is_activated = True
        self.is_deactivated = False
        if ability == 'can':
            self.controllable = True
        elif ability == 'cannot':
            self.controllable = False


    
    def activate(self):
        if(self.is_activated == False):
            self.is_activated = True
            self.is_deactivated = False

    def deactivate(self):
        if(self.is_deactivated == False and self.controllable == True): 
            self.is_deactivated = True
            self.is_activated = False




 #       return (self.fromstate, self.tostate)
    
    def get_trans_name(self):
        return (self.key)

#def getProbabilityEquation(self):
        