def parse_args(file):
    file.readline()
    V = get_tokens(file.readline())
    file.readline()
    Q = get_tokens(file.readline())
    file.readline()
    q0 = get_tokens(file.readline())
    file.readline()
    F = get_tokens(file.readline())
    file.readline()
    transitions = dict()
    string = file.readline().strip()
    while len(string):
        tokens = replace_special(string.split(' '))
        q = tokens[0]
        x = tokens[1]
        t = tokens[2]
        if not transitions.get(q):
            transitions[q] = dict()
        if not transitions.get(q).get(x):
            transitions[q][x] = []
        transitions[q][x].append(t)
        string = file.readline().strip()

    return (V, Q, q0, F, transitions)


def get_tokens(line):
    return replace_special(line.strip().split(' '))


def replace_special(tokens):
    result = []
    for token in tokens:
        if token == 'whitespace':
            result.append(' ')
        else:
            result.append(token)
    return result
