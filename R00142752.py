# -*- coding: utf-8 -*-
"""
Created on a sunny day

@author: Helen Daly
@id: R00142752
@Cohort: SOFT8032_26756
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 


df = pd.read_csv("movie_metadata.csv", encoding = 'utf8')

#print(df.info())  
#print(df['color'].value_counts())
# to strip white space from the color column
s = pd.Series(df['color'])
s= s.str.strip()
df['color'] = s

def Task1():
    #get rows of Black and white films
    bwMask = df['color'] == 'Black and White'
    bwFilms = df[bwMask]
    
    #group those by actor
    bwActors = bwFilms.groupby(['actor_1_name'])
    
    #get series of groups and sizes
    actBWFilms = bwActors.size()
    #print(type(actBWFilms))
    
    #apply condition to the series
    print('Actors with at least 2 Black and white film')
    print(actBWFilms[actBWFilms > 1])
    


def Task2():
    #target is at least 1 movie longer than 150 and lang not eng
    #identify films with target language and duration
    #print(df['language'].value_counts())
    lengthMask = df['duration'] > 150
    langMask = df['language'] != 'English'
    target = df[langMask & lengthMask]
    #print(len(target))
    #group those by country
    targetCountries = target.groupby(['country'])
    #calculate how many films from each country and print with more than 1
    filmTarCountry = targetCountries.size()
    print('Films with at least 2 non English language films of greater than 150m in duration:')
    print(filmTarCountry[filmTarCountry > 1])
    

def Task3():
   #sort by years early to latest and show income(gross) growth
   #fill in nan gross with average. 
   #to get an idea of what values are in the gross column
   #print(df['gross'].describe())
   #nullGross = [df['gross'].isnull()
   #to make sure null values are not used in calculating mean
   #grossMean1 = df['gross'].mean(skipna = True)
   #grossMean = df['gross'].mean()
   #print(grossMean1, grossMean)
   
   grossMean = df['gross'].mean()
   print(grossMean)
   df['gross'].fillna(value=df['gross'].mean(), inplace = True)
   #print(df.info()) 
   yearly = df.groupby(['title_year', 'gross'])['gross'].sum()
   print(type(yearly))
   #yearly.plot(kind = 'scatter', x = 'title_year', y = 'gross')
   #plt.show()
   # print(df['gross'].describe())
   #plt.plot(yearly)
   #plot.show()
   yearly.plot()
   #plt.show()
   
   
   
    
   
    
   
   

def Task4():
  return
    
  

    
   

def Task5():
   return
    
   
    
   

def Task6():
    return
    

Task3()


