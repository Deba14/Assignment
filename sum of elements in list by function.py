#!/usr/bin/env python
# coding: utf-8

# In[8]:


def sum_of_members(*x):
    return sum(x)
sum_of_members(8, 2, 3, 0, 7)


# In[9]:


def sum_of_mem(*x):
    total=0
    for i in x:
        total=total+i
    return total
sum_of_mem(8, 2, 3, 0, 7)


# In[ ]:




