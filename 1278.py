lista = []
espacos = []

while True:
    n = int(input())
    if n == 0:
        break
    else:
        temporario = []
        caracteres = 0

        for i in range(n):
            frase = input().strip()
            temporario.append(" ".join(frase.split()))

        lista.append(temporario)
        caracteres = len(max(temporario, key=len))
        espacos.append(caracteres)


for idx, texto in enumerate(lista):
    justificar = espacos[idx]
    
    for frase in texto:
        print(f"{frase.rjust(justificar)}")

    if idx < len(lista) - 1:
        print() 