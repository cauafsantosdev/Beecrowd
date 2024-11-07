def remove_zero(n: int):
    if n == 0:
        return None
    
    n = str(n).replace("0", "")
    return int(n)

while True:
    x, y = input("").split()
    s = int(x) + int(y)
    out = remove_zero(s)

    if out == None:
        break
    else:
        print(out)
