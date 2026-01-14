from typing import List
import time
import functools

Matrix = List[List[int]]


def task_1(exp: int):
    def power(base: int):
        return base ** exp
    return power

def task_2(*args, **kwargs):
    for arg in args:
        print(arg)
    for value in kwargs.values():
        print(value)

def helper(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Hi, friend! What's your name?")
        func(*args, **kwargs)
        print("See you soon!")
    return wrapper

@helper
def task_3(name: str):
    print(f"Hello! My name is {name}.")

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__} in {run_time:.4f} secs")
        return result
    return wrapper

@timer
def task_4():
    return len([1 for _ in range(0, 10**7)])

def task_5(matrix: Matrix) -> Matrix:
    if not matrix or not matrix[0]: 
        return []
    # Simplified version for online compilers
    result = []
    for c in range(len(matrix[0])):
        new_row = []
        for r in range(len(matrix)):
            new_row.append(matrix[r][c])
        result.append(new_row)
    return result


# Task 1 check
growth_calculation = task_1(2) 
print(growth_calculation(1.05))

# Task 2 check
task_2(5000, 200, 150, date="2026-01-14", currency="AMD")

# Task 3 check
task_3("Lianna")

# Task 4 check
task_4()

# Task 5 check
portfolio = [[100, 200], [110, 210]]
print(task_5(portfolio))
