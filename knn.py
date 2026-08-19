#!/usr/bin/env python
# coding: utf-8

# In[26]:


from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
iris=load_iris()
X=iris.data
y=iris.target
print (iris.feature_names)
print(iris.target_names)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train,y_train)
y_predict=knn.predict(X_test)
accuracy=accuracy_score(y_test,y_predict)
print(f'Accuracy={accuracy:.2f}')
print("prediction=",y_predict[0])
new=[[1.1,2.2,3.3,4.4]]
new_predict=knn.predict(new)
print("Target Nmeiris.target_names[new_predict])


# In[33]:


from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
cancer=load_breast_cancer()
X=cancer.data
y=cancer.target
print("Features:",cancer.feature_names)
print("Target:",cancer.target_names)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train,y_train)
y_predict=knn.predict(X_test)
accuracy=accuracy_score(y_test,y_predict)
print(f'Accuracy={accuracy:.2f}')
print("prediction=",y_predict[0])
new = [[14.0, 20.0, 90.0, 600.0, 0.10, 0.10, 0.08, 0.05, 0.18, 0.06,
             0.40, 1.0, 2.5, 30.0, 0.006, 0.02, 0.02, 0.01, 0.02, 0.003,
             16.0, 25.0, 105.0, 800.0, 0.13, 0.25, 0.25, 0.12, 0.30, 0.08]]
new_predict=knn.predict(new)
print("Target Name=" ,cancer.target_names[new_predict])


# In[ ]:





# In[ ]:




