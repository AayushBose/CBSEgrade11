# a tuple t1 stores (11,21,31,42,51), where its second last element is mistyped. Write a program to correct its second last element as 41
t1 = (11,21,31,42,51)
print(t1)
lst = list(t1)
lst[-2]=41
t1 = tuple(lst)
print(t1)