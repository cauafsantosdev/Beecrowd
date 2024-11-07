def word_checker(word: str):
    one = ["o", "n", "e"]
    two = ["t", "w", "o"]

    if len(word) == 3:
        for_one = 0
        for_two = 0

        for i in range(len(word)):
            if word[i] in one[i]:
                for_one += 1
            elif word[i] in two[i]:
                for_two += 1

            if for_one == 2:
                return 1
            elif for_two == 2:
                return 2
                
    return 3

cases = int(input(""))

for i in range(0, cases):
    word = input("")
    print(word_checker(word))