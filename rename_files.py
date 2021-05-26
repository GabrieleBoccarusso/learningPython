'''
simple script that renames files
Gabriele Boccarusso - begin of 2021.05 or end of 2021.04
'''

# import the python operative system library
import os
# import the python regex library
import re

# specify the path
path = 'C:\\Users\\name\\folder_1\\folder_2'

# put all the file names in a array
list_files = []

for root, dirs, files in os.walk(path):
	for file in files:
		list_files.append(file)

for file in list_files:
	complete_string = re.sub(" ", '_', complete_string)
	os.rename(path + '\\' + file, path + '\\' + complete_string)