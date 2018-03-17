#!/usr/bin/python

# Write a program that takes a title and a list as input and outputs the list in a nice column. Try to make it so the title is centered. For example:
# title: 'Necessities'
# input: ['fairy', 'cakes', 'happy', 'fish', 'disgustipated', 'melon-balls']

# output:

#     +---------------+
#     |  Necessities  |
#     +---------------+
#     | fairy         |
#     | cakes         |
#     | happy         |
#     | fish          |
#     | disgustipated |
#     | melon-balls   |
#     +---------------+
# Bonus: amend the program so that it can output a two-dimensional table instead of a list. For example, a list of websites:
# titles: ['Name', 'Address', 'Description']
# input:  [['Reddit', 'www.reddit.com', 'the frontpage of the internet'],
#         ['Wikipedia', 'en.wikipedia.net', 'The Free Encyclopedia'],
#         ['xkcd', 'xkcd.com', 'Sudo make me a sandwich.']]

# output:

#     +-----------+------------------+-------------------------------+
#     |   Name    |     Address      |          Description          |
#     +-----------+------------------+-------------------------------+
#     | Reddit    | www.reddit.com   | the frontpage of the internet |
#     +-----------+------------------+-------------------------------+
#     | Wikipedia | en.wikipedia.net | The Free Encyclopedia         |
#     +-----------+------------------+-------------------------------+
#     | xkcd      | xkcd.com         | Sudo make me a sandwich       |
#     +-----------+------------------+-------------------------------+

title = 'Long Necessities'
list = ['fairy', 'cakes', 'happy', 'fish', 'disgustipated', 'melon-balls']

def print_seperator_line(output,length):
	output = output + '+-' + ('-' * length) + '-+\n'
	return output

def find_max_length(list,title):
	return max([max(len(x) for x in list),len(title)])

def print_list(title,list):
	output = ''
	max_length = find_max_length(list,title)
	padding = max_length - len(title)

	output = print_seperator_line(output,max_length)
	output = output + '| ' + (' ' * (padding / 2)) + title + (' ' * (padding - (padding /2))) + ' |\n'
	output = print_seperator_line(output,max_length)

	for i in list:
		padding = max_length - len(i)
		output = output + '| ' + i + (' ' * padding) + ' |\n'

	output = print_seperator_line(output,max_length)

	return output


def print_list2(title,list):
	output = ''

	if type(title).__name__ == 'str':
		max_length = find_max_length(list,title)
		padding = max_length - len(title)
		output = print_seperator_line(output,max_length)
		output = output + '| ' + (' ' * (padding / 2)) + title + (' ' * (padding - (padding /2))) + ' |\n'
		output = print_seperator_line(output,max_length)

		for i in list:
			padding = max_length - len(i)
			output = output + '| ' + i + (' ' * padding) + ' |\n'

		output = print_seperator_line(output,max_length)

	elif type(title).__name__ == 'list':
		max_length = []
		title_padding = []
		padding = []

		for i in range(0,len(title)):
			items = []
			for j in range(0,len(list)):
				items.append(list[j][i])
			max_length.append(find_max_length(items,title[i]))

		for i in range(0,len(title)):
			title_padding.append(max_length[i] - len(title[i]))
		
	output = print_seperator_line(output,max_length)
	output = output + '| ' + (' ' * (padding / 2)) + title + (' ' * (padding - (padding /2))) + ' |\n'
	output = print_seperator_line(output,max_length)

	for i in list:
		padding = max_length - len(i)
		output = output + '| ' + i + (' ' * padding) + ' |\n'

	output = print_seperator_line(output,max_length)

	return output

print print_list(title,list)
