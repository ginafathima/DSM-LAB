#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from sklearn import datasets,metrics
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

iris=datasets.load_iris()
X=iris.data
y=iris.target

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

dt_classifier=DecisionTreeClassifier(random_state=42)
dt_classifier.fit(X_train,y_train)

y_pred=dt_classifier.predict(X_test)
new=[[10,2,4,7]]
new_pred=dt_classifier.predict(new)
print(iris.target_names[new_pred])

accuracy=accuracy_score(y_test,y_pred)

print(f"Accuracy:{accuracy*100:2f}%")


# In[ ]:





# In[ ]:




