leds = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

n = int(input())

for _ in range(n):
    numero = input().strip()

    resposta = 0
    for digito in numero:
        resposta += leds[int(digito)]

    print(f"{resposta} leds")