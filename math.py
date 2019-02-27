# how to open  a file in python

obj = open(filename,mode)

#Example:
 
fobj = open('customer.txt",'r')   
fobj = open('customer.txt",'w')
fobj = open('customer.txt",'a')

# r -- read mode
# w -- write mode
# a -- append mode


# read mode 
# if file doesnt exist -- error msg 
# if file is there -- display contents

# w - write mode 
# if file not there - it creates the file and write the data
#If exists - it overwrites the data and start from scratch


# a - append mode
# if file exists - appand the data
# if no file - create and writes the data


fobj = open('C:/Users/pgupta24/Desktop/demo.txt','w')

fobj.write('python prog sdasda\n')
fobj.write('python sdas sdaasd sad\n')
fobj.write('progsadasds\n')

fobj.close()

fobj=open("C:/Users/pgupta24/Desktop/demo.txt","r")
content=fobj.read()
print(content)
fobj.close() 

# read  line by line 
# reading the whole file at a time fobj.readlines() & fobj.read()

fobj = open('C:/Users/pgupta24/Desktop/demo.txt')

for line in fobj:
    #remove whitespace at the end of each line
    line = line.strip()
    ##split the line with , as the delimeter
    data = line.split(' ')
    d = list(data) 
    print(d)
fobj.close()


# prog to show lines containing females
fobj = open('C:/Users/pgupta24/Desktop/Example/datasets/employees.csv')

for line in fobj:
    line= line.split(',')
    a = line[1]
    if a == 'Female':
        print(line)
    
    
# program to calculate the number of females 
        
fobj = open('C:/Users/pgupta24/Desktop/Example/datasets/employees.csv')
x = 0
j = 0
for line in fobj:
    line = line.split(',')
    c = len(line)
    for a in range(0,c,1):
       b = line[a]
       if b == 'Male':
           x = x + 1
         
       if b == 'Female':
           j = j + 1
        
print(x)
print(j)
        
# write line where salary > 100000
fobj = open('C:/Users/pgupta24/Desktop/Example/datasets/employees.csv')
line = fobj.readline()
x = 0
j = 0
for line in fobj:
    line = line.split(',')
    c = len(line)
    for a in range(0,c,1):
       b = line[a]
       if b == 'Salary':
          print(a)
       y = int(a)
       q = line[4]
       
       d = int(q)
    if d > 100000:
        print(line)

         
for line in fobj:
    print(line)
    
    
    
# context manager 
with open('C:/Users/pgupta24/Desktop/Example/datasets/employees.csv') as fobj:
    for line in fobj:
        print(line)
        
        
        
# reading lines
        
with open('C:/Users/pgupta24/Desktop/Example/datasets/employees.csv') as fobj:
    data = fobj.readlines()
    
for line in data[0:5]:
    print(line)
    
# built in libraries
    
# installed in  -- C:\Anaconda3\Lib
    
 # 3rd party libraries  - develooper has to install 
 # path -- C:\Ananconda3\Lib\site-packages
 # 3rd party library available in  -  www.pypi.org
 #libraries
# - math
# -os
# -sys
# -time
# -datetime
# -logging
# -shutil
# -copy
# -unitest
# -pytest
# -xml
# -email
# -sqlite3
# 
    