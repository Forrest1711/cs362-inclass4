def wordCount(str):
    # str = input("Gimme a sentence with some words and I'll tell you how many words it has: ")

    charCount = 0
    wordCount = 0

    for i in range(0, len(str)):
        char = str[i]
        if char.isalpha():
            charCount += 1
        elif charCount > 0 and char == ' ':
            charCount = 0
            wordCount += 1
        if charCount > 0 and i >= len(str)-1:
            charCount = 0
            wordCount += 1

    # print(wordCount)
    return wordCount
