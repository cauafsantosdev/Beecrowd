while True:
    try:
        n = input().split()
        print(int(n[0]) ^ int(n[1]))
    except EOFError:
        break