#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Write a Python program to square the elements of a list using map() function.



Sample List: [4, 5, 2, 9]

Square the elements of the list:

[16, 25, 4, 81]


# In[1]:


def sqrr(x):
    return x**2


# In[2]:


sample_list = [4, 5, 2, 9]
print(list(map(sqrr,sample_list)))


# In[ ]:




