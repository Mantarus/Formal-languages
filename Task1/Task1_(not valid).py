ADV = "ADV"
WIN = "WIN"
LOSE = "LOSE"
FALSE = "FALSE"
A_WON = "A WON"
B_WON = "B WON"


def main():
    string = input("Type input string: ")
    result = run_det(string)
    if result:
        print("Det: Allowed")
    else:
        print("Det: Not allowed")

    result = run_not_det(string)
    if result:
        print("Not det: Allowed")
    else:
        print("Not det: Not allowed")


def run_det(string):
    F = {A_WON, B_WON}
    q = (0, 0)

    for char in string:
        q = get_next_state_det(q, char)
        print(char, q)
        if q == FALSE:
            return False

    if q in F:
        return True
    return False


# def run_not_det(input, init_states):
#     results = [run_det(input, x) for x in init_states]
#     for result in results:
#         if result:
#             return True
#     return False


def run_not_det(string):
    F = {A_WON, B_WON}
    q = {(0, 0)}
    print(q)
    X = {'a', 'b'}
    for char in string:
        q_next = set()
        for state in q:
            if state == FALSE:
                continue
            for x in X:
                q_next.add(get_next_state_det(state, x))

        if q_next == {FALSE}:
            return False

        q = q_next
        print(q)

    for fin in F:
        if fin in q:
            return True

    return False



def get_next_state_det(q, x):
    if q == A_WON or q == B_WON:
        return FALSE
    if x == 'a':
        count = calc_count_det(q[0], q[1])
        if count[0] == WIN:
            return A_WON
        next_q = count
    elif x == 'b':
        count = calc_count_det(q[1], q[0])
        if count[0] == WIN:
            return B_WON
        next_q = (count[1], count[0])
    else:
        return FALSE
    return next_q


def calc_count_det(w_points, l_points):
    if w_points == 40 and l_points == 40:
        return (ADV, 40)
    if w_points == 40 and l_points == ADV:
        return (40, 40)
    if w_points == ADV or w_points == 40 and l_points < 40:
        return (WIN, LOSE)
    if w_points == 30:
        return (40, l_points)
    return (w_points + 15, l_points)


main()