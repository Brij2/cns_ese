import math

# Function to calculate the modular multiplicative inverse
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Function to find the solution using Chinese Remainder Theorem
def chinese_remainder_theorem(n, a):
    # Calculate N
    N = math.prod(n)

    # Calculate x values
    x = [N // ni for ni in n]

    # Calculate the modular inverses
    inverses = [mod_inverse(x[i], n[i]) for i in range(len(n))]

    # Calculate the solution
    result = 0
    for i in range(len(n)):
        result += (a[i] * x[i] * inverses[i])

    return result % N

# Get user input for the moduli and remainders
n = []
a = []
num_equations = int(input("Enter the number of equations: "))

for i in range(num_equations):
    n_i = int(input(f"Enter modulus (n{1 + i}): "))
    a_i = int(input(f"Enter remainder (a{1 + i}): "))
    n.append(n_i)
    a.append(a_i)

# Calculate the solution using the Chinese Remainder Theorem
solution = chinese_remainder_theorem(n, a)
print("Solution:", solution)

