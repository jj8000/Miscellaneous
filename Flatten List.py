l = [2, 88, [], [4, 5, 0, [5, 7]], 4, 4, 9022, [6, 7, 0], [1], [8, [7], [[[77]]], 90, [0, [23, 67, [76, 6, [5], 8],]], 0], 11]
splaszczona_lista = []

def splaszcz(arg):

    for i in arg:
        if type(i) is not list:
            splaszczona_lista.append(i)
        else:
            splaszcz(i)
    return(splaszczona_lista)

print(splaszcz(l))