



name= "python"
print(name.upper())
print(name.replace('python','puneet'))
print(name.isalpha())
print(name.isalnum())

alist=[10,20,30,40]
print(alist.count(20))

# dir(__builtins__) # list of all predefined functions
getindex=alist.index(20)
print(getindex)
alist.reverse()
print(alist)
alist.pop(1)
print(alist)