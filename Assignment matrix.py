#!/usr/bin/env python
# coding: utf-8
program in Python to transpose a 2D matrix

# In[16]:



matrix= [[1,2],[3,4],[5,6]]  
rez = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))] 
for row in rez: 
    print(row) 


# In[ ]:




