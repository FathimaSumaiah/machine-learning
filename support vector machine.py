#!/usr/bin/env python
# coding: utf-8

# In[5]:


#---------------------  LINEAR KERNEL    -------------


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


# In[16]:


# ---------------   POLYNOMIAL KERNEL ----------------
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

data=load_iris()

X=data.data[:,:2]
y=data.target
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
svm_model=SVC(kernel='poly')
svm_model.fit(X_train,y_train)
y_pred=svm_model.predict(X_test)
accuracy=accuracy_score(y_test,y_pred)
print(f'accuracy of SVM with polynomial kernel:{accuracy:.2f}')

x_min,x_max=X[:,0].min()-1,X[:,0].max()+1
y_min,y_max=X[:,1].min()-1,X[:,1].max()+1
xx,yy=np.meshgrid(np.arange(x_min,x_max,0.01),np.arange(y_min,y_max,0.01))
Z=svm_model.predict(np.c_[xx.ravel(),yy.ravel()]).reshape(xx.shape)
plt.figure(figsize=(8,6))
plt.contourf(xx,yy,Z,alpha=0.8,cmap="coolwarm")
plt.scatter(X_test[:,0],X_test[:,1],c=y_test,marker='x',label='Test')

plt.title('SVM Decision Boundary with Polynomial Kernel')
plt.xlabel(data.feature_names[0])
plt.ylabel(data.feature_names[1])
plt.legend()
plt.show()


# In[ ]:




