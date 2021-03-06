from parse import strip, tokens, parse,\
 balanced_parans, ignore_comments, pair_list

def fread(f):
	lines = f.readlines()
	lines = list(filter(lambda l: len(ignore_comments(l.strip())) != 0, lines))
	exp, i, eof = read_exp(lines, 0)
	yield pair_list(parse(tokens(strip(exp))))
	while not eof:
		exp, i, eof = read_exp(lines, i)
		yield pair_list(parse(tokens(strip(exp))))

def read_exp(lines, i):
	s = ignore_comments(strip(lines[i]))
	i = i + 1
	while not balanced_parans(s) and i < len(lines):
		s = s + ' ' + ignore_comments(strip(lines[i]))
		i = i + 1
	return s, i, i == len(lines)
