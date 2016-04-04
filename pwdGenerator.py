import string
import random
import sys

print("=======================================")
print("|    Password generator in Python.    |")
print("|     Copyright by 'badand' 2015.     |")
print("|       http://badand.github.io       |")
print("=======================================")
print()


######## DEFINITIONS - modify at your will ############
includeUpperLetters = True
includeLowerLetters = True
includeDigits = True
includeSpecialChars = True
excludeSimilarChars = True
passwordLength = 12
passwordCount = 10

######## IMPLEMENTATION - avoid modification ############
chars = ""
if includeUpperLetters:
    chars = chars + string.ascii_lowercase;
if includeUpperLetters:
    chars = chars + string.ascii_uppercase;
if includeDigits:
    chars = chars + string.digits;
if includeSpecialChars:    
    chars = chars + '_-$!?%#&@';
if excludeSimilarChars:
    chars = "".join(c for c in chars if c not in "ilI1oO0Z25SG68&q9g")

print("Generated passwords:")
for num in range(1,passwordCount):
    print(''.join(random.choice(chars) for _ in range(passwordLength)))
    pass