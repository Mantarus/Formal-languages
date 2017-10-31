def parse_args(file):
    file.readline()
    V = file.readline().strip().split(' ')
    file.readline()
    Q = file.readline().strip().split(' ')
    file.readline()
    q0 = file.readline().strip().split(' ')
    file.readline()
    F = file.readline().strip().split(' ')
    file.readline()
    transitions = dict()
    string = file.readline().strip()
    while len(string):
        tokens = string.split(' ')
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
