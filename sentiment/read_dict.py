__author__ = 'yang'


import re

dict_file_name= 'words.tff'

# initial the dict
word_dict = dict()

with open(dict_file_name) as f:
    for line in f:
        word_list = re.split('=| ', line)

        word = word_list[5]
        if word_list[1][:4] == 'weak':
            score = 0.5
        else:
            score = 1

        if word_list[-1][:4] == 'nega':
            score *= -1

        word_dict[word] = score



# save dictionary
import json

with open('word_dict.json', 'w') as f:
    json.dump(word_dict, f)

# load
# with open('word_dict.json') as f:
#    word_dict = json.load(f)

