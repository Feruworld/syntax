import numpy as np

n = 7

class nonterminal_rule:
    def __init__(self, parent, child1, child2):
        self.parent = parent
        self.child = [child1, child2]
        self.term = False


class terminal_rule(nonterminal_rule):
    def __init__(self, parent, terminal):
        self.parent = parent       
        self.child = terminal
        self.term = True

def search_terminal(word):
    rulenum = []
    for i,rule in enumerate(term_rules):
        if rule.child == word: rulenum.append(i)
    return rulenum

def search_nonterminal(lc, bc):
    rulenum = []
    for i,rule in enumerate(nonterm_rules):
        print rule.child[0], table[lc[0]][lc[1]]
        if rule.child[0] in table[lc[0]][lc[1]] and rule.child[1] in table[bc[0]][bc[1]]:
            rulenum.append(i)
    return rulenum

for d in range(n-1):
    for i in range(n-d):
        j = i + d
        for k in range(i,j):
            print i,j, "from", i,k, ",", k+1,j

term_rules = []
nonterm_rules = []
nonterm_rules.append(nonterminal_rule('S', 'NP', 'VP'))
term_rules.append(terminal_rule('NP', 'I'))
term_rules.append(terminal_rule('VP', 'see'))

string = 'I see'
words = string.split()
words_num = len(words)

table = [[[] for j in range(words_num)] for i in range(words_num)]

for i, word in enumerate(words): #search for nonterminal rule corresponding to (i,i) in the table
    #Is there any rules that generate word? (the i-th word in sentence)
    match = search_terminal(word)
    for m in match:
        table[i][i].append(term_rules[m].parent)

for d in range(words_num):
    for i in range(words_num - d):
        j = i + d
        for k in range(i,j):
            match =  search_nonterminal([i,k], [k+1,j])
            for m in match:
                table[i][j].append(nonterm_rules[m].parent)
            #must give the cell (i,k) and (k+1,j) in the table.

print words
print table
