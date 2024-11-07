rounds = int(input())

for _ in range(rounds):
    bonus = int(input())
    atq1, def1, lvl1 = map(int, input().split())
    atq2, def2, lvl2 = map(int, input().split())

    golpe1 = (atq1 + def1) / 2
    if lvl1 % 2 == 0:
        golpe1 += bonus
    
    golpe2 = (atq2 + def2) / 2
    if lvl2 % 2 == 0:
        golpe2 += bonus

    if golpe1 > golpe2:
        print("Dabriel")
    elif golpe2 > golpe1:
        print("Guarte")
    else:
        print("Empate")