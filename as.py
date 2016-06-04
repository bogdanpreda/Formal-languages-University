
reguli = [{'a': [0, 1], 'b': [0]}, {'a': [1], 'b': [2]}, {'a': [2], 'b': [2]}]
print reguli

print "-" * 50


def gen(cuvant, curent, stare, nivel, reguli):
    #print "===", cuvant, "c ", curent,"s", stare,"n", nivel
    if nivel > len(cuvant) -1:
        if cuvant == curent:
            if stare ==2:
                print   "starea s", stare, "este stare finala"

            else:
                print  "starea s", stare, "nu este stare finala"
                #print curent[0], "->", "s", stare

        return

    start = int(stare)
    v = cuvant[nivel]

    for state in reguli[start][v]:
        if nivel +1 > len(cuvant) - 1:
            aux = str(curent) + str(v)
            if aux == cuvant:
                print v, "->", "s", state

        else:
            print v, "->", "s", state

        curent = curent + v

        gen(cuvant, curent, state, nivel + 1, reguli)
        curent = ''

cuvant = "abb"
cuvant = "aab"
cuvant = "aba"
#cuvant = "bba"
#cuvant = "baa"

gen(cuvant, '', 0, 0, reguli)

