def all_digits_even():
    result = []
    for num in range(1000, 3001):
        if all(int(d) % 2 == 0 for d in str(num)):
            result.append(str(num))
    print(",".join(result))

all_digits_even()
