#!/usr/bin/env python
# coding: utf-8

# In[8]:



m = [[1,2],[3,4],[5,6]] 
for row in m : 
    rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))] 
for row in rez: 
    print(row) 

