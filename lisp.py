from parse import read
from funeval import *
from lglobals import lglobals, apply_primitive
from functools import partial
def leval(exp, env):
    if is_false(exp):
        return 'False'
    elif is_number(exp):
        return exp
    elif is_quote(exp):
        return unquote(exp)
    elif is_symbol(exp):
        return env[exp]
    elif is_define(exp):
        return define(exp, env)
    elif is_cond(exp):
        return condeval(exp, env)
    elif is_lambda(exp):
        return closure(exp, env)
    elif is_primitive(exp):
        return exp
    else:
        return lapply(leval(head(exp), env),\
         tail(exp), env)

def lapply(fun, params, env):
    if is_primitive(fun):
        leval_e = partial(leval, env=env)
        args = map(leval_e, params)
        return apply_primitive(fun[1],
            args)
    env.update(fun[1])
    e = env.copy()
    formals = fun[0][1]
    z = zip(formals, params)
    for p in z:
        e[p[0]] = leval(p[1], env)
    return leval(fun[0][2], e)

def condeval(exp, env):
    clauses = tail(exp)
    for c in clauses:
        condition = head(c)
        consequence = c[1]
        if not is_false(leval(condition, env)):
            return leval(consequence, env)
    return tuple()

def define(exp, env):
    env[exp[1]] = leval(exp[2], env)
    return exp[1]

def lprint(l):
    print(l)

def loop(f):
    while True:
        f()

def main():
    loop(lambda:lprint(leval(read(), lglobals)))

if __name__ == '__main__':
    main()


