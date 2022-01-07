# Sort out the input list ending with special character according to the following weights if the symbols

# Weight of the symbols
# @ - 3
# * - 2
# # - 1
# $ - 0

# Input
# ['abc#','def*','ghi@','jkl$','mno:','pqr#']

# Output
# ['ghi@','def*','abc#''jkl$','mno:','pqr#']

# * Sorting should be done for list sets before and after the : keyword
# * If a special word repeats, maintain original order

def flo_sorting(list):
    length = len(list)
    i = 0
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0

    list2 = []
    newlist = []

    while i != length:
        if list[i][-1] == ':':
            e = list[i]
            list2 = list[i+1:]
            list2 = flo_sorting(list2)
            break
        elif list[i][-1] == '#':
            a = list[i]
        elif list[i][-1] == '*':
            b = list[i]
        elif list[i][-1] == '$':
            c = list[i]
        elif list[i][-1] == '@':
            d = list[i]
        else:
            break
        i = i+1
    if d != 0:
        newlist.append(d)
    if b != 0:
        newlist.append(b)
    if a != 0:
        newlist.append(a)
    if c != 0:
        newlist.append(c)
    if e != 0:
        newlist.append(e)
    if list2 == []:
        return newlist
    else:
        newlist = newlist+list2
        return newlist


input = ['jkl$', 'def*', 'abc#', 'ghi@', 'mno:', 'pqr#', 'jkl$', 'def*']

print(flo_sorting(input))
