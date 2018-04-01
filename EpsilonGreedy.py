# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


class EpisolonGreedy():
    " counts : a vector of length N , # of times we have played each of the N arms
    " epsilon : probability of exploring 
    " values : a vector of length N storing the avg. rewards for each of the N arms 
    def _init_ (self , epsilon , counts , values):  
        self.epsilon = epsilon                      
        self.counts = counts
        self.values = values 
        return 
        
    def initiliaze(self , n_arms):                    
        " initialize the class counts and values when there is a need
        " to start from a clean slate. 
        self.counts = [0 for col in range(n_arms)]    
        self.values = [0.0 for col in range(n_arms)]               
        return

    def ind_max(x):
        "returns the arm that gives the hightest reward. Exploitation
        m = max(x)
        return x.index(m)
                       
    def select_arm(self):
        if random.random() > self.epsilon: 
            return ind_max(sel.values)
        else:
            return random.randrange(len(self.values))
        
        
    def update(self , chosen_arm , reward):
        "self : ctor of EpsilonGrredy object we are walready working with 
        " chosen_arm : Arm that is currently run 
        " reward : reward assicated with the chosen arm 
        " objective to update self.values indexed on the chosen arm with the new values after the current run
        " note we are using weighted average here but it can ve anything that is useful in the context of the problem 
        self.counts[chosen_arm] = self.counts[chosen_arm] + 1 "update iter to accoutn for current run 
        n = self.counts[chosen_arm] 
        value = self.values[chosen_arm]
        new_value = ((n - 1) / float(n)) * value + (1 / float(n)) * reward 
        self.values[chosen_arm] = new_value
        return
        
    