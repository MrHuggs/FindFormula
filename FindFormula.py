
# Program to solve 24 style problems.
#
# For example make 24 out 1 1 8 3 using only multiplication, division, addition, subtraction.
#                  24 = 1 * 1 * 8 * 3
#
import sys

# Special entry for the starting values.
nul = ([], [], 'N')


# Given a list of possible numbers, find numbers that can be made using binary operations.
#
# Each entry of the list should be of the form (<value>, (<list entry>, <list entry>, operation))
#
def possibles(current_list):

    n = len(current_list)

    results = []
    for i in range(0, n):
        xn = current_list[i]
        x = xn[0]
        for j in range(i + 1, n):
            yn = current_list[j]
            y = yn[0]

            l = current_list.copy()
            del l[j]
            del l[i]

            c = [((x * y, (xn, yn, '*')))]
            c.extend(l)
            results.append(c)

            c = [((x - y, (xn, yn, '-')))]
            c.extend(l)
            results.append(c)

            c = [((y - x, (yn, xn, '-')))]
            c.extend(l)
            results.append(c)

            c = [((x + y, (xn, yn, '+')))]
            c.extend(l)
            results.append(c)

            if not y == 0:
                c = [((x / y, (xn, yn, '/')))]
                c.extend(l)
                results.append(c)

            if not x == 0:
                c = [((y / x, (yn, xn, '/')))]
                c.extend(l)
                results.append(c)

    return results


# Given a list numbers, extend to make a new list by applying binary
# operations.
def extend(ll):
    r = []
    for l in ll:
        t = possibles(l)
        r.extend(t)

    return r


# Take a list and produce a lits of numbers that can be made with binary operations.
def process(sl):

    l = sl
    while len(l[0]) > 1:
        l = extend(l)

    return l

# Given a list of operations, produce a string representing the result:
def make_string(list):
    prev = list[1]
    if prev[2] == 'N':
        return str(list[0])

    a = make_string(prev[0])
    b = make_string(prev[1])

    return "({0}{1}{2})".format(a, prev[2],b)

if __name__ == '__main__':

    if len(sys.argv) < 3:
        print("Usage: <target value> [values]")
        quit(0)

    target = int(sys.argv[1])

    start_list = []

    for i in range(2, len(sys.argv)):
        start_list.append( (int(sys.argv[i]), nul) )

    start_list = [start_list]

    a = process(start_list)


    seen = set()
    for l in a:
        for t in l:
            if t[0] == target:
                s = make_string(t)

                if s in seen:
                    continue

                seen.add(s)
                print(target, " = ", s)


