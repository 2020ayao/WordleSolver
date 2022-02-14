def update(possible_words, lettersInWord, lettersNotInWord, lettersInWordRightPosition):
    for letter in lettersNotInWord:
        possible_words = [word for word in possible_words if letter not in word]

    for combo1 in lettersInWord:
        possible_words = [word for word in possible_words if word[int(combo1[1]) - 1] != combo1[0] and combo1[0] in word]

    for combo in lettersInWordRightPosition:
        possible_words = [x for x in possible_words if combo[0] == x[int(combo[1])-1]]

    print(lettersNotInWord)
    print(lettersInWord)
    print(lettersInWordRightPosition)
    print("Narrowed down to: ", len(possible_words))
    print(possible_words)
    if (len(possible_words) > 0):
        print("Try: ", possible_words[0])
    else:
        exit()
    return possible_words

def solve(possible_words, lettersInWord, lettersNotInWord, lettersInWordRightPosition, possible_guesses):
    tries = 6
    while True:
        a = input("Letters in Word (a,#) (b,#): ")
        b = input("Letters Not In Word: ")
        c = input("Letters In Word & Right Position (a,#) (b,#): ")
        if a != "":
            key = a.split(" ")
            for element in key:
                lettersInWord.append([element[1], element[3]])
        if b != "":
            lettersNotInWord += list(b)
        if c != "":
            key = c.split(" ")
            for element1 in key:
                lettersInWordRightPosition.append([element1[1], element1[3]])
        possible_words = update(possible_words, lettersInWord, lettersNotInWord, lettersInWordRightPosition)
        tries -= 1

def main():
    possible_guesses = []
    lettersInWord, lettersNotInWord, lettersInWordRightPosition = [], [], []
    possible_words = []
    c = 0
    fh = open('words.txt')
    for line in fh:
        possible_words.append(line)
    fh.close()

    print(possible_words)
    print(len(possible_words))
    solve(possible_words, lettersInWord, lettersNotInWord, lettersInWordRightPosition, possible_guesses)

if __name__ == "__main__":
    main()