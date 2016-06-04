'''
f(s0,a) = {s0, s1}
f(s0,b) = s0
f(s1,a) = 0
f(s1,b) = s2
f(s2, a) = s2
f(s2,b) = s2
'''
from copy import deepcopy

def add_unique(list, str_to_add):
    if str_to_add not in list:
        list.append(str_to_add)
        return True
    return False

traiectorii = {('0', 'a'): ['0', '1'], ('0', 'b'): '0', ('1', 'a'): 'none', ('1', 'b'): '2', ('2', 'a'): '2', ('2', 'b'): '2'}
letters = ['a', 'b']
nodes = ['0']
#nodes_frequency = []*100
nodes_frequency_index = 0
state = 0


aux_list = []
n = 0 # nodul initial
while n < len(nodes):
    if len(nodes[n]) <= 1:
        for ch in letters:
            print 's', 0,
            if n==0:
                print  '->',ch, traiectorii[(nodes[n], ch)]
            if traiectorii[(nodes[n], ch)] == 'none':
                continue
            #print ch,'->', 's', traiectorii[(nodes[n], ch)]
            if(add_unique(nodes, traiectorii[(nodes[n], ch)])):
                nodes_frequency_index += 1
            #print nodes
    else:
        for ch in letters:
            print 's', nodes[n],
            aux_list2 = []
            #print ch, '-> ',nodes[n]
            for k in range(len(nodes[n])):
                '''
                if n==0:
                    print ch, '->', traiectorii[(nodes[n][k], ch)]
                '''
                if traiectorii[(nodes[n][k], ch)] == 'none':
                    continue

                #print ch,'->', 's', traiectorii[(nodes[n][k], ch)]
                #print "*", n[int(traiectorii[(nodes[n][k], ch)])]
                for el in range(len(traiectorii[(nodes[n][k],ch)])):
                    add_unique(aux_list2, traiectorii[(nodes[n][k],ch)][el])
                #print "*", aux_list
            add_unique(nodes, aux_list2)
            print "->",ch, aux_list2


    n = n + 1




print "verificare"
traiectorii2 = {('0', 'a'): '1', ('0', 'b'): '0', ('1', 'a'): '1', ('1', 'b'): '2', ('2', 'a'): '3', ('2', 'b'): '2', ('3', 'a'): 3, ('3', 'b'):2}
print traiectorii2[('0', 'a')]


n = 0
while n < len(nodes):
    for ch in letters:
        print 's',n, '->', ch, 's', nodes[int(traiectorii2[(str(n), ch)])]
    n = n+1
