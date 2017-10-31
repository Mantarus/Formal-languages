from auto.FNDA import FNDA
from auto.util import parse_args


def main():
    transition_table = open('Task1/notdet.txt', 'r')
    params = parse_args(transition_table)
    transition_table.close()

    V = params[0]
    Q = params[1]
    q0 = params[2]
    F = params[3]
    func = params[4]

    a = FNDA(V, Q, q0, F, func)
    result = a.run(input("Input string: "))
    if result:
        print("Allowed")
    else:
        print("Not allowed")


if __name__ == '__main__':
    main()
