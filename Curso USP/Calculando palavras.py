


'''
import string

# initialize string
text = 'o, gato, caçava, o, rato'

# using the sum(), strip(), split() methods
result = sum([i.strip(string.punctuation).isalpha() for i in text.split()])

print("There are " + str(result) + " words.")
'''
'''
# import regex module
import re

# initialize string
text01 = 'Python !! is the best $$             programming language @'

# using regex findall()
result01 = len(re.findall(r'\w+', text01))

print("There are " + str(result01) + " words.")
'''

# initialize string
text01 = 'o, gato, caçava, o, rato'

# default separator: space
result = len(text01.split())





# initialize string
text = "o, gato, caçava, o, rato "
substring = " caçava, o, rato"

total= text.count(substring)
print(total)