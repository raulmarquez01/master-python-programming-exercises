def number_of_uppercase(s):
    counts = {"upper": 0, "lower": 0}
    for c in s:
        if c.isupper():
            counts["upper"] += 1
        elif c.islower():
            counts["lower"] += 1
    print(f"UPPERCASE {counts['upper']}")
    print(f"LOWERCASE {counts['lower']}")

number_of_uppercase("Hello world!")
