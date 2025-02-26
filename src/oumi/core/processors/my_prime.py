def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def next_prime(n):
    next_number = n + 1
    while not is_prime(next_number):
        next_number += 1
    return next_number