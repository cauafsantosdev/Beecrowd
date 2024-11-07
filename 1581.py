def define_lang(people: int):
    languages = []

    for i in range(people):
        lang = input("")
        languages.append(lang)

    main = languages[0]
    languages.pop(0)

    for language in languages:
        if language != main:
            return "ingles"
        
    return main

cases = int(input(""))

for i in range(cases):
    people = int(input(""))
    print(define_lang(people))