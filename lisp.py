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
        return lookup(exp, env)
    elif is_define(exp):
        return define(exp, env)
    elif is_cond(exp):
        return condeval(tail(exp), env)
    elif is_lambda(exp):
        return closure(exp, env)
    elif is_macro(exp):
        return closure(exp, env)
    elif head(exp) == 'eval':
        return leval(leval(head(tail(exp)), env), env)
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
    e = {'$parent': fe,
         '$name': 'new_env'}
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
        p = predicate(exp)
        c = consequence(exp)
        if not is_false(leval(p, env)):
            return leval(c, env)
        else:
            return condeval(tail(exp), env)

def apply_macro(m, p, env):
    macro_e = function_env(m)
    replace_e = {'$parent': macro_e,
                 '$name': 'macro_env'}
    assoc(formal_params(m), p, replace_e)
    fbody = function_body(m)
    return leval(lparse(fbody, replace_e), env)

def lparse(exp, env):
    if type(exp) is not str and type(exp) is not tuple:
        return exp
    if is_symbol(exp):
        if env.get(exp) is not None:
            return env[exp]
        else:
            return exp
    elif len(exp) > 0 and head(exp) == '$eval':
        print(exp)
        print(env['exp'])
        return leval(leval(head(tail(exp)), env), env)
    else:
        return tuple(map(lambda x: lparse(x, env), exp))

def apply_primitive(f, p, e):
    leval_e = partial(leval, env=e)
    args = linearize_pair(pair_map(leval_e, p))
    return f[1](*args)

def define(exp, env):
    env[head(tail(exp))] = leval(head(tail(tail(exp))), env)
    return env[head(tail(exp))]

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
