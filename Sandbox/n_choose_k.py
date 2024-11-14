import math
def combination(n, k):
    if k > n:
        return 0
    return math.comb(n, k)  # Available in Python 3.8 and later
# Example usage
n = int(input("Enter the total number of elements: "))
k = int(input("Enter the number of elements to choose: "))
result = combination(n, k)
print(f"Number of combinations: {result}")