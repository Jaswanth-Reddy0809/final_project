#!/usr/bin/env python
# coding: utf-8

# In[218]:


#program for analysis of elections in India
#programmed by Jaswanth Reddy Tanamala
#email:JaswanthReddy.Tanamala@chubb.com
# Date : 04-Mar-2021
# Language : Python3.9.1
# Console:Jupyter notebook


# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
import plotly.graph_objects as go


# In[219]:


ge14=pd.read_csv(r"C:\Users\jatanam\Data Analytics Project-2/GE_india_2014_results.csv")
ge14.head()
ge14.isnull().sum()


# In[220]:


ge19=pd.read_csv(r"C:\Users\jatanam\Data Analytics Project-2/GE_india_2019_results.csv")
ge19.head()
ge19.isnull().sum()
ge19['migrant_votes'].fillna(0,inplace=True)
ge19.isnull().sum()


# In[221]:


NE=pd.read_csv(r"C:\Users\jatanam\Data Analytics Project-2/indian-national-level-election-data-1977-2015.csv")
NE.head()
NE[NE['pc_type'].isnull()].head()


# In[222]:


LS_1=pd.read_csv(r"C:\Users\jatanam\Data Analytics Project-2/LokSabha2004-2019.csv")
LS_1.head()
LS_1.isnull().sum()
LS_1['Total Assets'].fillna(0,inplace=True)
LS_1.isnull().sum()
LS_1.head()


# In[223]:


LS_candidates=pd.read_csv(r"C:\Users\jatanam\Data Analytics Project-2/lok-sabha-candidate-details-2019.csv")
LS_candidates.head()
LS_candidates['SYMBOL'].fillna('NO SYMBOL',inplace=True)
LS_candidates['GENDER'].fillna('NO GENDER',inplace=True)
LS_candidates['AGE'].fillna(0,inplace=True)
LS_candidates['CATEGORY'].fillna('NO CATEGORY',inplace=True)
LS_candidates['ASSETS'].fillna(0,inplace=True)
LS_candidates['EDUCATION'].fillna('NO EDUCATION',inplace=True)
LS_candidates['LIABILITIES'].fillna(0,inplace=True)
LS_candidates['CRIMINAL\nCASES'].fillna(0,inplace=True)
LS_candidates.isnull().sum()
LS_candidates[LS_candidates['NAME']=='NOTA'].head()
LS_candidates.head()


# In[ ]:





# In[224]:


ge14['evm_after_log']=np.log(np.array(ge14['evm_votes'])+1)
ge14['postal_after_log']=np.log(np.array(ge14['postal_votes'])+1)
ge14['total_after_log']=np.log(np.array(ge14['total_votes'])+1)
ge14.head()


# In[225]:


ge19['evm_after_log']=np.log(np.array(ge19['evm_votes'])+1)
ge19['postal_after_log']=np.log(np.array(ge19['postal_votes'])+1)
ge19['total_after_log']=np.log(np.array(ge19['total_votes'])+1)
ge19.head()


# In[226]:


NE['pc_type'].mode()[0]


# In[227]:


NE.dropna(how='any',inplace=True)
NE.isnull().sum()


# In[228]:


NE['totvot_log']=np.log(np.array(NE['totvotpoll'])+1)
NE['electors_log']=np.log(np.array(NE['electors'])+1)
NE.head()


# In[229]:


LS_1.isnull().sum()


# In[230]:


LS_1['Total Assets_log']=np.log(np.array(LS_1['Total Assets'])+1)
LS_1['Liabilities_log']=np.log(np.array(LS_1['Liabilities'])+1)
LS_1.head()


# In[444]:


LS_candidates['GENERAL_VOTES_log']=np.log(np.array(LS_candidates['GENERAL\nVOTES'])+1)
LS_candidates['POSTAL_VOTES_log']=np.log(np.array(LS_candidates['POSTAL\nVOTES'])+1)
LS_candidates['TOTAL_VOTES_log']=np.log(np.array(LS_candidates['TOTAL\nVOTES'])+1)
LS_candidates['TOTAL ELECTORS_log']=np.log(np.array(LS_candidates['TOTAL ELECTORS'])+1)
LS_candidates.head()
LS_candidates['CRIMINAL\nCASES'] = LS_candidates['CRIMINAL\nCASES'].replace(['Not Available'],'0')
LS_candidates['EDUCATION'] = LS_candidates['EDUCATION'].replace(['Not Available'],'NO EDUCATION')
LS_candidates['LIABILITIES'] = LS_candidates['LIABILITIES'].replace(['Not Available'],'RS 0')
LS_candidates['ASSETS'] = LS_candidates['ASSETS'].replace(['Not Available'],'RS')
LS_candidates.head()


# In[460]:


a=LS_candidates['PARTY'].unique()
winners=[]
for i in a:
    winners.append(LS_candidates[LS_candidates['PARTY']==i]['WINNER'].sum())
figure1=go.Figure()
import plotly.express as px
fig = px.pie(values=winners, names=a, title='parties with winnings in 2019 loksabha elections')
fig.show()


# In[461]:


male=LS_candidates[LS_candidates['GENDER']=='MALE']['GENDER'].count()
female=LS_candidates[LS_candidates['GENDER']=='FEMALE']['GENDER'].count()
plt.subplot(1,1,1)
plt.title("Percentage of males and females participating in Loksabha Elections")
plt.pie([male,female],labels=['MALE','FEMALE'],autopct='%1.2f%%',shadow=True, startangle=90)
plt.show()
print(male)
print(female)


# In[463]:


a=LS_1['Party'].unique()
temp={}
for i in a:
    temp[i]=LS_1[(LS_1['Criminal Cases']>0) & (LS_1['Party']==i)]['Criminal Cases'].count()
figure=go.Figure()
temp=sorted(temp.items(), key=lambda x: x[1], reverse=True)
temp = {k: v for k, v in temp}
top10 = {k: temp[k] for k in list(temp)[:10]}
plt.title("Party with most candidates with criminal cases since 2004")
plt.bar(top10.keys(),top10.values())
plt.show()


# In[326]:


a=LS_candidates[LS_candidates['WINNER']==1]['NAME']
temp={}
for i in a:
    temp[i]=LS_candidates[(LS_candidates['WINNER']==1) & (LS_candidates['NAME']==i)]['OVER TOTAL VOTES POLLED \nIN CONSTITUENCY'].values[0]
figure=go.Figure()
temp=sorted(temp.items(), key=lambda x: x[1], reverse=True)
temp = {k: v for k, v in temp}
top15 = {k: temp[k] for k in list(temp)[:15]}
plt.title("Candidates who got highest share of votes in their constituency")
plt.bar(top15.keys(),top15.values())
plt.xticks(list(top15.keys()), rotation='vertical')
plt.show()


# In[465]:


a=list(LS_candidates['SYMBOL'].unique())
a.remove('NO SYMBOL')

temp={}
for i in a:
    temp[i]=LS_candidates[LS_candidates['SYMBOL']==i]['SYMBOL'].count()
figure=go.Figure()
temp=sorted(temp.items(), key=lambda x: x[1], reverse=True)
temp = {k: v for k, v in temp}
top15 = {k: temp[k] for k in list(temp)[:15]}
plt.title("Most number of candidates participated from a party")
plt.bar(top15.keys(),top15.values())
plt.xticks(list(top15.keys()), rotation='vertical')
plt.show()


# In[466]:


a=list(LS_candidates['CATEGORY'].unique())
a.remove('NO CATEGORY')
temp={}
for i in a:
    temp[i]=LS_candidates[LS_candidates['CATEGORY']==i]['SYMBOL'].count()
figure=go.Figure()
temp=sorted(temp.items(), key=lambda x: x[1], reverse=True)
temp = {k: v for k, v in temp}
plt.title("graph for percentage of candidates in a category")
plt.pie(temp.values(),labels=temp.keys(),autopct='%1.2f%%')
plt.show()


# In[341]:


a=list(LS_candidates['EDUCATION'].unique())
a.remove('NO EDUCATION')
temp={}
for i in a:
    temp[i]=LS_candidates[LS_candidates['EDUCATION']==i]['SYMBOL'].count()
figure=go.Figure()
temp=sorted(temp.items(), key=lambda x: x[1], reverse=True)
temp = {k: v for k, v in temp}
top15 = {k: temp[k] for k in list(temp)[:15]}
plt.title("candidates based on their education")
plt.bar(top15.keys(),top15.values())
plt.xticks(list(top15.keys()), rotation='vertical')
plt.show()


# In[377]:


a=LS_1[LS_1['Liabilities']>0]['Candidate']
temp={}
for i in a:
    temp[i]=LS_1[(LS_1['Liabilities']>0) & (LS_1['Candidate']==i)]['Liabilities'].values[0]
figure=go.Figure()
temp=sorted(temp.items(), key=lambda x: x[1], reverse=True)
temp = {k: v for k, v in temp}
top15 = {k: temp[k] for k in list(temp)[:15]}
print(LS_1[(LS_1['Liabilities']>0) & (LS_1['Candidate']==i)]['Liabilities'].mean())
plt.bar(top15.keys(),top15.values())
plt.xticks(list(top15.keys()), rotation='vertical')
plt.title("Candidates who have highest liabilities",pad=20)
plt.show()


# In[375]:


a=LS_candidates['STATE'].unique()
temp={}
for i in a:
    temp[i]=LS_candidates[(LS_candidates['STATE']==i) & (LS_candidates['WINNER']==1)]['STATE'].count()
figure=go.Figure()
temp=sorted(temp.items(), key=lambda x: x[1], reverse=True)
temp = {k: v for k, v in temp}
top15 = {k: temp[k] for k in list(temp)[:len(a)]}
plt.title("States with number of seats")
plt.bar(top15.keys(),top15.values())
plt.xticks(list(top15.keys()), rotation='vertical')
plt.show()
figure.update_layout(title="States with number of seats")
figure.add_trace(go.Bar(y=list(top15.values()),x=list(top15.keys())))
figure.show()


# In[394]:


a=LS_1[LS_1['Total Assets']>0]['Candidate']
temp={}
for i in a:
    temp[i]=LS_1[(LS_1['Total Assets']>0) & (LS_1['Candidate']==i)]['Total Assets'].values[0]
figure=go.Figure()
temp=sorted(temp.items(), key=lambda x: x[1], reverse=True)
temp = {k: v for k, v in temp}
top15 = {k: temp[k] for k in list(temp)[:15]}
plt.bar(top15.keys(),top15.values())
plt.xticks(list(top15.keys()), rotation='vertical')
plt.title("Candidates who have highest Assets since 2004",pad=20)
plt.show()


# In[384]:


a=list(LS_candidates['CONSTITUENCY'].unique())
temp={}
for i in a:
    temp[i]=LS_candidates[LS_candidates['CONSTITUENCY']==i]['TOTAL ELECTORS'].unique()[0]
figure=go.Figure()
temp=sorted(temp.items(), key=lambda x: x[1], reverse=True)
temp = {k: v for k, v in temp}
top15 = {k: temp[k] for k in list(temp)[:20]}
plt.title("highest number of electors in constituency")
plt.bar(top15.keys(),top15.values())
plt.xticks(list(top15.keys()), rotation='vertical')
plt.show()


# In[388]:


a=ge19[ge19['migrant_votes']>0]['candidate_name']
temp={}
for i in a:
    temp[i]=ge19[(ge19['migrant_votes']>0) & (ge19['candidate_name']==i)]['migrant_votes'].values[0]
figure=go.Figure()
temp=sorted(temp.items(), key=lambda x: x[1], reverse=True)
temp = {k: v for k, v in temp}
top15 = {k: temp[k] for k in list(temp)[:15]}
plt.bar(top15.keys(),top15.values())
plt.xticks(list(top15.keys()), rotation='vertical')
plt.title("Candidates who got high migrant votes",pad=20)
plt.show()


# In[393]:


a=[20,30,40,50,60,70,80,90]
temp={}
for i in range(len(a)-1):
    temp[str(a[i])+'-'+str(a[i+1])]=LS_candidates[(LS_candidates['AGE']>=a[i])& (LS_candidates['AGE']<a[i+1])]['AGE'].count()
plt.bar(temp.keys(),temp.values())
plt.xticks(list(temp.keys()), rotation='vertical')
plt.title("Age group of candidates")
plt.show()


# In[471]:


a=LS_candidates[LS_candidates['GENDER']=='MALE']['GENDER'].count()
m_win=LS_candidates[(LS_candidates['GENDER']=='MALE') & (LS_candidates['WINNER']==1)]['GENDER'].count()
b=LS_candidates[LS_candidates['GENDER']=='FEMALE']['GENDER'].count()
f_win=LS_candidates[(LS_candidates['GENDER']=='FEMALE') & (LS_candidates['WINNER']==1)]['GENDER'].count()

per_m=(m_win/a)*100
per_f=(f_win/b)*100
y=[per_m,per_f]
x=['male_wins_percentage','female_wins_percentage']
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(x,y)
plt.show()
print("male")
print(a,m_win)
print("female")
print(b,f_win)


# In[469]:


a=LS_1[(LS_1['Criminal Cases']>0)]['Criminal Cases'].count()
a_c_win=LS_1[(LS_1['Criminal Cases']>0)&(LS_1['Winner']==1)]['Criminal Cases'].count()
LS_candidates['CRIMINAL\nCASES']=LS_candidates['CRIMINAL\nCASES'].astype(int)
a_19=LS_candidates[(LS_candidates['CRIMINAL\nCASES']>0)]['CRIMINAL\nCASES'].count()
a_c_win19=LS_candidates[(LS_candidates['CRIMINAL\nCASES']>0)&(LS_candidates['WINNER']==1)]['CRIMINAL\nCASES'].count()

a_19_nocases=LS_candidates[(LS_candidates['CRIMINAL\nCASES']==0)]['CRIMINAL\nCASES'].count()
a_c_win19_nocases=LS_candidates[(LS_candidates['CRIMINAL\nCASES']==0)&(LS_candidates['WINNER']==1)]['CRIMINAL\nCASES'].count()

criminal_perc=(a_c_win19/a_19)*100
not_criminal_perc=(a_c_win19_nocases/a_19_nocases)*100

fig1 = plt.figure()
x=['criminal_perc','not_criminal_perc']
y=[criminal_perc,not_criminal_perc]
ax1 = fig1.add_axes([0,0,1,1])
ax1.bar(x,y)
plt.title("criminals and not criminals winning share in their categories")
plt.show()
print("criminal")
print(a_19,a_c_win19)
print("not criminal")
print(a_19_nocases,a_c_win19_nocases)
print(criminal_perc,not_criminal_perc)


# In[473]:


a=LS_candidates['STATE'].unique()
temp={}
for i in a:
    temp[i]=LS_candidates[(LS_candidates['CRIMINAL\nCASES']>0) & (LS_candidates['STATE']==i)]['STATE'].count()
figure=go.Figure()
temp=sorted(temp.items(), key=lambda x: x[1], reverse=True)
temp = {k: v for k, v in temp}
top15 = {k: temp[k] for k in list(temp)[:len(a)]}
plt.bar(top15.keys(),top15.values())
plt.xticks(list(top15.keys()), rotation='vertical')
plt.title("States with most number of criminal cases",pad=20)
plt.show()
figure.add_trace(go.Bar(y=list(top15.values()),x=list(top15.keys())))
figure.show()


# In[451]:


a=list(LS_candidates['EDUCATION'].unique())
a.remove('NO EDUCATION')
temp={}
for i in a:
    temp[i]=LS_candidates[(LS_candidates['EDUCATION']==i)&(LS_candidates['WINNER']==1)]['SYMBOL'].count()
figure=go.Figure()
temp=sorted(temp.items(), key=lambda x: x[1], reverse=True)
temp = {k: v for k, v in temp}
top15 = {k: temp[k] for k in list(temp)[:15]}
plt.title("elected candidates based on their education")
plt.bar(top15.keys(),top15.values())
plt.xticks(list(top15.keys()), rotation='vertical')
plt.show()


# In[467]:


a=LS_candidates[LS_candidates['GENERAL\nVOTES']>0]['NAME']
temp={}
for i in a:
    temp[i]=LS_candidates[(LS_candidates['GENERAL\nVOTES']>0) & (LS_candidates['NAME']==i)]['GENERAL\nVOTES'].values[0]
figure=go.Figure()
temp=sorted(temp.items(), key=lambda x: x[1], reverse=True)
temp = {k: v for k, v in temp}
top15 = {k: temp[k] for k in list(temp)[:15]}
plt.bar(top15.keys(),top15.values())
plt.xticks(list(top15.keys()), rotation='vertical')
plt.title("Candidates who got high general votes",pad=20)
plt.show()


# In[468]:


a=LS_candidates[LS_candidates['POSTAL\nVOTES']>0]['NAME']
temp={}
for i in a:
    temp[i]=LS_candidates[(LS_candidates['POSTAL\nVOTES']>0) & (LS_candidates['NAME']==i)]['POSTAL\nVOTES'].values[0]
figure=go.Figure()
temp=sorted(temp.items(), key=lambda x: x[1], reverse=True)
temp = {k: v for k, v in temp}
top15 = {k: temp[k] for k in list(temp)[:15]}
plt.bar(top15.keys(),top15.values())
plt.xticks(list(top15.keys()), rotation='vertical')
plt.title("Candidates who got high postal votes",pad=20)
plt.show()


# In[ ]:




