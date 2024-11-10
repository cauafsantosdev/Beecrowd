def battle(ip: int, pc: int, na: int, monsters: list) -> bool:
    if len(monsters) == 0:
        return True
    
    low = pc - ip
    high = pc + ip
    fighters = [monster[0] for monster in monsters if monster[0] >= low and monster[0] <= high]

    if len(fighters) <= na:
        return True
    return False


while True:
    try:
        ip, team = input().split()
        ip = int(ip)
        team = int(team)
    except EOFError:
        break

    monsters = []
    
    for _ in range(team):
        pc, na = map(int, input().split())

        if battle(ip, pc, na, monsters):
            monsters.append((pc, na))
    
    print(len(monsters))