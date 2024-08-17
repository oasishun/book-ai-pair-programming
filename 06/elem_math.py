import random

def generate_math_problem():
    # Define the types of problems
    operations = ['+', '-', '*', '/']
    
    # Randomly select an operation
    operation = random.choice(operations)
    
    # Generate random numbers for the problem
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    
    # Ensure no division by zero
    if operation == '/':
        num2 = random.randint(1, 10)
        # Ensure the division result is an integer
        num1 = num2 * random.randint(1, 10)
    
    # Create the problem string
    problem = f"{num1} {operation} {num2}"
    
    return problem

# Example usage
for _ in range(10):
    print(generate_math_problem())
    