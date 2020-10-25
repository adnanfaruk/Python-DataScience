#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


tips=sns.load_dataset('tips')


# In[3]:


tips.head()


# In[4]:


sns.distplot(tips['total_bill'],kde=False,bins=100)


# In[5]:


sns.jointplot(x='total_bill',y='tip',data=tips,kind='hex')


# In[6]:


sns.jointplot(x='total_bill',y='tip',data=tips,kind='reg')


# In[7]:


sns.jointplot(x='total_bill',y='tip',data=tips,kind='kde')


# In[8]:


sns.pairplot(tips,hue='sex',palette='coolwarm')


# In[9]:


sns.rugplot(tips['total_bill'])


# In[10]:


# Keine Sorge, ihr müsst diesen Code nicht verstehen!
# Er soll nur das nachfolgende Diagramm erzeugen
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

#Datensatz erstellen
dataset = np.random.randn(25)

# Ein weiteres rugplot erstellen
sns.rugplot(dataset);

# Die x-Achse des Plot einstellen
x_min = dataset.min() - 2
x_max = dataset.max() + 2

# 100 gleich verteilte Punkte von x_min bis x_max
x_axis = np.linspace(x_min,x_max,100)

# Die Bandbreite (en.: bandwidth) einstellen. Mehr Infos zur Bandbreite:
url = 'https://de.wikipedia.org/wiki/Kerndichtesch%C3%A4tzer#Satz_von_Nadaraya'

bandwidth = ((4*dataset.std()**5)/(3*len(dataset)))**.2


# Eine leere Liste erstellen
kernel_list = []

# Jede Funktion visualisieren
for data_point in dataset:
    
    # Für jeden Punkt wird ein Kernel erstellt und der Liste angefügt
    kernel = stats.norm(data_point,bandwidth).pdf(x_axis)
    kernel_list.append(kernel)
    
    # Skalieren für die Darstellung
    kernel = kernel / kernel.max()
    kernel = kernel * .4
    plt.plot(x_axis,kernel,color = 'grey',alpha=0.5)

plt.ylim(0,1)


# In[11]:


# Um das KDE-Plot zu erhalten können wir diese Funktionen summieren.

# Zeiche die Summe der Basisfunktionen
sum_of_kde = np.sum(kernel_list,axis=0)

# Diagramm zeigen
fig = plt.plot(x_axis,sum_of_kde,color='indianred')

# Das erste rugplot hinzufügen
sns.rugplot(dataset,c = 'indianred')

# Die y-tick-Markierungen entfernen
plt.yticks([])

# Titel definieren
plt.suptitle("Summe der Basisfunktionen")


# In[12]:


sns.kdeplot(tips['total_bill'])
sns.rugplot(tips['total_bill'])


# In[13]:


sns.kdeplot(tips['tip'])
sns.rugplot(tips['tip'])


# In[14]:


tips.head()


# In[15]:


sns.barplot(x='sex',y='total_bill',data=tips,estimator=np.std)


# In[16]:


sns.countplot(x='sex',data=tips)


# In[23]:


sns.boxplot(x='day',y='total_bill',data=tips,palette='rainbow')


# In[25]:


sns.boxplot(data=tips,palette='rainbow',orient='h')


# In[26]:


sns.boxplot(x='day',y='total_bill',hue='smoker',data=tips,palette='rainbow')


# In[27]:


sns.violinplot(x='day',y='total_bill',data=tips,palette='rainbow')


# In[29]:


sns.violinplot(x='day',y='total_bill',data=tips,hue='sex',palette='rainbow')


# In[30]:


sns.violinplot(x='day',y='total_bill',data=tips,hue='sex',split=True,palette='rainbow')


# In[39]:


sns.stripplot(x='day',y='total_bill',data=tips,jitter=True,hue='sex',palette='Set1',dodge=True)


# In[41]:


sns.swarmplot(x='day',y='total_bill',data=tips,hue='sex',palette='Set1')


# In[46]:


sns.violinplot(x='tip',y='day',data=tips,platte='rainbow')
sns.swarmplot(x='tip',y='day',data=tips,color='black',size=3)


# In[51]:


sns.factorplot(x='sex',y='total_bill',data=tips)


# In[ ]:




