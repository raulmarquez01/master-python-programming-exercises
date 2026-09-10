def remove_duplicate_words(s):
    words = set(s.split())
    return " ".join(sorted(words))

print(remove_duplicate_words("hello world and practice makes perfect and hello world again"))
