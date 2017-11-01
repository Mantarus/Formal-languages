from auto.FNDA import FNDA
from auto.util import parse_args


def main():
    transition_table = open('automats/5-LS.txt', 'r')
    params = parse_args(transition_table)
    transition_table.close()

    V = params[0]
    Q = params[1]
    q0 = params[2]
    F = params[3]
    func = params[4]

    string = input("Input string: ")

    i = 0
    while i < len(string):
        a = FNDA(V, Q, q0, F, func)
        result = a.run(string[i:])
        if result[0]:
            print("Found: '{}'".format(string[i : i + result[1]]))
        else:
            i += 1
        i += result[1]


if __name__ == '__main__':
    main()
