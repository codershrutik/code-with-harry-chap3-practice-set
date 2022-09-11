import re

my_str = 'avocado   banana  cherry   dragonfruit'
result = " ".join(my_str.split())
print(repr(result))

result_2 = re.sub(' +', ' ', my_str)
print(repr(result_2))