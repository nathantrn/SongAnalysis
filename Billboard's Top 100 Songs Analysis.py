#!/usr/bin/env python
# coding: utf-8

# In[2]:



import pandas as pd
raw_song_table = pd.read_csv('songs_dataset.csv')


# 1. What is the name of the song that has the longest duration in the dataset?

# In[3]:


sorted_by_duration = raw_song_table.sort_values(by = ['duration_ms'], ascending = False)
sorted_by_duration


# 2. What percentage of songs have a duration greater than 3 minutes? Note that the dataset gives duration in terms of milliseconds.

# In[4]:


sorted_by_duration[sorted_by_duration.duration_ms > 180000]


# In[5]:


1861/2000


# 3. What is the name of Katy Perry's least danceable song?

# In[6]:


Katy = raw_song_table.where(raw_song_table.artist == "Katy Perry")
Katy = Katy.dropna()
sorted_Katy_dance = Katy.sort_values(by = ['danceability'])
sorted_Katy_dance


# 4. What artist has the highest number of explicit songs released in the years before and including 2008?

# In[7]:


explicit_songs = raw_song_table.where(raw_song_table.explicit == True).dropna()
sorted_explicit = explicit_songs.sort_values(by = ['year'], ascending = False)
sorted_explicit[sorted_explicit.year < 2009]
sorted_explicit['artist'].value_counts()


# Challenge Questions
# 1. You are a music producer hoping to create the next big hit. You have aligned all the artists, and you know the genre of the song you want to create. You just have one question: should your song be explicit? You know that your mom disapproves of profanity in songs, but it seems like kids these days don't mind. The only thing you have on your mind is business though. Will a song being explicit affect its popularity in the modern streaming ecosystem? What conclusions can you draw from this dataset, and what are the limitations of your thought process?

# In[8]:


sorted_by_year = raw_song_table.sort_values(by = ['year'], ascending = False)
sorted_after_2015 = sorted_by_year[sorted_by_year.year > 2015]
sorted_after_2015


# In[9]:


sorted_by_popular = sorted_after_2015.sort_values(by = ['popularity'], ascending = False) 
sorted_by_popular['explicit'].value_counts()


# In[10]:


159/409


# In[11]:


bottom_popular = sorted_by_popular[sorted_by_popular.popularity < 43]
bottom_popular['explicit'].value_counts()


# In[12]:


20/68


# In[13]:


top_half_popular = sorted_by_popular[sorted_by_popular.popularity > 43]
top_half_popular['explicit'].value_counts()


# In[14]:


139/339


# In[15]:


top_25_popular = sorted_by_popular[sorted_by_popular.popularity > 64]
top_25_popular['explicit'].value_counts()


# In[16]:


118/271


# In[17]:


top_10_popular = sorted_by_popular[sorted_by_popular.popularity > 75]
top_10_popular['explicit'].value_counts()


# In[18]:


57/124


# Yes, your song should be explicit. Since you are concerned with popularity in the modern streaming ecosystem, I first looked at the data from recent years(2015-2020). This data gives us a look at what is popular and unpopular among individuals in the modern age. I then sorted this table of songs by popularity and looked at the ratio of explicit songs to total songs. First, I looked at the total ratio of explicit songs to total songs, then looked at the same ratio in the bottom 50% of popular songs, top 50%, top 25% and top 10%. As the criteria of songs became more popular, the ratio of explicit songs within that population also became consistently higher which demonstrates that there is a positive correlation of a song being explicit and popular among the modern audience. Some limitations of my thought process are that while my analysis focuses on the fact that explicit songs become more prevalent as popularity of songs increase, it ignores the fact that nonexplicit songs maintain the majority in every category of popularity. This fact may be influenced by confounding variables not captured in the data set such as the ratio of songs produced that are explicit compared to nonexplicit. 
# 

# 2. You are put in charge of organizing the 2024 Superbowl Half-Time Show, and you get to choose who gets to perform. You have to present your idea to the board, and if it's a flop, they're going to send the linebackers at you. What single artist would you pick, and why? Which metrics are most important in your decision, and what are potential drawbacks of your methodology? How can you create a good show and save your neck?

# In[19]:


top_25_popular['artist'].value_counts()


# In[24]:


top_energy = top_25_popular.sort_values(by = ['energy'], ascending = False)
top_energy = top_energy[top_energy.energy > .5]
top_dance = top_energy[top_energy.danceability > .65]
top_dance['artist'].value_counts()


# In[21]:


top_25_popular['artist'].value_counts()


# The artist I chose was Drake. What makes Superbowl performances memorable are largely three metrics( Popularity, energy, and danceability). An artist must have multiple songs that are popular for audience to recognize the name and songs. They must have energy to get the crowd excited, pumped, and engaged. Lastly, danceability plays a huge part in making a Superbowl performance memorable as audiences often remember the choreography and theatrics over what actual songs played in the performance. Thus, I took the top 25% of songs by popularity. Then took the songs that had an energy greater than .5 and a danceability greater than a .65. I, then, counted the artists who had the most songs within this tailored group of songs and came with Post Malone and Drake. Because there was a tie, I went back to the top 25% of songs by popularity and counted to see who had the most songs within that population. Drake came out on top of Post Malone demonstrating that Drake would be a more recognizable artist to have on the big stage. 

# In[ ]:




