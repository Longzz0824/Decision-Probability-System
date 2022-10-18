from fractions import Fraction

class State():
    def __init__(self, key):
        self.key = key
        self.target_states = {}
        # Use dictionary to save transition information, likes{ State: Probability}
        self.transition_num = 0
        self.is_final_state = False
        self.is_initial_state = False
    
    def add_target_state(self, nbr):
        self.transition_num += 1
        self.target_states.update({nbr: Fraction(1,self.transition_num)})
    
    def __str__(self):
        return str(self.key) + '-->' + str([nbr.key for nbr in self.target_states])

    def get_out_transitions(self):       # Use tuple to save every transition then use list to save them.
        nbrlist = list(self.target_states.keys())
        tranlist = []
        for i in nbrlist:
            tranlist.append((self.key, i.get_id(), Fraction(1,self.transition_num)))
        return tranlist

    def get_id(self):
        return self.key
    
    def get_probability_equation(self):
        if self.is_final_state == False:
            if self.transition_num == 0:
                return self.key +'=='+ str(0)
            else:    
                nbrlist = list(self.target_states.keys())
                tranlist = []
                if len(nbrlist):
                    for i in nbrlist:
                        tranlist.append(i.get_id()+'*'+str(Fraction(1,self.transition_num)))
                    add = '+'
                    rExpr = add.join(tranlist)
                    return self.key +'=='+ rExpr
        else:
            return self.key +'=='+ str(1)


    