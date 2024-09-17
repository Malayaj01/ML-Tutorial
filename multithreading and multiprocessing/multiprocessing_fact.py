import multiprocessing
import multiprocessing.pool
import time
import sys
import math 

sys.set_int_max_str_digits(100000)

def factorial(number):
    print(f"Computing factorial of {number}")
    result = math.factorial(number)
    print(f"Factoorial of {number} is {result}")
    return result

if __name__ == "__main__":
    numbers = [500,600,700,800]

    start_time = time.time()

    with multiprocessing.Pool() as pool:
        results = pool.map(factorial,numbers)

    end_time = time.time()

    total_time = end_time - start_time
    print(total_time)