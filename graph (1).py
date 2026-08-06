#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
print("add=\n",(a+b),"\n")
print("sub=\n",(a-b),"\n")
print("mul=\n",(a*b),"\n")
print("div=\n",(a/b),"\n")
print("matrix multiplication=\n",np.dot(a,b))
print("transpose: \n a=\n",np.transpose(a),"\n")
print("b=\n",np.transpose(b),"\n")


# In[11]:


import numpy as np
X=np.array([[1,2],[3,4]])
 
U,S,VT=np.linalg.svd(X)

n_components=2
X_reconstructed=np.dot(U[:,:n_components],np.dot(np.diag(S[:n_components]),VT[:n_components,:]))
print("Original matrix:")
print(X)
print("\nReconstructed Matrix(with reduced dimensions):")
print(X_reconstructed)


# In[12]:


import matplotlib.pyplot as plt
x=[2,3,4,5]
y=[1,3,4,6]
plt.plot(x,y)
plt.title("sales report")
plt.xlabel("sales")
plt.ylabel("time")
plt.legend("profit")


# In[13]:


import matplotlib.pyplot as plt
subjects=["maths","english","science"]
marks=[90,80,85]
plt.bar(subjects,marks)
plt.title("result")
plt.xlabel("subjects")
plt.ylabel("marks")
plt.legend(marks)


# In[14]:



import matplotlib.pyplot as plt
subjects=["maths","english","science"]
marks=[90,80,85]
plt.scatter(subjects,marks)
plt.title("result")
plt.xlabel("subjects")
plt.ylabel("marks")


# In[15]:


#HISTOGRAM
#count
import matplotlib.pyplot as plt
marks=[10,20,20,30,30,30,40]
plt.hist(marks)


# In[16]:


#HISTOGRAM
#count
import matplotlib.pyplot as plt
marks=[10,20,30]
subject=["maths","english","science"]
plt.pie(marks,labels=subject)
plt.legend("profit")

plt.show()


# In[17]:


import matplotlib.pyplot as plt
x=[1,2,6,18]
y=[3,10,12,20]
plt.plot(x,y,'r:o')


# In[28]:


import numpy as np
import matplotlib.pyplot as plt
x=np.array([0,1,2,3])
y=np.array([3,8,1,10])
plt.suptitle("Sub plots")

plt.subplot(1,2,1)
plt.plot(x,y)
plt.title("first plot")

x=np.array([0,1,2,3])
y=np.array([3,8,1,10])
plt.subplot(1,2,2)
plt.plot(x,y)


# In[29]:


import numpy as np
import matplotlib.pyplot as plt
x=np.array([0,1,2,3])
y=np.array([3,8,1,10])
plt.suptitle("multiple plots")
plt.subplot(1,2,1)
plt.bar(x,y)
plt.title("first plot")

x=np.array([0,1,2,3])
y=np.array([3,8,1,10])
plt.subplot(1,2,2)
plt.scatter(x,y)
plt.title("Second plot")


# In[54]:


import numpy as np
import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[1,4,9,16]
z=[1,1,2,2]
plt.plot(x,y,label="squares")
plt.plot(y,z,label="yz")
plt.plot(x,z,label="xz")

plt.xlabel("x")
plt.ylabel("y")
plt.title("different color lines")
plt.legend()
plt.show


# In[49]:


import matplotlib.pyplot as plt
import numpy as np
men=[22,30,35,35,26]
women=[25,32,30,35,29]

groups=[1,2,3,4,5]

groups=np.arange(5)
plt.bar(groups,men,0.3)
plt.bar(groups+0.3,women,0.3)

plt.xlabel("group")
plt.ylabel("scores")
plt.title("scores by groups & genders")
plt.legend("mw")


# In[71]:


import matplotlib.pyplot as plt
language=["java","python","php","js","c#","c++"]
popularity=[22.2,17.6,8.8,8,7.7,6.7]

plt.subplot(1,3,1)
plt.pie(popularity,labels=language)


plt.subplot(1,3,2)
plt.scatter(language,popularity)

plt.subplot(1,3,3)
plt.barh(language,popularity)
plt.xlabel("popularity")


plt.show()


# In[76]:


import matplotlib.pyplot as plt
language=["java","python","php","js","c#","c++"]
popularity=[22.2,17.6,8.8,8,7.7,6.7]


plt.pie(popularity,labels=language)
plt.show()

plt.scatter(language,popularity)
plt.show()

plt.barh(language,popularity)
plt.xlabel("popularity")
plt.ylabel("languages")
plt.show()


# In[ ]:




