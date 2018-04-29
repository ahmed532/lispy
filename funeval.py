def head(l):
	return l[0]

def tail(l):
	return l[1:]

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
	return exp[1]

def is_false(exp):
	return exp == tuple()

def closure(exp, env):
	return (exp, env.copy())

def is_define(exp):
	return head(exp) == 'define'

def is_primitive(exp):
	return head(exp) == '$'
