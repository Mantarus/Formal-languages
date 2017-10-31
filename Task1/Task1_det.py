class FDA:
    ERROR = 'ERROR'

    def __init__(self, V, Q, q0, F, func):
        self.V = V
        self.Q = Q
        self.q0 = q0
        self.F = F
        self.func = func

    def run(self, string):
        q = self.q0
        for x in string:
            q = self._transit(q, x)
            print(x, q)
            if q == self.ERROR:
                return False

        if q in self.F:
            return True
        return False

    def _transit(self, q, x):
        if self.func.get(q).get(x):
            return self.func.get(q).get(x)
        return self.ERROR


def main():
    params = parse('Task1/task1det.txt')
    V = params[0]
    Q = params[1]
    q0 = params[2]
    F = params[3]
    func = params[4]

    a = FDA(V, Q, q0, F, func)
    result = a.run(input("Input string: "))
    if result:
        print("Allowed")
    else:
        print("Not allowed")


def parse(filename):
    file = open(filename, 'r')
    file.readline()
    V = file.readline().strip().split(' ')
    file.readline()
    Q = file.readline().strip().split(' ')
    file.readline()
    q0 = file.readline().strip()
    file.readline()
    F = file.readline().strip().split(' ')
    file.readline()
    transitions = dict()
    str = file.readline().strip()
    while len(str):
        tokens = str.split(' ')
        q = tokens[0]
        x = tokens[1]
        t = tokens[2]
        if not transitions.get(q):
            transitions[q] = dict()
        transitions[q][x] = t
        str = file.readline().strip()
    file.close()

    return (V, Q, q0, F, transitions)

if __name__ == '__main__':
    main()
