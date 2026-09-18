#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from sklearn import datasets,metrics
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

iris=datasets.load_iris()
X=iris.data
y=iris.target
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

nb_classifier=GaussianNB()
nb_classifier.fit(X_train,y_train)

y_pred = nb_classifier.predict(X_test)

sample = [[10,2,9,7]]
sample_pred=nb_classifier.predict(sample)
print(iris.target_names[sample_pred])

accuracy = accuracy_score(y_test,y_pred)
print (accuracy)
print(f"Accuracy:{accuracy*100:.2f}%")


# In[2]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import CategoricalNB
from sklearn.metrics import accuracy_score
df=pd.read_csv("cricket.csv")

df["Play Cricket"]=df["Play Cricket"].map({"No":0, "Yes":1})

categorical_columns=["Outlook","Temperature","Humidity","Wind"]
for col in categorical_columns:
    df[col]=df[col].astype("category").cat.codes
    
X=df[categorical_columns]
y=df["Play ricket"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

nb_classifier=CategoricalNB()
nb_classifier.fit(X_train,y_train)

y_pred=nb_classifier.predict(X_test)
accuracy=accuracy_score(y_test,y_pred)

print("Predicted values:",y_pred)
print(f"Accuracy:{accuracy*100:.2f}%")


# In[ ]:





# In[ ]:




