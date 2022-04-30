#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pandas


# In[2]:


pip install matplotlib.pyplot


# In[3]:


pip install matplotlib


# In[9]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# In[12]:


x = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
y = [1, 4, 3, 2, 7, 6, 9, 8, 10, 5]

plt.plot(x,y,'b')
plt.xlabel('x')
x = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
y = [1, 4, 3, 2, 7, 6, 9, 8, 10, 5]

plt.plot(x,y,'b')
plt.xlabel('x')
plt.ylabel('y')


# In[15]:


plt.plot(x,y,'b')
plt.xlabel('x')
x = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
y = [1, 4, 3, 2, 7, 6, 9, 8, 10, 5]

plt.plot(x,y,'b')
plt.xlabel('x')
plt.ylabel('y')
plt.xticks(np.arange(0,51,5))
plt.yticks(np.arange(0,11,1))
plt.show()


# In[ ]:




