alist = [10,20,30,40]
blist =  ["unix","scala","spark","hadoop"]
#clist = [10,20,"unix,"scala",4000,56.44]

print(alist[0])
print(alist[1])
print(alist[0:3])
print(alist[-1])
print("updated list:", alist) 
final = alist+blist
print('i.e.',final)

# tuple - set of elements, defined in ()

atup=(1,2)
btup=('x','y')
print(atup)
atup[0]=1000
print('new:',atup)