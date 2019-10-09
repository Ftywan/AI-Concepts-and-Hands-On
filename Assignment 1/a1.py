# five_x_cubed_plus_two(3) -> 137
def five_x_cubed_plus_2(num):

	return num ** 3 * 5 + 2

# triple_up([2, 5, 1.5, 100, 3, 8, 7, 1, 1, 0, -2])  ->  [[2, 5, 1.5], [100, 3, 8], [7, 1, 1], [0, -2]]
def triple_up(array):
	new_array = []
	count = 0
	for i in range(len(array) / 3):
		row = []
		for j in range(3):
			row.append(array[count])
			count = count + 1
		new_array.append(row)

	row = []
	for i in range(count, len(array)):
		row.append(array[i])
	new_array.append(row)

	return new_array

# mystery_code("abc Iz th1s Secure? n0, no, 9!") -> "VWX dU OC1N nZXPMZ? I0, IJ, 9!"
def mystery_code(string):
	new_string = ''
	for i in range(len(string)):
		ascii_num = ord(string[i])
		# upper case
		if ascii_num >= 97 and ascii_num <= 122:
			encoded = chr((ascii_num - 97 + 21) % 26 + 65)
			new_string = new_string + encoded
		# lower case
		elif ascii_num >= 65 and ascii_num <= 90:
			encoded = chr((ascii_num - 65 + 21) % 26 + 97)
			new_string = new_string + encoded
		else:
			new_string = new_string + string[i]

	return new_string


# future_tense(['Yesterday', 'I', 'ate', 'pasta', 'and', 'today', 'I', 'am', 'having', 'soup']) ->
#  ['Tomorrow', 'I', 'will', 'eat', 'pasta', 'and', 'tomorrow', 'I', 'will', 'be', 'having', 'soup']
def future_tense(sentence):
	mapping_sheet = {
		"am": "will be",
		"is": "will be",
		"are": "will be",
		"was": "will be",
		"were": "will be",
		"being": "will be",
		"go": "will go",
		"goes": "will go",
		"went": "will go",
		"going": "will go",
		"eat": "will eat",
		"ate": "will eat",
		"eats": "will eat",
		"eating": "will eat",
		"have": "will have",
		"has": "will have",
		"had": "will have",
		"having": "will have",
		"today": "tomorrow",
		"yesterday": "tomorrow",
		"now": "tomorrow",
		"Today": "Tomorrow",
		"Yesterday": "Tomorrow",
		"Now": "Tomorrow"
	}

	future_tense = []
	for x in sentence:
		if x in mapping_sheet:
			future_word = mapping_sheet[x].split(" ")
			for y in future_word:
				future_tense.append(y)
		else:
			future_tense.append(x)

	return future_tense



if __name__ == "__main__":
	print(mystery_code(input()))