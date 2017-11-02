from auto.util import build_fnda


def main():
    automates = []
    automates.append(build_fnda('automates/2-IN.txt', 'IN'))
    automates.append(build_fnda('automates/3-RN.txt', 'RN'))
    automates.append(build_fnda('automates/4-LOG.txt', 'LOG'))
    automates.append(build_fnda('automates/5-LS.txt', 'LS'))
    automates.append(build_fnda('automates/6-RS.txt', 'RS'))
    automates.append(build_fnda('automates/7-NIL.txt', 'NIL'))
    automates.append(build_fnda('automates/8-LB.txt', 'LB'))
    automates.append(build_fnda('automates/9-RB.txt', 'RB'))
    automates.append(build_fnda('automates/10-COL.txt', 'COL'))
    automates.append(build_fnda('automates/11-COM.txt', 'COM'))
    automates.append(build_fnda('automates/12-OP.txt', 'OP'))
    automates.append(build_fnda('automates/13-LC.txt', 'LC'))
    automates.append(build_fnda('automates/14-RC.txt', 'RC'))
    automates.append(build_fnda('automates/15-KW.txt', 'KW'))
    automates.append(build_fnda('automates/16-AS.txt', 'AS'))
    automates.append(build_fnda('automates/17-WS.txt', 'WS'))
    automates.append(build_fnda('automates/1-ID.txt', 'ID'))

    string = input("Input string: ")

    i = 0
    while i < len(string):
        result = (False, 0)
        tag = ''
        for auto in automates:
            res = auto.run(string[i:])
            if res[0]:
                if not result[0] or res[1] > result[1]:
                    result = res
                    tag = auto.tag

        if result[0]:
            print("{}: '{}'".format(tag, string[i : i + result[1]]))
        else:
            i += 1
        i += result[1]


if __name__ == '__main__':
    main()
