def euclidean_algorithm(a, b):
    while b:
        a, b = b, a % b
    return a

def extended_euclidean_algorithm(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = extended_euclidean_algorithm(b % a, a)
        return (gcd, y - (b // a) * x, x)

# Get user input for the two numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Calculate the GCD using the Euclidean Algorithm
gcd = euclidean_algorithm(a, b)
print(f"GCD of {a} and {b} is {gcd}")

# Calculate the GCD, x, and y using the Extended Euclidean Algorithm
gcd, x, y = extended_euclidean_algorithm(a, b)
print(f"GCD of {a} and {b} is {gcd}")
print(f"x: {x}, y: {y}")
