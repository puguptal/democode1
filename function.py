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

fobj.write('python prog\n')
fobj.write('python\n')
fobj.write('prog\n')

fobj.close()

fobj=open("C:/Users/pgupta24/Desktop/demo.txt","r")
content=fobj.read()
print(content)
fobj.close() 

# read  line by line 
# reading the whole file at a time fobj.readlines() & fobj.read()

fobj = open('C:/Users/pgupta24/Desktop/demo.txt')

for line in fobj:
    print(line)
    
fobj.close()

