#!/usr/bin/env python
# coding: utf-8

# In[4]:


# qst 1
import numpy as np
array = np.array([[1,2],[3,4]])
array = array.tolist()
print(array)


# In[1]:


# qst 2
import numpy as np
  
n_array = np.array([[2, 5, 1],
                    [0, 4, 12],
                    [21, 4, 7]])
  
print("Numpy Matrix is:")
print(n_array)
  
# trace = calcul diagonale
trace = np.trace(n_array)
  
  
print("\nTrace of given 3X3 matrix:")
print(trace)


# In[2]:


# qst 3
x = np.array([[1,2],[3,5]])
print("Values bigger than 3 =", x[x>3])


# In[3]:


# qst 4
import numpy as np
A = np.array([2, 5, 9])
B = np.array([2, 9, 1])
C = np.empty((0,2), int)
for x in range(3):
    C = np.append(C,np.array([[A[x]+B[x]]]))
print(C)


# In[4]:


# qst 5
import numpy as np
print("Original matrix:\n")
X = np.random.rand(1, 2)
print(X)
print("\nSubtract the mean of each row of the said matrix:\n")
Y = X - X.mean(axis=1, keepdims=True)
print(Y)


# In[ ]:




