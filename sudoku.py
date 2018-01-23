
import random

# game_field = [
# [1, 2, 3, 2, 0, 0, 5, 0, 0],
# [4, 5, 6, 0, 0, 0, 0, 0, 0],
# [7, 8, 9, 0, 0, 0, 0, 0, 0],
# [4, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 3, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0],
# [2, 0, 0, 0, 0, 0, 0, 5, 0]]

game_field = [
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0]]


def print_game_field():
	print('\n===========================\n')

	for i in game_field:
		print(i)

	print('\n===========================\n')

def detect_square(string, column):
	x1 = 0
	y1 = 0
	x2 = 0
	y2 = 0

	string = int(string)
	column = int(column)

	if string <= 2:
		y1 = 0
		y2 = 2
	
	elif string > 2 and string <= 5:
		y1 = 3
		y2 = 5
	
	elif string > 5:
		y1 = 6
		y2 = 8

	if column <= 2:
		x1 = 0
		x2 = 2

	elif column > 2 and column <= 5:
		x1 = 3
		x2 = 5

	elif column > 5:
		x1 = 6
		x2 = 8

	return (x1, y1, x2, y2)

def create_unique_set(string, column):
	all_numbers = set(range(1, 10))
	exist_numbers = set()

	our_square = detect_square(string, column)
	x1 = our_square[0]
	y1 = our_square[1]
	x2 = our_square[2] + 1
	y2 = our_square[3] + 1

	for i in range(0, 9):
		x = game_field[string][i]
		if x != 0:
			exist_numbers.add(x)

		y = game_field[i][column]
		if y != 0:
			exist_numbers.add(y)

	for i in range(y1, y2):
		for j in range(x1, x2):
			n = game_field[i][j]
			if n != 0:
				exist_numbers.add(n)

	unique_set = all_numbers - exist_numbers

	# return all_numbers, exist_numbers, unique_set
	return unique_set

def fill_game_field():

	def calc_value(value):
		if value > 9:
			return value - 9
		return value

	block_start = 1
	str_start = 1

	# по блокам из 3х строк:
	for i in range(0, 8, 3):
		str_start = block_start
		# по строкам:
		for j in range(i, i + 3):
			# по ячейкам:
			for n in range(0, 9):
				game_field[j][n] = calc_value(str_start + n)

			str_start += 3
		block_start += 1

def mix_game_field():

	global game_field

	def transpose():
		list_of_columns = []
		# по столбцам:
		for j in range(len(game_field)):
			# берем j-тую ячейку каждой строки:
			column = [game_field[i][j] for i in range(len(game_field))]
			list_of_columns.append(column)
		
		return list_of_columns

	def mix_strings():
		mixed = []
		variants = list(range(len(game_field)))
		for i in range(len(game_field)):
			n = random.choice(variants)
			mixed.append(game_field[n])
			variants.remove(n)

		return mixed

	def create_blocks(mode):
		block = []
		list_of_blocks = []

		for n in range(0, 9, 3):
			for m in range(3):
				if mode == 'str':
					block.append(game_field[m + n])
				elif mode == 'col':
					column = [game_field[i][m + n] for i in range(len(game_field))]
					block.append(column)

			list_of_blocks.append(block)
			block = []

		return list_of_blocks

	def mix_blocks(blocks):
		n = random.randint(0, len(blocks) - 1)
		print(n)
		a = blocks.pop(n)
		print(a)
		# m = random.randint(0, len(blocks) - 1)
		m = random.randint(0, 2)
		print(m)
		blocks.insert(m, a)
		for i in blocks:
			print(i)

	blocks_of_str = create_blocks('str')
	for i in blocks_of_str:
		print(i)

	mix_blocks(blocks_of_str)

	# x = random.randint(3, 5)
	# for i in range(x):
	# 	game_field = transpose()
	# 	game_field = mix_strings()


fill_game_field()
print_game_field()

mix_game_field()
# print_game_field()

# game_field[0][0] = 0
# game_field[0][5] = 0
# game_field[4][7] = 0
# game_field[8][8] = 0

# print_game_field()

# print(create_unique_set(0, 0))
# print(create_unique_set(0, 5))
# print(create_unique_set(4, 7))
# print(create_unique_set(8, 8))

# for i in range(9):
# 	for j in range(9):
# 		print(create_unique_set(i, j))

