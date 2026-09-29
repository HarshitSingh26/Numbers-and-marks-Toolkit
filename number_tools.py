def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


def fibonacci(n):
    series = []
    a = 0
    b = 1
    for i in range(n):
        series.append(a)
        a, b = b, a + b      
    return series


def reverse_number(n):
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return rev


def to_base(n, base):
    digits = "0123456789ABCDEF"
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        result = digits[n % base] + result
        n = n // base
    return result


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def generate_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes


def smallest_divisor(n):
    if n % 2 == 0:
        return 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return d
        d += 2
    return n


def prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n = n // d
        d += 1
    if n > 1:
        factors.append(n)
    return factors


def square_root(n):
    if n == 0:
        return 0
    guess = n / 2
    for i in range(20):
        guess = (guess + n / guess) / 2
    return guess
