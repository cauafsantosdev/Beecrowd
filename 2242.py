def funny(laugh: str):
    vowels = ["a", "e", "i", "o", "u"]
    laugh = [i for i in laugh if i in vowels]
    laugh = "".join(laugh)
    reversed_laugh = laugh[::-1]

    if laugh == reversed_laugh:
        return "S"
    
    return "N"

laugh = input("")
print(funny(laugh))