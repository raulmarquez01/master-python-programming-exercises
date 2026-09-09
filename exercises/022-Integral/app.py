def squares_dictionary(n):
    result = {}
    for i in range(1, n + 1):
        result[i] = i * i
    return result

print(squares_dictionary(8))
