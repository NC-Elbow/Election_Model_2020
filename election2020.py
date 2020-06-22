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

electoral_dict = {}
states = ['AL','AK','AZ','AR','CA','CO','CT','DC','DE','FL','GA','HI','ID','IL','IN',
          'IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV',
          'NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN',
          'TX','UT','VT','VA','WA','WV','WI','WY']

votes = [9,3,11,6,55,9,7,3,3,29,16,4,4,20,11,6,6,8,8,4,10,11,16,10,6,10,3,5,6,
         4,14,5,29,15,3,18,7,7,20,4,9,3,11,38,6,3,13,12,5,10,3]


for k in range(len(states)):
    electoral_dict[states[k]] = votes[k]
    