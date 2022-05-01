import random

#The words in this list come from http://www.merriam-webster.com/top-ten-lists/top-10-funny-sounding-and-interesting-words/bumfuzzle.html
words = {'bumfuzzle': 'confuse; perplex; fluster', 'cattywampus': 'askew, awry, kitty-corner', 'taradiddle': 'a fib or pretentious nonsense', 'billingsgate': 'coarsely abusive language', 'snickersnee': 'a large knife', 'widdershins': 'in a left-handed or contrary direction; counterclockwise', 'collywobbles': 'pain in the abdomen and expecially in the stomach; a bellyache', 'dipthong': 'two vowel sounds joined in one syllable to form one speech sound, e.g. the sounds of "ou" in out and of "oy" in boy'}

for i in words:
    print(i)

print()
print('Which of the words above would you like to know the definition of?')

word = input().lower()

while word not in words:
    print("That didn't match any of the words in the dictionary.")
    print("Please try again.")
    word = input().lower()

print(words[word])
