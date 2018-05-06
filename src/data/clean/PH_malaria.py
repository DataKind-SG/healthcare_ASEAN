import os
import sys
import csv
import itertools


indirectory = '../../../Data/raw/disease_PH'
input_file = 'yearly-Malaria.csv'

outdirectory = '../../../Data/interim/disease_PH'
output_file = 'yearly-Malaria_PH.csv'

confirmed_malaria = []
death_malaria    = []
year             = []

if not os.path.exists(outdirectory):
    os.makedirs(outdirectory)
    
input_path = os.path.join(indirectory, input_file)
output_path = os.path.join(outdirectory, output_file)

with open(input_path, 'r') as infile:
    for line in infile:

        if 'Indicator' in line:
            line=line.replace('\n','')
            tmp= line.split(',')
            for i in range(1,len(tmp)): 
                
                tmp1 = tmp[i].replace('Philippines;','')
                tmp1 = tmp1.replace('\"','')
                year.append(int(tmp1))
                   
        if 'Malaria' in line and 'confirmed' in line:
            line=line.replace('\n','')
            tmp= line.split(',')
            for i in range(1,len(tmp)): 
                
                tmp1 = tmp[i].replace(' ','')
                tmp1 = tmp1.replace('\"','')
                
                if len(tmp1) > 0:
                    confirmed_malaria.append(int(tmp1))
                else :
                    confirmed_malaria.append(0)
                

        if 'Malaria' in line and 'death' in line:
            line=line.replace('\n','')
            tmp= line.split(',')
            for i in range(1,len(tmp)): 
                
                tmp1 = tmp[i].replace(' ','')
                tmp1 = tmp1.replace('\"','')
                
                if len(tmp1) > 0:
                    death_malaria.append(int(tmp1))
                else :
                    death_malaria.append(0)


outfile = open(output_path, 'w')
for i in range(len(year)):
    outfile.write("{} {} {}\n".format(year[i], confirmed_malaria[i], death_malaria[i]))
        
infile.close()
outfile.close()
