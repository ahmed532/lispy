from funeval import pair, head, tail
 
def read():
    try:
        s = ignore_comments(strip(input('=> ')))
        while not balanced_parans(s):
            s = s + ' ' + ignore_comments(strip(input('.... ')))
    except:
        print('bye!')
        quit()
    if is_empty(s):
        return read()
    return pair_list(parse(tokens(strip(s))))

def parse(exp):
    if is_number(exp):
        return make_number(exp)
    elif is_symbol(exp):
        return exp
    else:
        return tuple(map(lambda x: pair_list(parse(x)), exp))

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

def is_empty(exp):
    return len(exp) == 0

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

def strip(s):
    s = s.strip()
    i = 0
    ns = ''
    while i < len(s):
        if s[i].isspace():
            ns = ns + ' '
            while s[i].isspace():
                i = i + 1
        else:
            ns = ns + s[i]
            i = i + 1
    return ns

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


def balanced_parans(s):
    return s.count('(') == s.count(')')

def ignore_comments(s):
    if s.find('//') != -1:
        return s[:s.find('//')]
    else:
        return s

def pair_list(l):
    if type(l) is tuple:
        if len(l) == 0:
            return tuple()
        else:
            return pair(head(l), pair_list(l[1:]))
    else:
        return l

