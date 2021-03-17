'''
table printer exercise from 'automate boring stuff with python (second edition)'
chapter six page 188, first project
3.17.2021 (dd-mm-yyyy)
Gabriele Boccarusso
'''
tableData = [['apples', 'oranges', 'cherries', 'banana'],
						 ['Alice', 'Bob', 'Carol', 'David'],
						 ['dogs', 'cats', 'moose', 'goose']]

# iterating through the matrix
for i in range(len(tableData)):
	maxlength = 0
	# iterating through the column to find the longest word
	for j in range(len(tableData[i])):
		if len(tableData[i][j]) > maxlength:
			maxlength = len(tableData[i][j])
	# iterating over the column again to add
	# padding to shorter words
	for j in range(len(tableData[i])):
		if len(tableData[i][j]) < maxlength:
			justify = (maxlength - len(tableData[i][j])) + len(tableData[i][j])
			tableData[i][j] = tableData[i][j].rjust(justify)

# this works only if every rows has the same length of elements
for x in range(len(tableData[0])):
	for i in range(len(tableData)):
		print(tableData[i][x], end = ' ')
	print()