__author__ = 'yang'

#
# tel1 = {'jack': 4098, 'sape': 4139}
# tel1['guido'] = 4127
#
#
# tel2 = {'jack': 4098, 'sape': 4139}
# tel2['guido'] = 4127
#
# tel3 = {'jack': 4098, 'sape': 4139}
# tel3['guido'] = 4127
#
# listofdict = [tel1, tel2, tel3]


import json

#with open('test_dict.json', 'w') as f:
#    json.dump(listofdict, f)

# load
# with open('test_dict.json') as f:
#    word_dict = json.load(f)
#    print(word_dict[1]['jack'])


# from collections import defaultdict
# s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# d = defaultdict(list)
# for k, v in s:
#      d[k].append(v)
#      print(d[k])

project = 'category'

with open('vocab_' + project +'.json') as f:
    vocabulary = json.load(f)


print('assad' in vocabulary)

