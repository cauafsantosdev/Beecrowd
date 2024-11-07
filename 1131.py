inter = 0
gremio = 0
empate = 0
grenais = 1

while True:
    gols_inter, gols_gremio = input().split()

    if int(gols_inter) > int(gols_gremio):
        inter += 1
    elif int(gols_gremio) > int(gols_inter):
        gremio += 1
    else:
        empate += 1

    print("Novo grenal (1-sim 2-nao)")
    x = int(input())

    if x == 1:
        grenais += 1
    elif x == 2:
        break

print(f"{grenais} grenais\nInter:{inter}\nGremio:{gremio}\nEmpates:{empate}")
print(f"Inter venceu mais" if inter > gremio else f"Gremio venceu mais" if gremio > inter else "Empate")