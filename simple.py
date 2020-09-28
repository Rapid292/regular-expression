import re
from re import match

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat 
mat
bat
pat
'''

sentence = 'Start a sentence and then bring it to an end'

# pattern = re.compile(r'defg')
# pattern = re.compile(r'\.')
# pattern = re.compile(r'coreyms\.com')
# pattern = re.compile(r'^Start')
# pattern = re.compile(r'end$')
# pattern = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d')
# pattern = re.compile(r'[a-zA-Z1-9]')
# pattern = re.compile(r'[^b]at')
# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
pattern = re.compile(r'(Mr|Mrs|Ms)\.?\s[A-Z]\w*')
# pattern = re.compile(r'sentence')
# pattern = re.compile(r'start', re.IGNORECASE)



matches = pattern.finditer(text_to_search)
# matches = pattern.findall(text_to_search)
# matches = pattern.match(Start) #Search at starting of sentence only and return first matching object else None 
# matches = pattern.search(sentence)





print(matches)

for match in matches:   
    print(match)

# with open('data.txt', 'rt', encoding='utf-8') as f:
#     contents = f.read()

#     matches = pattern.finditer(contents)

#     for match in matches:   
#         print(match)



# print(r'\tTab')

# print(text_to_search[214:215])