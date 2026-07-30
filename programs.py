#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a=int(input("enter a number:"))
b=int(input("enter a number:"))
choice=int(input("enter your choice:\n1.addition\n2.subtraction\n3.division\n4.multiplication\n"))
if choice==1:
    print(a+b)
elif choice==2:
    print(a-b)
elif choice==3:
    if(b==0):
        print("cannot divide")
    else:
        print(a/b)
elif choice==4:
    print(a*b)
else:
    print("invalid choice")
    


# ### 

# In[13]:


a=int(input("enter a number:"))
b=int(input("enter a number:"))
print("a&b",a and b)
print("a|b",a or b)
print("a!b",not b)
print("a>=b",a >= b)



# In[27]:


dict1={"a":"apple","c":"cat"}
dict2={"b":"ball","b":"balloon"}
dict1.update(dict2)
print(dict1)


# In[33]:


num1=int(input("enter a number:"))
num2=int(input("enter a number:"))
num3=int(input("enter a number:"))
if num1>num2 and num1>num3:
    print(num1,"is greater")
elif num2>num3:
    print(num2,"is greater")
else:
    print(num3,"is greater")


# In[45]:


list1=[1,2,3]

list1.append(7)
print(list1)

list1.insert(1,5)
print(list1)

list1.remove(2)
print(list1)

list1.pop()
print(list1)


# In[ ]:




