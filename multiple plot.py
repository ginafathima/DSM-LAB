#!/usr/bin/env python
# coding: utf-8

# In[4]:


import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y1=[2,4,6,8,10]
y2=[1,3,5,7,9]
plt.subplot(1,2,1)
plt.plot(x,y1)
plt.title("FIRST PLOT")

plt.subplot(1,2,2)
plt.plot(x,y2)
plt.title("SECOND PLOT")
plt.show()


# In[3]:


import matplotlib.pyplot as plt
men=[22,30,42,56,35]
women=[25,34,21,48,85]
x=[1,2,3,4,5]
plt.bar(x,men,label="MEN",color="blue",width=0.4)
plt.bar(x,women,label="WOMEN" , color="pink" , width=0.2)
plt.xlabel("Group")
plt.ylabel("Scores")
plt.title("Scores by group and gender")
plt.legend()
plt.show()


# In[1]:


import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y1=[1,4,9,16,25]
y2=[1,8,27,64,125]
y3=[1,30,45,67,100]
plt.plot(x,y1 , label="SQUARE")
plt.plot(x,y2 , label="TRIANGLE")
plt.plot(x,y3 ,label="RECTANGLE",color="green")

plt.xlabel=("X-axis")
plt.ylabel=("Y-axis")
plt.title("MULTIPLE LINES")
plt.legend()
plt.show()


# In[32]:


import matplotlib.pyplot as plt
languages=["java","python","php","javascript","c#","c++"]
popularity=[22.2,17.6,8.8,8,7.7,6.7]
plt.pie(popularity,labels=languages)
plt.title("PIE CHART")
plt.show()


# In[4]:


import matplotlib.pyplot as plt
lang=["java","python","php","dbms","javascript","c++"]
y=[22.2,17.6,8.8,8,7.7,6.7]

plt.scatter(lang,y)
plt.title("SCATTER GRAPH")
plt.show()


# In[1]:


import matplotlib.pyplot as plt
lang=["java","python","php","javascript"]
popularity=[22.2,8,17.4,6.9]
plt.barh(lang,popularity)
plt.grid()
plt.title("HORIZONTAL GRAPH")
plt.show()


# In[ ]:




