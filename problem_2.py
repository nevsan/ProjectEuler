def fibonacci(max_val):
    x0, x1 = 1, 2

    yield x0
    while x1 <= max_val:
        yield x1
        x0, x1 = x1, x0 + x1

if __name__ == '__main__':
    print sum([x for x in fibonacci(4e6) if x % 2 == 0])
