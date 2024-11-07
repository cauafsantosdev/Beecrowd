n = int(input())

for _ in range(n):
    cifrado = input().strip()
    deslocamento = int(input().strip())

    decodificado = []
    
    for letra in cifrado:
        valor_original = ord(letra)
        novo_valor = valor_original - deslocamento

        if novo_valor < ord('A'):
            novo_valor += 26
        
        decodificado.append(chr(novo_valor))
    
    print(''.join(decodificado))