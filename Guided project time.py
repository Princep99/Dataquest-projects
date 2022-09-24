#!/usr/bin/env python
# coding: utf-8

# ## Hacker News
# The study aims to compare two types of posts in order to determine if Ask HN and Show HN receive more comments on average and posts created at a certain time receive more comments on average
# 
# 

# In[3]:


from csv import reader 
open_file=open("hacker_news.csv")
file=reader(open_file)
hn=list(file)
hn[0:4]


# In[4]:


headers=hn[0]
del hn[0]
print(headers)
print(hn[0:4])


# In[5]:


ask_posts=[]
show_posts=[]
other_posts=[]
for i in hn:
    title=i[1]
    title= title.lower()
    if title.startswith("ask hn"):
        ask_posts.append(i)
    elif  title.startswith("show hn"):
        show_posts.append(i)
    else:
         other_posts.append(i)
print(len(ask_posts))
print(len(show_posts))
print(len(other_posts))
ask_posts[0:4]


# In[6]:


total_ask_comments=0
for i in ask_posts:
    num_comments=i[4]
    num_comments=int(num_comments)
    total_ask_comments= total_ask_comments+num_comments 
avg_ask_comments=total_ask_comments/len(ask_posts) 
print(avg_ask_comments)


# In[7]:


total_show_comments=0
for i in show_posts:
    num_comments=i[4]
    num_comments=int(num_comments)
    total_show_comments= total_show_comments+num_comments 
avg_show_comments=total_show_comments/len(show_posts) 
print(avg_show_comments)


# The ask posts receive more comments on average. In particular, 4 more than show comments.

# In[8]:


import datetime as dt 
result_list=[]
for i in ask_posts:
    created_at=i[6]
    num_comments= int(i[4])
    result_list.append([created_at, num_comments])
    
counts_by_hour={}
comments_by_hour={}
date_format="%m/%d/%Y %H:%M"

for i in result_list:
    hour=i[0]
    comm=i[1]
    d_ob=dt.datetime.strptime(hour,date_format).strftime("%H")
    if d_ob not in counts_by_hour:
        counts_by_hour[d_ob]=1
        comments_by_hour[d_ob]=comm
    else:
        counts_by_hour[d_ob]+=1
        comments_by_hour[d_ob]+=comm
comments_by_hour


# In[9]:


result_list[0:4]


# In[16]:


avg_by_hour=[]
for i in comments_by_hour:
    avg_by_hour.append([i, comments_by_hour[i]/counts_by_hour[i]])
avg_by_hour    


# In[17]:


swap_avg_by_hour=[]
for i in avg_by_hour:
    swap_avg_by_hour.append([i[1],i[0]])
print(swap_avg_by_hour )


# In[18]:


sorted_swap= sorted(swap_avg_by_hour, reverse=True )


# In[22]:


print("Top 5 Hours for Ask Posts Comments")
for avg,i in sorted_swap[0:5]:
    print("{}:{:.2f} average comments per post".format(
    dt.datetime.strptime(i,"%H").strftime("%H:%M"),avg))


# The highest number of comments is during the afternoon, at 15:00 it reaches the peak. 
