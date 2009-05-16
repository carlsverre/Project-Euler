import math

def primes_up_to_n(n):
    primes = [2,3]
    start = 4
    for num in range(start,n):
        nap = 0
        for prime in primes:
            if num % prime == 0:
                nap=1
                break
            if prime**2 > num:
                break
        if nap != 1:
            primes.append(num)

    return primes

solve_num = 600851475143
solve_num_sqrt = int(math.ceil(math.sqrt(solve_num)))

p = primes_up_to_n(solve_num_sqrt)
p.reverse()

for prime in p:
    if solve_num % prime == 0:
        print prime
        break

