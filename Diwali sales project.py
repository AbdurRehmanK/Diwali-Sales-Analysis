#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as mt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


df = pd.read_csv("D:\ABDUl\Data analysis with python\Python_Diwali_Sales_Analysis-main\Diwali Sales Data.csv",encoding = 'unicode escape')
df


# In[4]:


df.shape


# In[5]:


df.head(20)


# In[6]:


df.info()


# In[7]:


df.drop(['Status','unnamed1'],axis=1,inplace=True)


# In[8]:


df.info()


# In[9]:


pd.isnull(df)


# In[10]:


pd.isnull(df).sum()


# In[11]:


df.dropna(inplace = True)


# In[12]:


pd.isnull(df).sum()


# In[13]:


df['Amount'] = df['Amount'].astype('int')


# In[14]:


df.info()


# In[15]:


df.columns


# In[16]:


df.rename(columns={"Marital_Status":"Shaadi"},inplace=True)
df


# In[17]:


df.describe()


# In[18]:


df[['Age','Orders','Amount']].describe()


# In[19]:


df.columns


# In[20]:


sns.countplot(x='Gender',data = df)


# In[21]:


ax = sns.countplot(x='Gender',data = df)

for bar in ax.containers:
    ax.bar_label(bar)


# In[42]:


df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)


# In[44]:


dp = df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x='Gender',y='Amount',data=dp)


# In[24]:


sx = sns.countplot(x='Age Group',hue='Gender',data=df)

for bars in sx.containers:
    sx.bar_label(bars)


# In[25]:


sales_Age = df.groupby(['Age Group'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)

sns.barplot(x='Age Group',y='Amount',data=sales_Age)


# In[26]:


sales_order = df.groupby(['State'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)
sns.set(rc={'figure.figsize':(15,5)})
val = sns.barplot(x='State',y='Orders',data=sales_order)
for ax in val.containers:
    val.bar_label(ax)


# In[27]:


state_amount=df.groupby(['State'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)
sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(x='State',y='Amount',data=state_amount)


# In[28]:


df.columns


# In[29]:


ax = sns.countplot(x='Shaadi',data=df)
sns.set({'figure.figsize':(7,5)})
for ad in ax.containers:
    ax.bar_label(ad)


# In[30]:


df.rename(columns={'Shaadi':'Martial_Status'},inplace=True)
df


# In[31]:


sales_data = df.groupby(['Martial_Status','Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.set({'figure.figsize':(5,5)})
sns.barplot(x='Martial_Status',y='Amount',data=sales_data,hue="Gender")


# In[32]:


ax = sns.countplot(x='Occupation',data=df)
sns.set({'figure.figsize':(20,5)})
for ad in ax.containers:
    ax.bar_label(ad)


# In[33]:


sales_data = df.groupby(['Occupation'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.set({'figure.figsize':(20,5)})
sns.barplot(data=sales_data,x='Occupation',y='Amount')


# In[34]:


ax = sns.countplot(x='Product_Category',data=df)
sns.set({'figure.figsize':(20,5)})
for ad in ax.containers:
    ax.bar_label(ad)


# In[35]:


sales_data = df.groupby(['Product_Category'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)
sns.set({'figure.figsize':(20,5)})
sns.barplot(data=sales_data,x='Product_Category',y='Amount')


# In[36]:


sales_data = df.groupby(['Product_ID'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)
sns.set({'figure.figsize':(20,5)})
sns.barplot(data=sales_data,x='Product_ID',y='Orders')


# In[37]:


df['Product_Category'].nunique()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




