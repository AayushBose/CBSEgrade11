#Write a program to print elements of a list['q','w','e','r','t','y'] in separate lines along with both their indexes ( positive and negative )
L = ['q','w','e','r','t','y']
for i in range(len(L)):
    print("At position",i,"and",i-len(L),L[i])