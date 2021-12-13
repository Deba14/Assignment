#!/usr/bin/env python
# coding: utf-8

# In[3]:


'''
Write a Python class to implement pow(x, n)



Explanation:

Use should be able to find the nth power of the x.(i.e x*x*x*x...n times)

You must implement it using Class
'''




x=int(input())
n=int(input())
class pow:
    def __init__(self,x,n):
        self.x=x
        self.n=n
    def power(self):
        result=x**n
        return result
the_given_num=pow(x,n)
result1=the_given_num.power()
print("the result is :",result1)


# In[ ]:




