cases = int(input())

for _ in range(cases):
    foods = {}
    entries = int(input())
    for _ in range(entries):
        food, weight = map(int, input().split())

        foods.setdefault(food, [0,])
        foods[food].append(weight)

    food_weights = []
    for key, val in foods.items():
        ideal = [i for i in val if 10 <= i <= 100]
        if len(ideal) == 0:
            food_weights.append(max(val))
        else:
            food_weights.append(max(ideal))
    print(sum(food_weights))