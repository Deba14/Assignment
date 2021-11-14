#!/usr/bin/env python
# coding: utf-8

# In[1]:


b=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
lenb=len(b)
for i in range(0,lenb):
    for j in range(0,lenb-i-1):
        if b[j][-1]>b[j+1][-1]:
            swap=b[j]
            b[j]=b[j+1]
            b[j+1]=swap
print(b)


# In[ ]:




