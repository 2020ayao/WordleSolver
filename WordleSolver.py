def rank(possible_words, letter_frequencies):
    scores = {}
    for word in possible_words:
        letters = list(word)
        for letter in letters:
            if word not in scores.keys():
                scores[word] = letter_frequencies[letter]
            else:
                scores[word] += letter_frequencies[letter]
    dict(sorted(scores.items(), key=lambda item: item[1]))
    return scores

def update(possible_words, lettersInWord, lettersNotInWord, lettersInWordRightPosition, letter_frequencies):
    for letter in lettersNotInWord:
        possible_words = [word for word in possible_words if letter not in word]

    for combo1 in lettersInWord:
        possible_words = [word for word in possible_words if len(word) == 5 and word[int(combo1[1]) - 1] != combo1[0] and combo1[0] in word]

    for combo in lettersInWordRightPosition:
        possible_words = [x for x in possible_words if len(x) == 5 and combo[0] == x[int(combo[1])-1]]

    # print(lettersNotInWord)
    # print(lettersInWord)
    # print(lettersInWordRightPosition)
    print()
    print("Narrowed down to: ", len(possible_words), "words.")

    scores = rank(possible_words, letter_frequencies)

    if (len(possible_words) > 0):
        word = list(scores.keys())[0]
        probability = list(scores.values())[0]
        print("Try: ", word)
        print("which has a probability of ", probability)
    else:
        print("No possible words exist")
        exit()
    if len(possible_words) < 10:
        print(possible_words)
    return possible_words

def solve(possible_words, lettersInWord, lettersNotInWord, lettersInWordRightPosition, letter_frequencies):
    while True:
        print()
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
        possible_words = update(possible_words, lettersInWord, lettersNotInWord, lettersInWordRightPosition, letter_frequencies )

def main():
    letter_frequencies = {}
    lettersInWord, lettersNotInWord, lettersInWordRightPosition = [], [], []
    possible_words = []
    c = 0
    f1 = open('frequency.txt')
    for line in f1:
        info = line.split(' ')
        if len(info) > 1:
            letter = info[0]
            frequency = float(info[1])
            letter_frequencies[letter] = frequency
    f1.close()
    fh = open('words.txt')
    for line in fh:
        possible_words.append(line[:-1])
    fh.close()
    print("Beginning with: ", len(possible_words), "words.")

    solve(possible_words, lettersInWord, lettersNotInWord, lettersInWordRightPosition, letter_frequencies)


if __name__ == "__main__":
    main()
