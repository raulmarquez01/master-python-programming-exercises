def sequence_of_words(s):
    words = s.split(",")
    words.sort()
    print(", ".join(words))

sequence_of_words("without,hello,bag,world")
