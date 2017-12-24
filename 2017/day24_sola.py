# from u794575248

from collections import defaultdict

def gen_bridges(library, bridge=None):
	l, s, components, a = bridge or (0, 0, set(), 0)
	for b in library[a]:
		next = (a, b) if a <= b else (b, a)
		if next not in components:
			new = l+1, s+a+b, (components | {next}), b
			yield new; yield from gen_bridges(library, new)

def solve(input):
	library = defaultdict(set)
	for l in input.strip().splitlines():
		a, b = [int(x) for x in l.split('/')]
		library[a].add(b); library[b].add(a)
	return [b[:2] for b in gen_bridges(library)]


file = open('day24_input.txt', 'r')
input = file.read()

bridges = solve(input)  # A list of (length, strength) tuples
part1 = sorted(bridges, key=lambda x: x[1])[-1][1]  # Sort by strength only
part2 = sorted(bridges)[-1][1]  # Sort by length, then by strength

print('part 1: strength of strongest bridge is {}'.format(part1))
print('part 1: strength of longest bridge is {}'.format(part2))


