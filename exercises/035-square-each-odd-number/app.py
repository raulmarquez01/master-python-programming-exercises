def square_odd_numbers(s):
    nums = [int(n) for n in s.split(",")]
    result = [n ** 2 for n in nums if n % 2 != 0]
    return result

print(square_odd_numbers("1,2,3,4,5,6,7,8,9"))
