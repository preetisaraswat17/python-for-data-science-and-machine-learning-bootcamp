from collections import Counter

n=int(input())
num=[int(x) for x in input().split(" ")]
num=sorted(num)

#---------Mean------------
#assign value to mean function
mean=lambda x: sum(x)/n
#always remember to call the function else it will give object reference ex: print (mean)
print (mean(num))  

#-------Median-------------

mid=lambda x: (x+1)//2 if x%2!=0 else  ((x//2),(x//2)+1)
middle=list(mid(n))
if len(middle)==1:
    median=num[middle[0]]
    print(median)
else:
    median=(num[middle[0]-1]+num[middle[1]-1])/2
    print(median)
    
#--------Mode---------------
#The Counter counts the frequency and returns a defaultdict. 
#sorted(Counter(num).items()) sorts using keys(which are numbers), not the frequency(or count). 
#so we need to provide key function for sort
#lambda x: x[1]. means sort using frequency
#reverse=True tells Python to sort the frequency from the largest to the smallest.
#finally return largest frequency

Mode = sorted(sorted(Counter(num).items()), key = lambda x: x[1], reverse = True)[0][0]
print(Mode)
