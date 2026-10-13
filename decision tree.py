#!/usr/bin/env python
# coding: utf-8

# In[3]:


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

print(f"Accuracy:{accuracy*100:.2f}%")


# In[8]:


##########     FOOD     #####

import pandas as pd
from sklearn import datasets,metrics
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

data=pd.read_csv("food.csv")

X=data.drop("FoodType",axis=1)
y=data["FoodType"]

le=LabelEncoder()

categorical_columns=["Ingredient","Sweetness","Crunchiness"]
for col in categorical_columns:
    X[col]=le.fit_transform(X[col])
y=le.fit_transform(y)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

dt_classifier=DecisionTreeClassifier(random_state=42)
dt_classifier.fit(X_train,y_train)

y_pred=dt_classifier.predict(X_test)



print("predicted",y_pred)


accuracy=accuracy_score(y_test,y_pred)

print(f"Accuracy:{accuracy*100:.2f}%")


# In[11]:


##########     FOOD     #####

import pandas as pd
from sklearn import datasets,metrics
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

data=pd.read_csv("food.csv")

X=data.drop("FoodType",axis=1)
y=data["FoodType"]

le=LabelEncoder()

categorical_columns=["Ingredient","Sweetness","Crunchiness"]
for col in categorical_columns:
    X[col]=le.fit_transform(X[col])
y=le.fit_transform(y)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

dt_classifier=DecisionTreeClassifier(random_state=42)
dt_classifier.fit(X_train,y_train)

y_pred=dt_classifier.predict(X_test)

new=[[4,10,9,]]
new_pred=dt_classifier.predict(new)

print(new_pred)

accuracy=accuracy_score(y_test,y_pred)

print(f"Accuracy:{accuracy*100:.2f}%")


# In[9]:


import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.metrics import accuracy_score
from sklearn import tree

data=load_iris()
X=data.data
y=data.target
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)
dt_model=DecisionTreeClassifier()
dt_model.fit(X_train, y_train)
plt.figure(figsize=(12, 8))
tree.plot_tree(dt_model,fontsize=10)
y_pred = dt_model.predict(X_test)
accuracy = accuracy_score(y_test,y_pred)
print(f'accuracy of decision tree model:{accuracy:2f}')


# In[ ]:




