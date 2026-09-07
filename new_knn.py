#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

data=pd.read_csv("insurance.csv")

X=data.iloc[:,:6]
y=data.iloc[:,-1]

le=LabelEncoder()
categorical_columns=['sex','smoker','region']
for col in categorical_columns:
    X[col]=le.fit_transform(X[col])
y=le.fit_transform(y)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
k=3
knn=KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train,y_train)
y_pred=knn.predict(X_test)
sample=[[1,10,9,11,4,2]]
k=knn.predict(sample)
print(k)
accuracy=accuracy_score(y_test,y_pred)
print(accuracy)


# In[22]:


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

data=pd.read_csv("food.csv")

X=data.iloc[:,:3]
y=data.iloc[:,3]

le=LabelEncoder()
categorical_columns=['Ingredient']
for col in categorical_columns:
    X[col]=le.fit_transform(X[col])
y=le.fit_transform(y)


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
k=3
knn=KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train,y_train)
y_pred=knn.predict(X_test)
sample=[[7,20,3]]
k=knn.predict(sample)
print(k)
accuracy=accuracy_score(y_test,y_pred)
print(accuracy)


# import numpy as np
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.metrics import accuracy_score
# from sklearn.preprocessing import LabelEncoder
# 
# data=pd.read_csv("cricket.csv")
# 
# X=data.iloc[:,:4]
# y=data.iloc[:,-1]
# 
# le=LabelEncoder()
# categorical_columns=['Outlook','Temp','Humidity','Windy']
# for col in categorical_columns:
#     X[col]=le.fit_transform(X[col])
# #y=le.fit_transform(y)
# y=y.str.strip().str.lower()
# y=y.map({'no':0,'yes':1})
# 
# X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
# k=3
# knn=KNeighborsClassifier(n_neighbors=k)
# knn.fit(X_train,y_train)
# y_pred=knn.predict(X_test)
# sample=[[7,20,3,11]]
# k=knn.predict(sample)
# print(k)
# accuracy=accuracy_score(y_test,y_pred)
# print(accuracy)

# In[ ]:




