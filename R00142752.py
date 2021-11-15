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
    #at least 1 movie longer than 150 and lang not eng
    return
  



def Task3():
   return
    
   
    
   
   

def Task4():
  return
    
  

    
   

def Task5():
   return
    
   
    
   

def Task6():
    return
    

Task1()


