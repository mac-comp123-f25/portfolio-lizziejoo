def count_words(word, s):
    words = s.split()
    return words.count(word)

print(count_words("Ban", "Ban in Banana"))