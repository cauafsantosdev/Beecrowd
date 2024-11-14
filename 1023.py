city_n = 0
while True:
    total_houses = int(input())

    if total_houses == 0:
        break
    else:
        city_n += 1
        people = 0
        water_used = 0
        consume_groups = {}

        for _ in range(total_houses):
            house_people, house_water = map(int, input().split())
            floor_house_consume = house_water // house_people

            consume_groups.setdefault(floor_house_consume, 0)
            consume_groups[floor_house_consume] += house_people

            people += house_people
            water_used += house_water

        sorted_groups = sorted(consume_groups.items())
        water_consume = int(water_used / people * 100) / 100

        print(f"Cidade# {city_n}:")

        for group in sorted_groups:
            print(f"{group[1]}-{group[0]}", end=" ")
        print(f"\nConsumo medio: {water_consume:.2f} m3.")

        print() 
