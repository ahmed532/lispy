from parse import read, parse
from funeval import *
from lglobals import lglobals
from functools import partial
from files import fread
import sys

def leval(exp, env):
    if is_false(exp):
        return tuple()
    elif is_number(exp):
        return exp
    elif is_quote(exp):
        return unquote(exp)
    elif is_symbol(exp):
        return env[exp]
    elif is_define(exp):
        return define(exp, env)
    elif is_cond(exp):
        return condeval(tail(exp), env)
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
    if is_closure_macro(fun):
        return apply_macro(fun,
            params, env)
    fe = function_env(fun)
    env.update(fe)
    e = env.copy()
    formals = formal_params(fun)
    bind(formal_params(fun), params, e, env)
    fbody = function_body(fun)
    return leval(fbody, e)

def bind(formals, params, e, env):
    if formals == tuple():
        return tuple()
    else:
        e[head(formals)] = leval(head(params), env)
        return bind(tail(formals), tail(params), e, env)

def condeval(exp, env):
    if exp == tuple():
        return tuple()
    else:
        predicate = head(head(exp))
        consequence = head(tail(head(exp))) 
        if not is_false(leval(predicate, env)):
            return leval(consequence, env)
        else:
            return condeval(tail(exp), env)

def apply_macro(m, p, env):
    macro_e = function_env(m)
    env.update(macro_e)
    e = env.copy()
    formals = formal_params(m)
    z = zip(formals, p)
    replace_e = {}
    for symbol, exp in z:
        replace_e[symbol] = exp
    fbody = function_body(m)
    return leval(parse(fbody, replace_e), e)

def apply_primitive(f, p, e):
    leval_e = partial(leval, env=e)
    args = tuple(pair_map(leval_e, p))
    return f[1](*flatten(args))

def define(exp, env):
    env[head(tail(exp))] = leval(head(tail(tail(exp))), env)
    return head(tail(exp))

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
    if len(sys.argv) == 2:
        leval_file(sys.argv[1]) 
    loop(lambda:lprint(leval(read(), lglobals)))

if __name__ == '__main__':
    main()


