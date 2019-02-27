

# write a program to capture the string and the output in terms of list.
# enter any list : perl, unix, spark,scala 
#List output - ['perl;, 'unix', 'saprk', 'scala']
# length of list - 4 
#-----------------------------------------------------------


a = input('first string - ')
b = input('second string - ')
c = input('third string - ')
d = input('forth string -')
alist = [a,b,c,d]
print(alist)
z = len(alist)
print('length of list -',z)

#------------------------------------------------------------------

# write a program to remove all the duplicated from the list
#alist = [10,20,10,20,30,40,50,20,30,40,60,70,80,10]
#output: [10,20,30,40,50,60,70,80]


blist = [10,20,10,20,30,40,50,20,30,40,60,70,80,10]
clist = set(blist)
dlist = list(clist)
dlist.sort()
print(dlist)


#--------------------------------------------------------------------

#write a prog to capture any filename and display filename and extension sepertaely

#enter any filename: data.csv
#filename : data
#extension : csv 

name = input('enter any filename')



#extension = input('enter any extension')
#dot = print('.', extension)
#Name = filename + dot 
#print(name)

name=input("Enter any filename:")
full=str(name)
sp=full.split('.',1)
alist=sp
print("filename", alist[0])
print("extension", alist[1]) 


name=input("Enter any filename:")
a= name.split('.',1)
print(a[0])
print(a[1])


#write a program to create a empty list and perform the following operations




alist= []
alist.append(100)
alist.append(30)
alist.append(1000)
blist = [90,3,3543,53,43,42,534,10,10,10,20]
alist.extend(blist)
print(alist)
alist.pop(5)
print(alist)
print(alist[6])


name = input('enter any file name :')
a = name.split('.',1)
b = a[1]
name = name.replace(b,'csv')
print(name)

name = "python is general purpose and python is interactive and python is cross 	platform language"
print(name.count('python'))
alist = name.split(' ')
a = len(alist)
print(a)
print(name.upper())
new = name.replace('python','spark')
print(new)

#append 100 to the list

#append 60 to the list

#       30 to the list

 #     1000 to the list

#extend the list with [90,3,3543,53,43,42,534,10,10,10,20]

#remove the element with 543

#pop the element which is at index 5

#find the element at the index 6 


name=input("Enter any filename:")
full=str(name)
sp=full.split('.',1)
b=sp[1]
if b=='py':
    print("python file")
elif b=='txt':
    print("text file")
elif b=='csv':
    print("csv file")
elif b=='pl':
    print("perl file")
elif b=='ksh':
    print("korn shell file")    
else:
    print("cannot recognize") 
    
    

name = '192.168.0.0'

for c in range(0,100,1):
    alist = name.split('.',3)
    b=alist[3]
    d = str(c)
    e=d
    name = name.replace('b','e')
    print(name)
    
    
    
    list = ["google","unix","facebook","linkedin"]

#write a program to read the above list and add "http://www" at the beginning
#and append ".com" at the end of each element.
#
#http://www.google.com
#http://www.unix.com
#http://www.facebook.com
#http://www.linkedin.com


alist = ["google","unix","facebook","linkedin"]

for i in range (0,4,1):
    a = alist[i]
    c = str(a)
    b = 'http://www.' + c + '.com'
    print(b)


#Write a program to check the validity of password input by user.
#Following are the criteria for checking the password:
#
#1. At least 1 character from [$#@]
#2. Minimum length of transaction password: 6
#3. Maximum length of transaction password: 12
#
#
#display "Valid password" if all the conditions are 
#satisfied or "Invalid password"



name = input('enter your pass : ')
a = list(name)
b = len(name)

if (b > 5) and (b < 13) :
    for i in range(0,b,1):
        d = a[i]
        
        if (d == '$') or (d == '#') or (d == '@'):
            flag=1
                   
else:
    print('invalid pass')
if (flag==1):
      print("valid")
else:
      print("invalid")    
      
      
      
def display(*data):
    print(data)
    for item in data:
        print(item)
    
display(10,20,['java',20,'python'],20,49,40)        
    
    
    








