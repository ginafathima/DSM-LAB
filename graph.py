#!/usr/bin/env python
# coding: utf-8

# In[17]:


import numpy  as np
a=np.array([[3,4],[5,7]])
b=np.array([[6,8],[2,9]])
c=a+b
print ("\n Sum \n" ,c)
c=a-b
print ("\n Difference \n" , c)
c=a*b
print ("\n Multiplication \n",c)
print("\n Division \n",a/b)
c=np.dot(a,b)
print (" \n Matrix mul \n",c)
print("\n Transpose \n",np.transpose(a))


# In[22]:


import numpy as np
X=np.array([[1,2],[4,5]])
U,S,VT=np.linalg.svd(X)
n_components=2
X_reconstructed=np.dot(U[:,:n_components],np.dot(np.diag(S[:n_components]),VT[:n_components,:]))
print("Original Matrix:")
print(X)
print("\n Reconstructed Matrix(with reduced dimensions):")
print (X_reconstructed)


# 

# In[27]:


import matplotlib.pyplot as plt
x=[1,7,3,6]
y=[2,4,7,8]
plt.plot(x,y)
plt.title("GINA FATHIMA")
plt.xlabel("size")
plt.ylabel("time")


# In[32]:


import matplotlib.pyplot as plt
sub=["java","python","dbms"]
mark=[90,60,30]
plt.bar(sub,mark)
plt.title("RESULTS")
plt.xlabel("SUBJECTS")
plt.ylabel("MARKS")
plt.scatter(sub,mark)


# In[33]:


import matplotlib.pyplot as plt
sub=["java","python","dbms"]
mark=[90,60,30]
plt.scatter(sub,mark)
plt.title("RESULTS")
plt.xlabel("SUBJECTS")
plt.ylabel("MARKS")


# In[45]:


import matplotlib.pyplot as plt
sub=["java"]
mark=[90,60,10,90,10,10,10,30,30]
plt.hist(mark)
plt.title("RESULTS")
plt.xlabel("SUBJECTS")
plt.ylabel("MARKS")
plt.legend("profit")


# In[50]:


import matplotlib.pyplot as plt
sub=["java","pthon","dbms","networks"]
mark=[90,60,85,30]
plt.pie(mark,labels=sub)
plt.title("RESULTS")


# In[52]:


import matplotlib.pyplot as plt
x=[1,3,2,10]
y=[6,12,18,20]
plt.plot(x,y ,color="red",marker='o',markerfacecolor="blue")
plt.title("PLOTS")
plt.xlabel("size")
plt.ylabel("time")


# In[56]:


import matplotlib.pyplot as plt
x=[1,2,6,18]
y=[3,10,12,20]
plt.plot(x,y ,'r:o')
plt.title("PLOTS")
plt.xlabel("size")
plt.ylabel("time")


# In[ ]:


import matplotlib.pyplot as plt
x=[1,2,6,18]
y=[3,10,12,20]
z=[2,4,6,8,10]
plt.plot(x,y ,'r:o')
plt.title("PLOTS")
plt.xlabel("size")
plt.ylabel("time")

