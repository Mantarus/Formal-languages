from auto.util import build_fnda
from auto.util import replace_delimeters


def main():
    automates = [
        build_fnda('automates/2-IN.txt', 'IN'),
        build_fnda('automates/3-RN.txt', 'RN'),
        build_fnda('automates/4-LOG.txt', 'LOG'),
        build_fnda('automates/5-LS.txt', 'LS'),
        build_fnda('automates/6-RS.txt', 'RS'),
        build_fnda('automates/7-NIL.txt', 'NIL'),
        build_fnda('automates/8-LB.txt', 'LB'),
        build_fnda('automates/9-RB.txt', 'RB'),
        build_fnda('automates/10-COL.txt', 'COL'),
        build_fnda('automates/11-COM.txt', 'COM'),
        build_fnda('automates/12-OP.txt', 'OP'),
        build_fnda('automates/13-LC.txt', 'LC'),
        build_fnda('automates/14-RC.txt', 'RC'),
        build_fnda('automates/15-KW.txt', 'KW'),
        build_fnda('automates/16-AS.txt', 'AS'),
        build_fnda('automates/17-WS.txt', 'WS'),
        build_fnda('automates/1-ID.txt', 'ID')
    ]

    in_string = ''
    out_string = ''

    with open('input.txt', 'r') as file:
        in_string = file.read()

    i = 0
    while i < len(in_string):
        result = (False, 0)
        tag = ''
        for auto in automates:
            res = auto.run(in_string[i:])
            if res[0]:
                if not result[0] or res[1] > result[1]:
                    result = res
                    tag = auto.tag

        if result[0]:
            out_string += ("{}: '{}'".format(tag, replace_delimeters(in_string[i : i + result[1]]))) + '\n'
        else:
            i += 1
        i += result[1]

    with open('output.txt', 'w') as file:
        file.write(out_string)


if __name__ == '__main__':
    main()
