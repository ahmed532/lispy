from operator import *

def eqx(p, q):
	if p != q:
		return tuple()
	else:
		return True

def gex(p, q):
	if p < q:
		return tuple()
	else:
		return True

def lex(p, q):
	if p > q:
		return tuple()
	else:
		return True

def ltx(p, q):
	if p >= q:
		return tuple()
	else:
		return True

def gtx(p, q):
	if p <= q:
		return tuple()
	else:
		return True

def notx(p):
	if p == tuple():
		return True
	else:
		return tuple()

def andx(p, q):
	if p == tuple() or q == tuple():
		return tuple()
	else:
		return True

def orx(p, q):
	if p == tuple() and q == tuple():
		return tuple()
	else:
		return True

lglobals = {'+': add,
            '-': sub,
            '*': mul,
            '/': truediv,
            'mod': mod,
            '=': eqx,
            '>=': gex,
            '<=': lex,
            '<': ltx,
            '>': gtx,
            'not': notx,
            'and': andx,
            'or': orx,
            'concat': concat,
}

l = lglobals.keys()
for k in l:
	lglobals[k] = ('$', lglobals[k])

lglobals['False'] = tuple()
lglobals['else'] = True
lglobals['True'] = True
