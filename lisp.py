def read():
    return raw_input('=> ')

def tokens(l):
    if is_atom(l):
        return l
    if is_list(l):
        return make_list(l)

def free_of(s, c):
    return s.find(c) == -1

def is_atom(l):
    return free_of(l, ' ')

def is_list(l):
    return l[0] == '(' and\
           l[-1] == ')' and\
           free_of(l[1:-1], '(') and\
           free_of(l[1:-1], ')')

def make_list(l):
    return tuple(l[1:-1].split())
def leval(l):
    return tokens(l)

def lprint(l):
    print(l)

def loop(f):
    f()
    return loop(f)

def main():
    loop(lambda:lprint(leval(read())))

if __name__ == '__main__':
    main()


