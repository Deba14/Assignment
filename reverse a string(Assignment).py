#!/usr/bin/env python
# coding: utf-8

# In[6]:


word = str(input("Enter a word : "))
for i in range(len(word)-1,-1,-1):
    print(word[i],end="")


# In[3]:


Char = str(input("Enter a word: "))
v=slice(None,None,-1)
print(Char[v])


# In[7]:


x="deba"
print("result :",x[5::-1])


# In[8]:


char_name=str(input("Enter a word :"))
print("Reversed word" ,char_name[len(char_name)+1::-1])


# In[ ]:




