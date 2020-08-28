import math


# 1
# bub = [i for i in range(1000) if i % 3 is 0 or i % 5 is 0]


# 2
def fib_sum(halt: int) -> int:
    one, two, sum = 1, 2, 0
    while two <= halt:
        if two % 2 is 0:
            sum += two
        one, two = two, one + two
    return sum


# print(fib_sum(4000000))

# 3
def primes(num: int) -> list:
    prim_list = [1]
    i = 2
    while i <= num:
        if num % i is 0:
            prim_list.append(i)
            num //= i
            i -= 1
        i += 1
    return prim_list


# print(primes(600851475143))

# 4
def is_pal(num: int) -> bool:
    nummy = str(num)
    for i in range(len(nummy) // 2):
        if not nummy[i] is nummy[-(i + 1)]:
            return False
    return True


def test_pal():
    biggest = 0
    for i in range(100, 999):
        for j in range(100, 999):
            if i * j > biggest and is_pal(i * j):
                biggest = i * j
    return biggest


# print(test_pal())

# 5
def factorize(n: int) -> dict:
    """returns a numbers prime factors and their powers in a dictionary"""
    out = {}
    i = 2
    while i <= n:
        if n % i is 0:
            try:
                out[i] += 1
            except KeyError:
                out[i] = 1
            n = n // i
            i -= 1
        i += 1
    return out


def smallest_multiple(n):
    """returns the smallest number that is evenly divisible by all numbers from 2 to n"""
    factors = {i: 0 for i in range(2, n + 1)}
    for j in range(2, n + 1):
        for n, p in factorize(j).items():
            if factors[n] < p:
                factors[n] = p
    multis = [pow(i, j) for i, j in factors.items() if j != 0]
    out = 1
    for i in multis:
        out *= i
    return out


# print(smallest_multiple(20))


# 6
def square_sum_diff(wall: int) -> int:
    sq = sum([i * i for i in range(1, wall + 1)])
    ds = sum([i for i in range(1, wall + 1)])
    return ds * ds - sq


# print(square_sum_diff(100))

# 7
def is_prime(cand: int) -> bool:
    for j in [2, 3, 5, 7, 10]:
        if cand % j == 0:
            return False
    factors = [power for power in factorize(cand).values()]
    return len(factors) == 1 and factors[0] == 1


def make_nth_prime(which: int) -> int:
    i, j = 0, 1
    while i <= which:
        if is_prime(j):
            i += 1
        j += 1
    return j - 1


# print(make_nth_prime(101))


# 8
def m_prod(number: int, how_many: int) -> int:
    nummy = str(number)
    max_prod = 0
    for j in range(len(nummy) - how_many):
        curr_prod = 1
        for i in range(j, j + how_many):
            curr_prod *= int(nummy[i])
        max_prod = curr_prod if curr_prod > max_prod else max_prod
    return max_prod


# print(m_prod())

# 9
def is_trip(a: int, b: int, c: int) -> bool:
    return a * a + b * b == c * c


def find_triplet(all_sum: int) -> int:
    i = 1
    while i <= all_sum:
        j = 1
        while i + j <= all_sum:
            k = all_sum - i - j
            if is_trip(i, j, k):
                return i * j * k
            j += 1
        i += 1


# print(find_triplet(1000))


# 10
def sum_prim(stop: int) -> int:
    primo = {i: True for i in range(stop + 1)}
    primo[0] = primo[1] = False
    primes = []
    for i in primo:
        if primo[i]:
            if is_prime(i):
                primes.append(i)
                for j in range(2 * primes[-1], stop + 1, primes[-1]):
                    primo[j] = False
    return sum(primes)


# print(sum_prim(20000))

# 11


# 12
def divisors(n: int) -> int:
    factors = [i + 1 for i in factorize(n).values()]
    out = 1
    for i in factors:
        out *= i
    return out - 1


def search_tri(bloing: int):
    j = 1
    for i in range(2, 15000):
        if divisors(j) >= bloing:
            return j
        j += i


# print(search_tri(500))
# 14
from CollatzTree import Branch

for i in range(1, 10):
    print(i, ":", Branch(i))
