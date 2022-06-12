def check(word):
    return word.islower() or word.isupper() or (word[0].isupper() and word[0:].islower())


word = "USSR"
print(word, check(word))

word = "fSSR"
print(word, check(word))

word = "goodworkman"
print(word, check(word))

word = "Fatherbot"
print(word, check(word))