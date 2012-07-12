def palindromic(N):
    return N == int(str(N)[::-1])



def find_largest_palindromic_simple(lower_bound, upper_bound):
    result = (0, 0, 0)

    for i in range(lower_bound, upper_bound + 1):
        for j in range(i, upper_bound + 1):
            p = i*j
            if palindromic(p) and p > result[0]:
                result = (p, i, j)
    return result



def find_largest_palindromic_fast(lower_bound, upper_bound):

    # The idea is to visit the products along the down/left diagonals
    # of the multiplication table, since this guarantees that we are
    # searching from the top down (i.e. looking at a monotonically
    # decreasing set of products).  Also, we only consider the lower
    # left half of the table, since the table is symmetric about the
    # diagonal.

    result = None

    # We visit each 'diagonal' element starting with (n,n) and going
    # left and up to (n,n-1), (n-1,n-1), etc.  We can compute this
    # implicitly as (floor((m+1)/2), floor(m/2)) where m starts at
    # 2*n
    for n in range(2*upper_bound, 2*lower_bound, -1):
        start = ((n + 1) // 2, n // 2)

        # Walk diagonally down and left from the starting point until
        # we hit the edge.
        for i in range(min(upper_bound - start[0] + 1,
                           start[1] - lower_bound + 1)):
            N = (start[0] + i) * (start[0] - i)
            if palindromic(N):
                result = (N, (start[0] + i), (start[0] - i))

        if result:
            return result



################################################################
if __name__ == '__main__':
    from time import time

    #L, U = 1000000, 9999999    # The fast one can compute this in 11s
    L, U = 100, 999

    t = time()
    print find_largest_palindromic_fast(L, U)
    print time() - t

    t = time()
    print find_largest_palindromic_simple(L, U)
    print time() - t
