#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Write a Python program to triple all numbers of a given list of integers. Use Python map.



sample list: [1, 2, 3, 4, 5, 6, 7]



Triple of list numbers:

[3, 6, 9, 12, 15, 18, 21]


# In[1]:


def triple_num(x):
    return x*3


# In[2]:


sample_list = [1, 2, 3, 4, 5, 6, 7]
print(list(map(triple_num,sample_list)))


# In[ ]:




