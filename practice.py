from random import *
lst = [1,2,3,4,5]
shuffle(lst)
print(lst)
print(sample(lst,1))
users = range(1,21)
users = list(users)
winners = sample(users,4)
print(winners)