n  = int(input("Prime Check: "))

def is_prime(n):
    if n <= 1 or n % 2 == 0 or n % 3 == 0 or str(n)[-1] in "024568":
        return f"False: Negative, Even, Divisible by 2 or 3, or ends in 0, 2, 4, 6, 8"
    if n <= 3:
        return "True"
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return f"False: divisible by {i} or {i + 2}"
        i += 6
    return "True"

print("Is Prime? ", is_prime(n))

def regex_is_prime(n):
    import re
    if re.match(r'^1?$|^(11+?)\1+$', '1' * n):
        return "False: Negative, Even, Divisible by 2 or 3, or ends in 0, 2, 4, 6, 8"
    return "True"

print("Is Prime? [REGEX] ", regex_is_prime(n))