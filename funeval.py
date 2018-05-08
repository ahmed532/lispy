def pair(x, y):
        return (x, y)

def head(l):
	return l[0]

def tail(l):
	return l[1]

def is_number(exp):
	return type(exp) is int or\
	       type(exp) is float

def is_quote(exp):
	return head(exp) == 'quote'

def is_symbol(exp):
	return type(exp) is str

def is_cond(exp):
	return head(exp) == 'cond'

def is_lambda(exp):
	return head(exp) == 'lambda'

def unquote(exp):
	return head(tail(exp))

def is_false(exp):
	return exp == tuple()

def closure(exp, env):
	return pair(exp, env.copy())

def is_define(exp):
	return head(exp) == 'define'

def is_primitive(exp):
	return head(exp) == '$'

def is_macro(exp):
	return head(exp) == 'macro'

def is_empty(exp):
	if type(exp) is str:
		return len(exp) == 0
	else:
		return False

def function_env(f):
	return tail(f)

def formal_params(f):
	return head(tail(head(f)))

def function_body(f):
	return head(tail(tail(head(f))))

def is_closure_macro(f):
	return head(head(f)) == 'macro'

def flatten(l):
	if type(l) is tuple:
		if l == tuple():
			return tuple()
		else:
			return sum(map(flatten, l), tuple())
	else:
		return (l, )

def pair_map(f, l):
	if l == tuple():
		return tuple()
	else:
		return pair(f(head(l)), pair_map(f, tail(l)))

def assoc(formals, params, e):
	if formals == tuple():
		return tuple()
	else:
		e[head(formals)] = head(params)
		return assoc(tail(formals), tail(params), e)

