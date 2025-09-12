"""Extract 2 list slices out of a givne list of numbers. 
DIsplay and print the sum of elements of first list slice which contains every other element of the list between indexes 5 to 15.
Program should also display the average of elements in second list slice that contains every fourth element of the list.
The given list coontains numbers from 1 to 20
"""
lst = list(range(1,21))
slc1 = lst[5:15:2]
slc2 = lst[::4]
s1=avg=0
for a in slc1:
    s1 += a
print(s1) 
s1=0
for a in slc2:
    s1+=a
    avg = s1/len(slc2)
print(avg)