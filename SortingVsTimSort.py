import time
arrayOne = [5,8,33,65,99]
arrayTwo = [100,1,0,3,23]


totalArray= arrayOne+arrayTwo
sortByInbuild=totalArray

i=0;
j=0
start = time.time()
# normal sorting 
for i in range(len(totalArray)):
  for j in range(len(totalArray)):
    if totalArray[i]>totalArray[j]:
      pass
      #print'no swap',totalArray,' index i- ',i,' index j ',j
    else:
      temp = totalArray[i]
      totalArray[i]=totalArray[j]
      totalArray[j]=temp
      #print'swaped',totalArray,' index i- ',i,' index j ',j
  j=j+1
i=i+1
end = time.time()
print 'Linear Sorting',totalArray
print 'Time taken in Liner Sorting', end-start


startInbuild = time.time()
sortedList=sorted(sortByInbuild)
endInbuild = time.time()
print'In Buid Sorted ',sortedList
print'Time taken for In build Sorting',endInbuild-startInbuild 


  
  

    
