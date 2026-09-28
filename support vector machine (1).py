#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics
iris=load_iris()
X,y=iris.data,iris.target
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=0)
clf=svm.SVC(kernel="linear")
clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)
print("Accuracy:",metrics.accuracy_score(y_test,y_pred))
print("Precision:",metrics.precision_score(y_test,y_pred,average='micro'))
print("Recall:",metrics.recall_score(y_test,y_pred,average='micro'))


# In[10]:


import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
data=load_iris()

X=data.data
y=data.target
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=0)
svm_model=SVC(kernel="linear")
svm_model.fit(X_train,y_train)
y_pred=svm_model.predict(X_test)
accuracy=accuracy_score(y_test,y_pred)
print(f'Accuracy of SVM:{accuracy:.2f}')


# In[14]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder


data=pd.read_csv("food.csv")
le=LabelEncoder()
for column in data.columns:
    if data[column].dtype=='object':
        data[column]=le.fit_transform(data[column])

X=data.drop("FoodType",axis=1)
y=data["FoodType"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=0)

svm_model=SVC(kernel="linear")
svm_model.fit(X_train,y_train)
y_pred=svm_model.predict(X_test)
accuracy=accuracy_score(y_test,y_pred)

print("Accuracy:",metrics.accuracy_score(y_test,y_pred))
print("Precision:",metrics.precision_score(y_test,y_pred,average='micro'))
print("Recall:",metrics.recall_score(y_test,y_pred,average='micro'))


# In[ ]:




