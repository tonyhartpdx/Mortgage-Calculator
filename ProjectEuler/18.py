import sys
rows = []
total = 0
with open("18tri.txt", "r") as f:
  for cur_line in f:
	  cur_list = cur_line.split()
	  for i in cur_list:
	  	rows.append(int(i))

print rows
