def read():
    try:
        s = raw_input('=> ')
    except:
        print('bye!')
        quit()
    return parse(tokens(s))

def parse(exp):
    if is_number(exp):
        return make_number(exp)
    elif is_symbol(exp):
        return exp
    else:
        return tuple(map(parse, exp))

def is_symbol(exp):
    return type(exp) is str

def is_number(exp):
    try:
        int(exp)
        return True
    except:
        try:
            float(exp)
            return True
        except:
            return False

def make_number(exp):
    try:
        return int(exp)
    except:
        return float(exp)

def tokens(l):
    if is_atom(l):
        return l
    if is_list(l):
        return make_list(l)
    else:
        return recur_list(l)

def recur_list(l):
    a = l[1:-1].split()
    t = []
    i = 0
    while i < len(a):
        x = a[i]
        if is_atom(x):
            t.append(x)
            i = i + 1
        else:
            p = 1
            j = 1
            s = ''
            while p > 0:
                if x[j] == '(':
                    p = p + 1
                elif x[j] == ')':
                    p = p - 1
                j = j + 1
                if j == len(x):
                    s = s + ' ' + x
                    i = i + 1
                    if i == len(a):
                        break
                    x = a[i]
                    j = 0
            t.append(s.strip())
    return tuple(map(tokens, t))

def free_of(s, c):
    return s.find(c) == -1

def is_atom(l):
    return free_of(l, ' ') and\
           free_of(l, '(') and\
           free_of(l, ')')

def is_list(l):
    return l[0] == '(' and\
           l[-1] == ')' and\
           free_of(l[1:-1], '(') and\
           free_of(l[1:-1], ')')

def make_list(l):
    return tuple(l[1:-1].split())
