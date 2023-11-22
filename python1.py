a=[*range(0,100)]
for i in a:
  oddlist=[]
  evenlist=[]
for i in a:
   if i%2==0:
     evenlist.append(i)
   else:
      oddlist.append(i)
print ("even numbers", evenlist)
print ("odd numbers", oddlist)