#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 15:18:12 2020

@author: clark
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, hist
from numpy.random import choice, randint

electoral_dict = {}
states = ['AL','AK','AZ','AR','CA','CO','CT','DC','DE','FL','GA','HI','ID','IL','IN',
          'IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV',
          'NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN',
          'TX','UT','VT','VA','WA','WV','WI','WY']

votes = [9,3,11,6,55,9,7,3,3,29,16,4,4,20,11,6,6,8,8,4,10,11,16,10,6,10,3,5,6,
         4,14,5,29,15,3,18,7,7,20,4,9,3,11,38,6,3,13,12,5,10,3]

probabilities = [[.5,.5 ]]*51


for k in range(len(states)):
    electoral_dict[states[k]] = (votes[k], probabilities[k])
    

def compute_probabilities(dictionary):
    #Here we need to do most of the work explaining how we get the likelihood
    # of each state's probability of voting one way or the other
    for key in dictionary.keys():
        r_pts = randint(1,10)# this is where the work is
        d_pts = randint(1,11)
        total_pts = r_pts+d_pts
        dictionary[key][1][0] = d_pts/total_pts
        dictionary[key][1][1] = r_pts/total_pts
        del r_pts, d_pts
    return dictionary

    
    
def simulate_election(dictionary):
    D = 0
    R = 0
    for key in dictionary.keys():
        elected = choice(['D','R'], p = dictionary[key][1])
        if elected == 'D':
            D += dictionary[key][0]
        else:
            R += dictionary[key][0]
    return D,R        
    
    
def many_votes(dictionary, num_votes):
     num_D_wins = 0
     num_R_wins = 0
     draws = 0
     for k in range(num_votes):
         D,R = simulate_election(compute_probabilities(dictionary))
         if D > R:
             num_D_wins += 1
         elif R > D:
             num_R_wins += 1
         else:
             draws += 1    
     return num_D_wins, num_R_wins, draws
        
    
    