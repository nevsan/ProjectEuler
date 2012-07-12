def get_largest_prime_factor(N):
    f = 1

    while N > 1:
        f += 1
        while N % f == 0:
            N /= f

    return f

if __name__ == '__main__':
    N = 600851475143
    print get_largest_prime_factor(N)
