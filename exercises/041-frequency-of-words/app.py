def compute_word_frequency(text):
    words = text.split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    for word in sorted(frequency):
        print(f"{word}: {frequency[word]}")

compute_word_frequency("New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.")
