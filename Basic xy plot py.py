#!/usr/bin/env python
# coding: utf-8

# In[1]:
#install packages
pip install numpy
pip install pandas
pip install matplotlib


# In[2]:

#import packages
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



# In[3]:

#apply variable parameters
x = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
y = [1, 4, 3, 2, 7, 6, 9, 8, 10, 5]

plt.plot(x,y,'b')
plt.xlabel('x')
plt.ylabel('y')
plt.xticks(np.arange(0,51,5))
plt.yticks(np.arange(0,11,1))
plt.show()


# In[ ]:




