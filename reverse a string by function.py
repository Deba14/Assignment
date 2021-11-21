#!/usr/bin/env python
# coding: utf-8

# In[4]:


def reverse(string):
    for i in range(len(string)-1,-1,-1):
        print(string[i],end="")
reverse("1234abcd")
        


# In[5]:


def reverse2(string):
    print("the reversed string is :",string[len(string)-1::-1])
reverse2("1234abcd")

