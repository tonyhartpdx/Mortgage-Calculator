#!/usr/bin/python

def rpn(s):
	stack = []
	for i in s.split():
		if not i in "+-*":
			stack.append(int(i))
		else:
			var1, var2 = stack.pop(), stack.pop()
			stack.append(eval(str(var2) + i + str(var1)))
	return stack[0]

print rpn('3 4 * 6 2 - +')
print rpn('12 5 * 4 8 + -')
