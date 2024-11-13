gago = list(input())

for i in range(len(gago)):
    if i+3 < len(gago):
        if gago[i] + gago[i+1] == gago[i+2] + gago[i+3]:
            gago.pop(i+1)
            gago.pop(i)

print("".join(gago))