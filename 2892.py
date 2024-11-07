from math import lcm


while True:
    times = input()

    if times != "0 0 0":
        times = times.split()
        total = int(times[0])
        bike1 = int(times[1])
        bike2 = int(times[2])

        divisors = []
        for i in range(1, int(total**0.5) + 1):
            if total % i == 0:
                divisors.append(i)
                if i != total // i:
                    divisors.append(total // i)
            
        possibilities = []
        for i in divisors:
            if lcm(bike1, bike2, i) == total:
                possibilities.append(i)
        
        print(" ".join(map(str, sorted(possibilities))))
    else:
        break
