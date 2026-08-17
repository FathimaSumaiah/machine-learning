#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
dict={"roll":[1,2,3],"name":['summi','nishba','diya']}

a=pd.DataFrame(dict)
print(a)


# In[16]:


import pandas as pd
dict={"roll":[1,2,3],"name":['summi','nishba','diya']}

a=pd.DataFrame(dict)
print(a.loc[0:])

print(a.loc[0])#first only


# In[7]:


list=[1,2,3,4]
list2=pd.Series(list)
print(list2)


# In[10]:


list=[1,2,3,4]
list2=pd.Series(list,index=["w","x","y","z"])
print(list2)


# In[33]:


import pandas as pd
a=pd.read_csv('students.csv')
print(a,"\n")


print("head:\n\n",a.head(2))
print("tail:\n\n",a.tail(2))




# In[35]:


import pandas as pd
a=pd.read_csv('students.csv')


b=a.dropna()
print(b)


# In[ ]:


import pandas as pd
a=pd.read_csv('students.csv')


b=a.fillna(inplace=)
print(b)

