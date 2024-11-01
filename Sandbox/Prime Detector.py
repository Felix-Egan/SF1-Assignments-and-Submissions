n  = int(input("Prime Check: "))
def is_prime(n):
    if n <= 1 or n % 2 == 0 or n % 3 == 0 or str(n)[-1] in "024568":
        return False
    if n <= 3:
        return True
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return f"False: divisible by {i} or {i + 2}"
        i += 6
    return True
print("Is Prime? ", is_prime(n))