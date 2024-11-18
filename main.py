import helpers as h
import random

wordsFile = open('wordsSorted.txt', 'r')

wordsList = wordsFile.readlines()

for i in range(len(wordsList)):
    wordsList[i] = wordsList[i][0:5]

print(wordsList)
print(len(wordsList))

guess = random.choice(wordsList)

while True:
    print("\nGuess:", guess)
    if len(wordsList) == 1:
        print("This must be the correct answer!")
        break

    result = input("Result (5-digit sequence): ")
    if result == "22222":
        print("Congrats! Correct word")
        break

    idx = 0
    while idx < len(wordsList):
        # assume each word in wordsList to be the correct answer
        # then check if the guess+correct combo would've produced the same result
        if h.compare(wordsList[idx], guess) != result:
            wordsList.pop(idx)
            idx -= 1
        idx += 1

    print()
    print(wordsList)
    print(len(wordsList))

    guess = random.choice(wordsList)



# def cond(word):
#     return (
#         ('c' not in word)
#         and ('r' not in word)
#         and ('n' not in word)
#         and (word[2] == 'a') and (word[0] == 'a')
#         and (word[4] == 'e')
#
#     )
#
# wordsListNew = []
#
# for word in wordsList:
#     if cond(word):
#         wordsListNew.append(word)
#
#
# print(wordsListNew)
# print(len(wordsListNew))
