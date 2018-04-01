# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


class EpisolonGreedy():
    def _init_ (self , epsilon , counts , values):
        self.epsilon = epsilon
        self.counts = counts
        self.values = values 
        return 
        
    def initiliaze(self , n_arms):
        self.counts = [0 for col in range(n_arms)]
        self.values = [0.0 for col in range(n_arms)]               
        return

               
                       
        
    
    