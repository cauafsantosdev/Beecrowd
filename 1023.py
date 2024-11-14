from math import floor

def get_water_consume(people: int, water_used: int):
    return water_used / people


all_cities_data = []
all_consumes = []
while True:
    total_houses = int(input())

    if total_houses == 0:
        break
    else:
        people = 0
        water_used = 0
        consume_groups = {}

        for _ in range(total_houses):
            house_people, house_water = map(int, input().split())
            floor_house_consume = int(get_water_consume(house_people, house_water))

            if floor_house_consume not in consume_groups.keys():
                consume_groups[floor_house_consume] = house_people
            else:
                consume_groups[floor_house_consume] += house_people

            people += house_people
            water_used += house_water

        all_cities_data.append(sorted(consume_groups.items(), key=lambda item: item[0]))

        media_consumo = get_water_consume(people, water_used)
        media_consumo_truncado = floor(media_consumo * 100) / 100
        all_consumes.append(media_consumo_truncado)

city_n = 0

for city in all_cities_data:
    city_n += 1
    print(f"Cidade# {city_n}:")

    for group in city:
        print(f"{group[1]}-{group[0]}", end=" ")
    print(f"\nConsumo medio: {all_consumes[city_n - 1]:.2f} m3.")

    if city_n != len(all_cities_data):
        print()