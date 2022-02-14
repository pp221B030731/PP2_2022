def spy_game(l):
    f1 = True
    f2 = True
    for i in range(len(l)):
        if l[i] == 0:
            f1 = False
        if l[i] == 0 and f1 == False:
            f2 = False
        if l[i] == 7 and f1 == False and f2 == False:
            return True
    return False