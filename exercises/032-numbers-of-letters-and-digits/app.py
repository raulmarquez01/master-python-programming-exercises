def letters_and_digits(s):
    counts = {"letters": 0, "digits": 0}
    for c in s:
        if c.isalpha():
            counts["letters"] += 1
        elif c.isdigit():
            counts["digits"] += 1
    print(f"LETTERS {counts['letters']}")
    print(f"DIGITS {counts['digits']}")

letters_and_digits("hello world! 123")
