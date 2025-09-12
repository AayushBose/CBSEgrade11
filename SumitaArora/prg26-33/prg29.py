"""Given a tuple pairs  =  {(2,5),(4,2),(9,8),(12,10)}  ,  count   the  number   of  pairs  (a,b) such that 
both a and b are even."""
t = {(2,5),(4,2),(9,8),(12,10)}
count = 0
for pair in t:
    if pair[0]%2==0 and pair[1]%2 == 0:
        count = count+1
print(count)