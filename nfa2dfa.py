'''
f(s0,a) = {s0, s1}
f(s0,b) = s0
f(s1,a) = 0
f(s1,b) = s2
f(s2, a) = s2
f(s2,b) = s2
'''
from copy import deepcopy
traiectorii = {('0', 'a'): ['0', '1'], ('0', 'b'): '0', ('1', 'a'): '0', ('1', 'b'): '2', }
letters = ['a', 'b']
nodes = ['0']
nodes_frequency = [0]
state = 0
char = 'a'

def addToList(list_of_strings, str_to_add):
    if str_to_add not in list_of_strings:
        list_of_strings.append(str_to_add)
        return True
    return False

nodes2 = deepcopy(nodes)
print nodes
def recursivity(traiectorii, nodes, )
for n in range(len(nodes2)):
    if nodes_frequency[n] == 0:
        nodes_frequency[n] = nodes_frequency[n] + 1

        for ch in letters:
            print ch, '->', traiectorii[(nodes2[n], ch)]
            if(addToList(nodes, traiectorii[(nodes2[n], ch)])):
                nodes_frequency.append(0)
            nodes2 = deepcopy(nodes)
            print nodes
            print nodes_frequency

#print nodes


while n < len(nodes):

#if len(nodes[n]) > 1:
    for k in range(len(nodes[n])):
        for ch in letters:
            if traiectorii[(nodes[n][k], ch)] == 'none':
                continue
            print ch,'->', 's', traiectorii[(nodes[n][k], ch)]
            if(add_unique(nodes, traiectorii[(nodes[n][k], ch)])):
                nodes_frequency_index += 1
            print nodes

    n = n+1
