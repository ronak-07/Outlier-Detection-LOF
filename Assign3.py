# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 13:00:59 2018

@author: ronak
"""
import numpy as np
import time
import operator
import pandas as pd
import os

#Specify k
k=35

#Number of card details
rows=1000

#Dictionary to store all the card attributes
card_details=dict()

#Dictionary to store the keys of card numbers
distance_keys=dict()

#Matrix to store the distances
distance_array=np.zeros(shape=(rows,rows))

#List to store kth distances
kdist=list()

#Dictionary to store the neighbours
neigh=dict()

#List to hold the reachable distances. Used in step 4 and step 5
reach_dist=list()

#Dict to store the Local reachable density(LRD) values
lrd=list()

#Dictionary to store the Local Outlier Factor values
lof=dict()

def last_step():
    sorted_lof = sorted(lof.items(), key=operator.itemgetter(1),reverse=True)
    df=pd.read_csv("input_graph.csv")
    for i in range(0,k-1):
        df.set_value(sorted_lof[i][0],"target",2)
        r=str(sorted_lof[i][0])+ " " +  str(sorted_lof[i][1]) + "\n"
        #print(sorted_lof[i][0],sorted_lof[i][1])
        file.write(r)
    
    df.to_csv("graph2.csv", index=False)
    

def local_outlier_factor():
    for i in range(0,rows):
        lrd_values=0
        for j in neigh[i]:
            lrd_values+=lrd[j]
        
        lof[i]=lrd_values*reach_dist[i]
    
def local():
    for i in range(0,rows):
        values=0
        for j in neigh[i]:
            values+= max(kdist[j],distance_array[i][j])
            
        reach_dist.insert(i,values)    
        lrd.insert(i,len(neigh[i])/reach_dist[i])

def neighbour():
    for i in range(0,rows):
        neigh[i]=list()
        for j in range(0,rows):
            if distance_array[i][j]<= kdist[i] and i!=j:
                neigh[i].append(j)


def k_distance():
    for i in range(0,rows):
        d=sorted(distance_array[i])
        kdist.insert(i,d[k])

def distance():
    key=-1
    for i in range(0,rows):
        for j in range(0,i):
            key+=1
            distance_keys[key]=[i,j]
            distance_array[i][j]=sum(abs(x-y) for x,y in zip(card_details[i],card_details[j]))
            distance_array[j][i]=distance_array[i][j]
            
def preprocessing():
    file=open("German-data-numeric.txt")
    for i,line in enumerate(file):
        details=line[:99].split(' ')
        while '' in details:
            details.remove('')
        card_details[i]=list(map(int,details))
        
    file.close()
          
if __name__ == "__main__":
    path="C:\\My Folder\\CMS\\CMS downloads\\4-2\\Data Mining\\Assign\\Assign 3\\K Values\\Text Files\\" +str(k-1)+".txt"
    file=open(path,"w+")
    
    #Step0: Preprocess
    start=time.time()
    preprocessing()
    file.write("Processing Time: " +str(time.time()-start)+"\n")
    #print("Processing Time: " +str(time.time()-start))
    
    #Step 1: Calculate Manhattan Distance
    start=time.time()
    distance()
    file.write("Distance Matrix Time: " +str(time.time()-start)+"\n")
    #print("Distance Matrix Time: " +str(time.time()-start))
    
    #Step2: Calculate kth distance
    start=time.time()
    k_distance()
    file.write("Calculate kth distance: "+ str(time.time()-start)+"\n")
    #print("Calculate kth distance: "+ str(time.time()-start))
    
    #Step3: k distnace Neighbourhood
    start=time.time()
    neighbour()
    file.write("To Calculate the Neighbourhood: " +str(time.time()-start)+"\n")
    #print("To Calculate the Neighbourhood: " +str(time.time()-start))
    
    #Step4: Calculate Local Reachable Density
    start=time.time()
    local()
    file.write("To Calculate the Local Reachable Density: " +str(time.time()-start)+"\n")
    #print("To Calculate the Local Reachable Density: " +str(time.time()-start))
    
    #Step5: Calculate Local Outlier Factor
    start=time.time()
    local_outlier_factor()
    file.write("To Calculate Local Outlier Factor:"+ str(time.time()-start)+"\n")
    #print("To Calculate Local Outlier Factor:"+ str(time.time()-start))
    
    #Step 6: Print the Outlier
    start=time.time()
    last_step()
    file.write("To print the outlier:"+ str(time.time()-start)+"\n")
    #print("To print the outlier:"+ str(time.time()-start))
    
    os.system('python K_graph2.py')
    file.close()