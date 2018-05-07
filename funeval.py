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

def is_macro(exp):
	return head(exp) == 'macro'

def is_empty(exp):
	if type(exp) is str:
	   return len(exp) == 0
	else:
		return False

def function_env(f):
	return f[1]

def formal_params(f):
	return f[0][1]

def function_body(f):
	return fun[0][2]
