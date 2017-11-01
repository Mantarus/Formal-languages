from auto.util import build_fnda


def main():
    a = build_fnda('automats/15-KW.txt')

    string = input("Input string: ")

    i = 0
    while i < len(string):
        result = a.run(string[i:])
        if result[0]:
            print("Found: '{}'".format(string[i : i + result[1]]))
        else:
            i += 1
        i += result[1]


if __name__ == '__main__':
    main()
