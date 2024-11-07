def fib(n, mod):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append((fib[i - 1] + fib[i - 2]) % mod)
    return fib[n]


while True:
    try:
        n = input().split()
        n1 = int(n[0])
        n2 = int(n[1])
        print(int(fib(fib(n1, n2), n2)))
    except EOFError:
        break