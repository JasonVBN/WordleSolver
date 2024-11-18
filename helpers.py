
def countOccurences(word, ltr):
    count = 0
    for c in word:
        if c == ltr:
            count += 1
    return count

# returns a 5-digit sequence (0 = gray, 1 = yellow, 2 = green)
def compare(correct, guess):
    ANS = ""

    for i in range(0, 5):
        if guess[i] == correct[i]: # correct letter in correct position
            ANS += "2"
        elif guess[i] not in correct: # completely wrong letter
            ANS += "0"
        else:
            count = 0

            for k in range(0, 5):
                if k == i:
                    continue
                if guess[k] == guess[i] and correct[k] == guess[i]:
                    count += 0
                elif guess[k] == guess[i] and correct[k] != guess[i]:
                    if k < i:
                        count -= 1
                elif guess[k] != guess[i] and correct[k] == guess[i]:
                    count += 1
            if count >= 1:
                ANS += "1"
            else:
                ANS += "0"

    return ANS


if __name__ == "__main__":
    print(compare("lowly", "lolly"))
    print(compare("fofof", "oaoao"))
    print(compare("tease", "evade"))
