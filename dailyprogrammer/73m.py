#!/usr/bin/python

# Write a program that, given an ASCII binary matrix of 0's and 1's like this:
# 0000000000000000
# 0000000000000000
# 0000011001110000
# 0000001111010000
# 0000011001110000
# 0000011011100000
# 0000000000110000
# 0000101000010000
# 0000000000000000
# 0000000000000000
# 0000000000000000

# Outputs the smallest cropped sub-matrix that still contains all 1's (that is, remove all borders of 0's):
# 01100111
# 00111101
# 01100111
# 01101110
# 00000011
# 10100001

matrix = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,1,1,0,0,1,1,1,0,0,0,0],
[0,0,0,0,0,0,1,1,1,1,0,1,0,0,0,0],
[0,0,0,0,0,1,1,0,0,1,1,1,0,0,0,0],
[0,0,0,0,0,1,1,0,1,1,1,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0],
[0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

start = len(matrix[0])
end = len(matrix[0])
length = len(matrix[0])

for row in matrix:
	if 1 in row:
		if row.index(1) < start:
			start = row.index(1)

		row.reverse()
		if row.index(1) < end:
			end = row.index(1)
		row.reverse()

end = length - 1 - end
i = 0
output = []
str_out = ''

for row in matrix:
	if 1 in row:
		output.append(row[start:end+1])
	i += 1

for row in output:
	for digit in row:
		str_out = str_out + str(digit)
	str_out = str_out + '\n'

print str_out
