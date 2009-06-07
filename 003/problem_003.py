#!/usr/bin/python
import math
import sys

solve_num = 600851475143
solve_num_sqrt = int(math.ceil(math.sqrt(solve_num)))

primes = [2,3]
number = 4
cursor_prime = 2

def get_next_prime():
    global number, primes
    while True:
        for prime in primes:
            if number%prime == 0:
                primes.append(number)
                number += 1
                return number
        number += 1

max = 0
while cursor_prime < solve_num_sqrt:
    cursor_prime = get_next_prime()
    while solve_num % cursor_prime == 0:
        solve_num /= cursor_prime
        if solve_num == 1:
            print "Solution 003: " + str(cursor_prime)
            sys.exit(0)
        max = cursor_prime

