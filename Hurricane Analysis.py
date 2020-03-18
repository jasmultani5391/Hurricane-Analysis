#!/usr/bin/env python
# coding: utf-8

# In[121]:


import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']
# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

def x_damages(num):
  updated_damages = []
  for i in num: 
    if 'Damages not recorded' in i:
      i = i.replace('Damages not recorded', '0')
      updated_damages.append(i)
    if 'Damages not recorded' not in i:
      if ('M' in i) and ('.' not in i):
        i = i.replace('M', '000000')
        updated_damages.append(i)
      if ('M' in i) and ('.' in i):
        i = i.replace('.', '')
        i = i.replace('M', '00000')
        updated_damages.append(i)
      if ('B' in i) and ('.' not in i):
        i = i.replace('B', '000000')
        updated_damages.append(i)
      if ('B' in i) and ('.' in i):
        i = i.replace('.', '')
        i = i.replace('B', '00000000')
        updated_damages.append(i)
  return updated_damages

newdamages = x_damages(damages)
newdamages = pd.to_numeric(newdamages)
#print(newdamages)

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

def final_dict(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
  dictionary = {}
  for i in range(len(names)):
    dictionary[i] = {"Names" : names[i],
                     "Months": months[i],
                     "Years": years[i],
                     "Max Sustained Wind": max_sustained_winds[i],
                     "Areas Affected": areas_affected[i],
                     "Damage": newdamages[i],
                     "Deaths": deaths[i] }
  return dictionary

HLoss = final_dict(names,
                   months,
                   years,
                   max_sustained_winds,
                   areas_affected,
                   damages,
                   deaths)

HurrData = pd.DataFrame(HLoss.values())
HurrLoss = pd.DataFrame(HLoss.values())
HurrLoss = HurrLoss.sort_values(by=['Years'], ascending = False)

print(HurrLoss.head(10))


# In[90]:


# write your count affected areas function here:

def counting_areas(parameter):
    recurring = []
    unique_keys = []
    for i in parameter:
        for ii in i:
            recurring.append(ii)
            if ii not in unique_keys:
                unique_keys.append(ii)
    return recurring, unique_keys

recurring, unique_keys = counting_areas(areas_affected)

#print(recurring, unique_keys)

# most affected area function here:
def finalcount(parameter):
    area_dictionary = {}
    for i in parameter:
        area_dictionary[i] = parameter.count(i)
    return area_dictionary

area_dictionary = finalcount(recurring)
print(area_dictionary)


# write your greatest number of deaths function here:

deadliest = HurrLoss.sort_values(by=['Deaths'], ascending = False)
deadliestHurr = list(deadliest.get('Names'))
deadliestAmt = list(deadliest.get('Deaths'))
deadliestYr = list(deadliest.get('Years'))
list(zip(deadliestHurr, deadliestAmt, deadliestYr))

deadliestHurrAmt = list(zip(deadliestHurr, deadliestAmt))
#print(deadliestHurrAmt[0])


# write your catgeorize by mortality function here:

def mortality_category(param):
    ranked_by_mortality = {'No Deaths':[], 1:[], 2:[], 3:[], 4:[], 5:[]}
    for i, ii in param:
        if (ii > 0):
            ranked_by_mortality ['No Deaths'].append(i)
        if (ii > 0) and (ii <= 100):
            ranked_by_mortality [1].append(i)
        if (ii > 100) and (ii <= 500):
            ranked_by_mortality [2].append(i)
        if (ii > 500) and (ii <= 1000):
            ranked_by_mortality [3].append(i)
        if (ii > 1000):
            ranked_by_mortality [4].append(i)
    return ranked_by_mortality

ranked_by_mortality = mortality_category(deadliestHurrAmt)
#print(ranked_by_mortality)



# write your greatest damage function here:
greatestdamage = HurrLoss.sort_values(by=['Damage'], ascending = False)
damagedHurr = list(greatestdamage.get('Names'))
damagedAmt = list(greatestdamage.get('Damage'))
damagedHurrAmt = list(zip(damagedHurr, damagedAmt))
#print(damagedHurrAmt[0])


# categorizing hurricanes by damages:

def damage_category(param):
    hurricanes_by_damage = {'Damages Not Recorded':[], 1:[], 2:[], 3:[], 4:[], 5:[]}
    for i, ii in param:
        if (ii == 0):
            hurricanes_by_damage['Damages Not Recorded'].append(i)
        if (ii > 0) and (ii < 100000000):
            hurricanes_by_damage[1].append(i)
        if (ii > 100000000) and (ii < 1000000000):
            hurricanes_by_damage[2].append(i)
        if (ii > 1000000000) and (ii < 10000000000):
            hurricanes_by_damage[3].append(i)
        if (ii > 10000000000) and (ii < 50000000000):
            hurricanes_by_damage[4].append(i)
        if ii > 50000000000:
            hurricanes_by_damage[5].append(i)
    return hurricanes_by_damage

#hurricanes_by_damage = damage_category(damagedHurrAmt)#
print(hurricanes_by_damage)




# In[103]:


from matplotlib import pyplot as plt

#print(area_dictionary)
area_names = list(area_dictionary.keys())
area_nameshurrdamages = list(zip(area_names, names, newdamages))
freq_hit = list(area_dictionary.values())
#print(len(area_dictionary))

plt.hist(freq_hit, alpha = .4)
plt.show()

#most of the time, when a hurricane hits an area, it's a new ara; areas may not be experiened or be anticipating these hits, may explain why damages can be so devastating
# next thing: of the areas that have been hit 4 times or less, whats the correlating damage? i think itd be higher in these places

areas_oftenhits = []
areas_rarehits = []


#for i, ii in area_dictionary.items():
 #   if ii >= 2:
  #      areas_oftenhits.append(i)
   # elif ii < 2:
     #   areas_rarehits.append(i)
#print(areas_rarehits)


# In[96]:


plt.plot(HurrLoss.Years[-11:], HurrLoss.Deaths[-11:], color = 'red', marker = 'o')
plt.xlabel('Years')
plt.ylabel('Deaths per hurricane')
plt.plot(HurrLoss.Years[:-10], HurrLoss.Deaths[:-10], color = 'blue', marker = 'o')
plt.xlabel('Years')
plt.ylabel('Deaths per hurricane')
plt.show()


plt.plot(HurrLoss.Years[-11:], HurrLoss.Deaths[-11:], color = 'red', marker = 'o')
plt.xlabel('Years - 1923 to 1965')
plt.ylabel('Deaths per hurricane')
plt.show()

plt.plot(HurrLoss.Years[:-10], HurrLoss.Deaths[:-10], color = 'blue', marker = 'o')
plt.xlabel('Years - 1960 to 2018')
plt.ylabel('Deaths per hurricane')
plt.show()


mostDeadlyint = (max(deaths))
mostDeadly = HurrData.loc[HurrData['Deaths'] == mostDeadlyint]

MitchAreas = HurrData.iloc[21, 4]  #21 is the row for Mitch hurricane, column 4 grabs the areas affectedm; verify through print(mostDeadly)


knowntobehit = {}
notknown = {}
for i in MitchAreas:
    if i in areas_rarehits:
        notknown[i] = area_dictionary.get(i)
    if i in areas_oftenhits:
        knowntobehit[i] = area_dictionary.get(i)
    

print(knowntobehit)
print(notknown)
#Would want to know how many deaths belonged to each area


# In[152]:


def normit(column):
    newlist = []
    for i in column:
        a = float(i)
        newlist.append(a)
    minimum = min(newlist)
    maximum = max(newlist)
    normalized = []
    for i in newlist:
        normalized += [(i - minimum)/ (maximum-minimum)]
    return normalized

normDamages = normit(newdamages)
normDeaths = normit(deaths)
normMPH = normit(max_sustained_winds)
plt.plot(HurrData['Years'], normDeaths, "o", alpha = 0.4)
plt.plot(HurrData['Years'], normDamages, "s", alpha = 0.4) #final damaes have only increased
plt.show()


# In[155]:


plt.plot(HurrLoss.Years, HurrLoss.Damage, color = 'orange', marker = 'o')
plt.xlabel('Years')
plt.ylabel('Damage per hurricane ($)')

mostDamagedint = (max(newdamages))
mostDamaged = HurrData.loc[HurrData['Damage'] == mostDamagedint]
print(mostDamaged)

plt.show()


# In[170]:


#trying to understand whether damages and mortality due to nature of hurricane or preparedness of community

nonzeroDamages = HurrLoss['Damage'].replace(0, np.nan)

mph_freq = HurrData['Max Sustained Wind'].value_counts()


mph_range = HurrData['Max Sustained Wind'].unique()
avg_mph = HurrData['Max Sustained Wind'].mean()
print(avg_mph)
print(mph_freq)
print(mph_range)

plt.pie(mph_freq, labels = mph_range, autopct = '%0.1f')
plt.axis('equal')
plt.legend()
plt.show()


plt.plot(HurrLoss['Max Sustained Wind'], normDamages, "o", alpha = 0.4)
plt.xlabel('MPH per hurricane')
plt.ylabel('Effect per hurricane')
plt.plot(HurrData['Max Sustained Wind'], normDeaths, "o", alpha = 0.4)
plt.xlabel('MPH per hurricane')
plt.ylabel('Effec per hurricane')
legend_labels = ['damages', 'deaths']
plt.legend(legend_labels, loc = 5)


plt.show()

fiercestHurr = (max(HurrData['Max Sustained Wind']))

fiercestHurrINFO = HurrData.loc[HurrData['Max Sustained Wind'] == fiercestHurr]
print(fiercestHurrINFO)


# In[173]:


fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)

# We can set the number of bins with the `bins` kwarg
axs[0].hist(normDeaths, bins=34, alpha = 0.4)
axs[0].hist(normDamages, bins=34, alpha = 0.4)

