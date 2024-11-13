def decodificar(texto, original, cifrado):
    texto_decifrado = ""
    for letra in texto:
        if letra.lower() in original:
            idx = original.index(letra.lower())
            if letra.isupper():
                texto_decifrado += cifrado[idx].upper()
            else:
                texto_decifrado += cifrado[idx].lower()

        elif letra.lower() in cifrado:
            idx = cifrado.index(letra.lower())
            if letra.isupper():
                texto_decifrado += original[idx].upper()
            else:
                texto_decifrado += original[idx].lower()

        else:
            texto_decifrado += letra

    return texto_decifrado

primeiro_caso = True
while True:
    try:
        entrada = input().strip()
        if not entrada:
            break
        cifra, textos = map(int, entrada.split())

        original = list(input().strip().lower())
        cifrado = list(input().strip().lower())

        lista_decifrada = []
        for _ in range(textos):
            texto = input().strip()
            lista_decifrada.append(decodificar(texto, original, cifrado))

        if not primeiro_caso:
            print()
        primeiro_caso = False

        for frase in lista_decifrada:
            print(frase)
    
    except EOFError:
        break

print()
