def list_and_tuple(*args):
    str_values = [str(n) for n in args]
    print(str_values)
    print(tuple(str_values))

list_and_tuple(34,67,55,33,12,98)
