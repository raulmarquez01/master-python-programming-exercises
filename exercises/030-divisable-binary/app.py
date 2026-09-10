def divisible_binary(s):
    parts = s.split(",")
    result = []
    for p in parts:
        decimal = int(p, 2)
        if decimal % 5 == 0:
            result.append(p)
    print(",".join(result))

divisible_binary("0100,0011,1010,1001")
