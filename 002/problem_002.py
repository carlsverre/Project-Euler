
def fib():
    sequence = [1,1]
    last=1
    while sum(sequence[last-1:last+1]) < 4000000:
        sequence.append(sum(sequence[last-1:last+1]))
        last+=1;
    return sequence

seq = fib()
print sum(filter(lambda x: not x%2, seq))
