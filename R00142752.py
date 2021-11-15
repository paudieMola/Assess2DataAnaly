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
    # target is at least 1 movie longer than 150 and lang not eng
    # identify films with target language and duration
    # print(df['language'].value_counts())
    lengthMask = df['duration'] > 150
    langMask = df['language'] != 'English'
    target = df[langMask & lengthMask]
    # print(len(target))
    # group those by country
    targetCountries = target.groupby(['country'])
    # calculate how many films from each country and print with more than 1
    filmTarCountry = targetCountries.size()
    print('Films with at least 2 non English language films of greater than 150m in duration:')
    print(filmTarCountry[filmTarCountry > 1])
    

def Task3():
   # to get an idea relevant data
   # print(df[['gross', 'title_year']].info())
   # print(df[['gross', 'title_year']].describe())

   # get rid of all the films without a year specified
   df.dropna(subset=['title_year'], inplace = True)

   #get the gross mean to apply to missing values
   grossMean = df['gross'].mean()
   # print(grossMean)
   df['gross'].fillna(value=df['gross'].mean(), inplace = True)
   
   # group by title year and then sum the gross to get total for year
   # divide by 1m to make visulaisation easier
   yearly = df.groupby('title_year')['gross'].sum()/1000000

   # print(yearly.head())
   # print(yearly.tail())

   plt.plot(yearly)
   plt.xlabel('Year')
   plt.ylabel('Total earnings in millions')
   #check if I can now take this following line out
   plt.ticklabel_format(useOffset=False, style='plain')
   plt.show()
   

def Task4():
  
   #print(df.info())
   #print(df['gross'].describe())
   #print(df['budget'].describe())
   # drop rows with no values for gross or budget
   df.dropna(subset=['gross', 'budget'], inplace = True)
   #print(df.info())
   
   
   # mask for films from 1989 and after
   yearsMask = df['title_year'] > 1989
   reqYears = df[yearsMask]
   
   # group by years and get the total per year
   yearsFilms = reqYears.groupby('title_year')
   yearsTotals = yearsFilms.size()
   
   # mask for cost 2 times over budget
   overrunMask = reqYears['gross'] > (reqYears['budget']*2)
   overrunYears = reqYears[overrunMask]
   
   # group by year and get total per year
   yearlyOverruns = overrunYears.groupby('title_year')
   yearOverTotals = yearlyOverruns.size()
  
   # to ensure all years are reflected
   #print(len(yearsTotals))
   
   # create a dataframe to make calculating easier
   combined = pd.DataFrame({'yearsTotals' : yearsTotals, 'yearOverTotals': yearOverTotals})
   percent = (combined.yearOverTotals*100)/combined.yearsTotals
   plt.plot(percent)
   plt.xlabel('Year')
   plt.ylabel('% of films that cost over 2 times the budget')
   plt.show
   
def Task5():
   #no of movies each country
   #print(df.info())
   # only 5 with no country recorded so they will go with the under 30s

   # select all that are not USA or uk and group
   noUs = df['country'] != 'USA'
   noUk = df['country'] != 'UK'
   exUsUk = df[noUs & noUk]
   
   # group all others by country
   countries = exUsUk.groupby('country')
   
   # put counts into a series
   countryseries = countries.size()
   
   # get countries from series that have > 30 counts
   newCnt = countryseries[countryseries > 30]

   # get the total number of films from these countries
   total = newCnt.sum()
   
   percent = ((newCnt*100)/total)
   plt.title('% of films')
   labels = newCnt.index
   plt.pie(percent,  labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
 

def Task6():
    #Each movie has a length (duration). Apply an appropriate visualization technique and visually
#depict what durations (movie lengths) are more common and popular among all movies in
#the file.
#Use comment and indicate the common and popular movie lengths.
#Data Cleansing: Some movies do not have a known duration, those movies (rows) should be
#ignored for this task.

    # drop films with unknown duration
    df.dropna(subset=['duration'], inplace = True)
    
    # to get an idea of what data is in the column
    print(df['duration'].describe())

    

Task5()


