li = [103,52,273,32,77]

min_value = 9999
>>> for i in li:
...     if min_value > i:
...         min_value = i
...
>>> min_value
32

max_value = -9999
>>> for i in li:
...     if max_value < i:
...         max_value = i
...
>>> max_value
273