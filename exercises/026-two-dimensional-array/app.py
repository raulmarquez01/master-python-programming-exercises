def two_dimensional_list(x, y):
    result = []
    for i in range(x):
        row = []
        for j in range(y):
            row.append(i * j)
        result.append(row)
    print(result)

two_dimensional_list(3, 5)
