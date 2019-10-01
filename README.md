# pwd-generator
Easy-to-use password generator for random mid-strong passwords in Python

## Usage
Prerequisities:
 - installed Python

Run `pwdGenerator.py` on *command line*.
The script prints 10 passwords with 12 character length.
To tweak the generator, edit with any text file and modify the `DEFINITIONS` section. These options are available for easy modification:
 - includeUpperLetters = if true letters with upper case (ABCD...) will be included in the result
 - includeLowerLetters = if true letters with upper case (abcd...) will be included in the result
 - includeDigits = if true digits (1234...) will be included in the result
 - includeSpecialChars = if true special characters ($!?%#...) will be included in the result
 - excludeSimilarChars = if true similar letters/digits/characters (lI1oO0...) will be excluded - prevents confusion when writing the password down on the paper (never write passwords on paper!)
 - passwordLength = number of characters the password will have
 - passwordCount = number of total passwords printed out to choose from
