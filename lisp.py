from parse import read
from funeval import *
from lglobals import lglobals

def leval(exp, env):
    if is_false(exp):
        return tuple()
    elif is_number(exp):
        return exp
    elif is_quote(exp):
        return unquote(exp)
    elif is_symbol(exp):
        return env[exp]
    elif is_cond(exp):
        return condeval(exp, env)
    elif is_lambda(exp):
        return closure(exp, env)
    else:
        return lapply(leval(head(exp), env),\
         tail(exp))

def lapply(fun, params):
    print(fun, params)


def condeval(exp, env):
    clauses = tail(exp)
    for c in clauses:
        condition = head(c)
        consequence = c[1]
        if not is_false(leval(condition, env)):
            return leval(consequence, env)
    return tuple()

def lprint(l):
    print(l)

def loop(f):
    while True:
        f()

def main():
    loop(lambda:lprint(leval(read(), lglobals)))

if __name__ == '__main__':
    main()


