def validador_tipico(prato):
    if prato in resultado_pratos:
        return resultado_pratos[prato]

    ingredientes = pratos[prato]
    tipicos_prato = sum(1 for item in ingredientes if item in tipicos or (item in pratos and validador_tipico(item)))

    resultado = tipicos_prato > len(ingredientes) / 2
    resultado_pratos[prato] = resultado
    return resultado


n_tipicos = int(input().strip())
tipicos = set(input().strip().split())

cases = int(input().strip())
resultados = []

pratos = {}
resultado_pratos = {}

for _ in range(cases):
    prato, n_ingredientes = input().strip().split()
    ingredientes = input().strip().split()

    pratos[prato] = ingredientes

for prato in pratos:
    if validador_tipico(prato):
        resultados.append("porcao tipica")
    else:
        resultados.append("porcao comum")

for resultado in resultados:
    print(resultado)