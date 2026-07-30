#!/usr/bin/env python
# coding: utf-8

# In[9]:


a=int(input("enter first number"))
b=int(input("enter second number"))
ch=int(input("Enter your choice : 1.ADDITION \n 2.SUBTRACTION \n 3.MULTIPLICATION \n 4.DIVISION"))
if (ch==1):

    print("ADDITION:",a+b)

elif(ch==2):

    print("SUBTRACTION:",a-b)

elif (ch==3):

    print("MULTIPLICATION :",a*b)

elif(ch==4):
    if b!=0:
            
    
      print("division:",a/b)
else:
     print("division with 0 not allowed ")

else:

    print("INVALID CHOICE!")


# In[10]:


a=int(input("enter first number"))
b=int(input("enter second number"))
if a>0 and b>0:
    print( " \n both nos are positive")
if a>0 or b>0:
    print("Atleast one no. is positive")
if not a==b:
    print ("both no are not equal")
if a==b:
    print("both nos.are equal")
if a>=b:
    print("First no is greater than or equal to second")
if a<=b:
    print("Second no is greater than or equal to first")
if a!=b:
    print("Both no are not equal")


# In[18]:


dict1={"name":"gina","age":22}
dict2={"nam":"fathima","ag":24}
dict1.update(dict2)
print(dict1)


# In[19]:


1st=[1,2,3,4,5,6,7,8,9]
1st.append(10)
print("Append:" ,1st)
1st.remove(10)
print("Remove:",1st)
1st.insert(13,22)
print("insert:",22)


# In[ ]:




