from parse import strip, tokens, parse, balanced_parans

def fread(f):
	lines = f.readlines()
	lines = list(filter(lambda l: len(l.strip()) != 0, lines))
	exp, i, eof = read_exp(lines, 0)
	yield parse(tokens(strip(exp)))
	while not eof:
		exp, i, eof = read_exp(lines, i)
		yield parse(tokens(strip(exp)))



def read_exp(lines, i):
	s = lines[i]
	i = i + 1
	while not balanced_parans(s) and i < len(lines):
		s = s + ' ' + lines[i]
		i = i + 1
	return s, i, i == len(lines)

