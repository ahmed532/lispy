from parse import read
from funeval import *
from lglobals import lglobals
from functools import partial
from files import fread
import os

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
    elif is_macro(exp):
        return closure(exp, env)
    elif is_primitive(exp):
        return exp
    else:
        return lapply(leval(head(exp), env),\
         tail(exp), env)

def lapply(fun, params, env):
    if is_primitive(fun):
        return apply_primitive(fun,
            params, env)
    fun_env = fun[1]
    env.update(fun_env)
    e = env.copy()
    formals = fun[0][1]
    z = zip(formals, params)
    for symbol, exp in z:
        e[symbol] = leval(exp, env)
    fun_body = fun[0][2]
    return leval(fun_body, e)

def condeval(exp, env):
    clauses = tail(exp)
    for c in clauses:
        condition = head(c)
        consequence = c[1]
        if not is_false(leval(condition, env)):
            return leval(consequence, env)
    return tuple()

def macroeval(exp, env):
    return exp

def apply_primitive(f, p, e):
    leval_e = partial(leval, env=e)
    args = map(leval_e, p)
    return f[1](*args)

def define(exp, env):
    env[exp[1]] = leval(exp[2], env)
    return exp[1]

def lprint(l):
    if is_empty(l):
        print(l, end='')
    else:
        print(l)

def loop(f):
    while True:
        f()

def leval_file(path):
    f = open(path)
    for exp in fread(f):
        lprint(leval(exp, lglobals))

def main():
    leval_file('sample.s') 
    loop(lambda:lprint(leval(read(), lglobals)))

if __name__ == '__main__':
    main()


