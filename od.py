from collections import OrderedDict
import operator
l = ['a','b','c','a','x','a','b','c','b']

d = OrderedDict()
for i in l:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)
print("Max number in dictionary",max(d.items(),key=operator.itemgetter(1))[0])