products = []
small = 1000
step = 100
palendrome = None

def f(start):
    for i in range(start,start+100):
        for j in range(start,start+100):
            products.append(i*j)
    products.sort(cmp=lambda x,y:y-x)

while palendrome == None and small > 0:
    small=small-step
    f(small)
    for num in products:
        if ("%d"%num)[::-1] == ("%d"%num):
            palendrome = num
            break

print palendrome
