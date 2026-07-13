def calculate_love_score(name1,name2):
    TrueScore = 0
    T = 0
    R = 0
    U = 0
    E = 0
    for letter in (name1+name2):
        if letter.upper() == "T":
            T += 1
        if letter.upper() == "R":
            R += 1
        if letter.upper() == "U":
            U += 1
        if letter.upper() == "E":
            E += 1
        TrueScore = T + R + U + E
    LoveScore = 0
    L = 0
    O = 0
    V = 0
    E = 0
    for letter in (name1+name2):
        if letter.upper() == "L":
            L += 1
        if letter.upper() == "O":
            O += 1
        if letter.upper() == "V":
            V += 1
        if letter.upper() == "E":
            E += 1
        LoveScore = L + O + V + E
    return int(str(TrueScore) + str(LoveScore)) 


print("\n" + str(calculate_love_score("Kanye West", "Kim Kardashian")))