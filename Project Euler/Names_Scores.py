''' PROJECT EULER: PROBLEM 22: NAMES SCORES

Using names.txt (right click and 'Save Link/Target As...'), a 46K text
file containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a
name score.

For example, when the list is sorted into alphabetical order, COLIN,
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''
import string

def alpha_score(name):
    name = name.strip('\"')
    alpha_score = sum((string.ascii_uppercase.index(i)+1 for i in name))
    return alpha_score

with open('p022_names.txt') as f:
  names = f.read().split(',')
  sorted_names = sorted(names)

sum_sorted_names = sum(index*alpha_score(name) for index, name in enumerate(sorted_names))

print(f'For the file the sum of alphabetically sorted names is {sum_sorted_names}!')




















# end.
