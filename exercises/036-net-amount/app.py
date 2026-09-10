def net_amount(s):
    parts = s.split()
    total = 0
    for i in range(0, len(parts), 2):
        op = parts[i]
        amount = int(parts[i + 1])
        if op == "D":
            total += amount
        elif op == "W":
            total -= amount
    return total

print(net_amount("D 300 D 300 W 200 D 100"))
