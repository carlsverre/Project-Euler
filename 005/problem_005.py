def lcm(x,y):
    return x*y/gcd(x,y)

def gcd(x,y):
    while y != 0:
        (x, y) = (y, x%y)
    return x

final = 2
for num in range(3,21):
    final = lcm(final,num)

print final
