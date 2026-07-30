#!/usr/bin/env python
# coding: utf-8

# In[22]:


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


# In[30]:


import numpy as np
X=np.array([[1,2],[3,4]])
 
U,S,VT=np.linalg.svd(X)

n_components=2
X_reconstructed=np.dot(U[:,:n_components],np.dot(np.diag(S[:n_components]),VT[:n_components,:]))
print("Original matrix:")
print(X)
print("\nReconstructed Matrix(with reduced dimensions):")
print(X_reconstructed)


# In[57]:


import matplotlib.pyplot as plt
x=[2,3,4,5]
y=[1,3,4,6]
plt.plot(x,y)
plt.title("sales report")
plt.xlabel("sales")
plt.ylabel("time")
plt.legend("profit")


# In[55]:


import matplotlib.pyplot as plt
subjects=["maths","english","science"]
marks=[90,80,85]
plt.bar(subjects,marks)
plt.title("result")
plt.xlabel("subjects")
plt.ylabel("marks")
plt.legend(marks)


# In[40]:



import matplotlib.pyplot as plt
subjects=["maths","english","science"]
marks=[90,80,85]
plt.scatter(subjects,marks)
plt.title("result")
plt.xlabel("subjects")
plt.ylabel("marks")


# In[49]:


#HISTOGRAM
#count
import matplotlib.pyplot as plt
marks=[10,20,20,30,30,30,40]
plt.hist(marks)


# In[72]:


#HISTOGRAM
#count
import matplotlib.pyplot as plt
marks=[10,20,30]
subject=["maths","english","science"]
plt.pie(marks,labels=subject)
plt.legend("profit")

plt.show()


# In[75]:


import matplotlib.pyplot as plt
x=[1,2,6,18]
y=[3,10,12,20]
plt.plot(x,y,'r:o')


# In[85]:


import numpy as np
import matplotlib.pyplot as plt
x=np.array([0,1,2,3])
y=np.array([3,8,1,10])
plt.suptitle("multiple plots")

plt.subplot(1,2,1)
plt.plot(x,y)
plt.title("first plot")

x=np.array([0,1,2,3])
y=np.array([3,8,1,10])
plt.subplot(1,2,2)
plt.plot(x,y)


# In[ ]:




