from operator import *

def apply_primitive(f, x, y):
	return f(x, y)

def eqx(p, q):
	if p != q:
		return tuple()
	else:
		return True

lglobals = {'+': add,
            '-': sub,
            '=': eqx,
            '>=': ge,
            '<=': le,
            '*': mul
}

l = lglobals.keys()
for k in l:
	lglobals[k] = ('$', lglobals[k])
