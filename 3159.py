def discar(letra, teclas):
    for i in letra:
        for j in range(len(teclas)):
            if i in teclas[j]:
                return teclas[j][0], teclas[j].index(i)

teclas = [["1"], ["2", "a", "b", "c"], ["3", "d", "e", "f"], ["4", "g", "h", "i"], ["5", "j", "k", "l"], 
          ["6", "m", "n", "o"], ["7", "p", "q", "r", "s"], ["8", "t", "u", "v"], ["9", "w", "x", "y", "z"], ["0", " "]]

for i in range(int(input())):
    anterior = -1
    palavra = input().strip()
    for l in palavra:
        num, local = discar(l.lower(), teclas)
        
        if l.isupper():
            print("#", end="")
        elif anterior == num:
            if anterior != -1:
                print("*", end="")
        
        print(f"{str(num) * int(local)}", end="")
        anterior = num

    print()
