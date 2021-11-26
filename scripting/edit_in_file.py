'''
Gabriele Boccarusso - 26/11/2021
This script edits an file that can be opened through any text editor,
so txt, srt and etc.
'''
import os

def main():
	path:str = 'C:\\Users\\gabri\\Desktop\\Logo Trend Report 2021'

	for i in os.listdir(path):
    if i.endswith('.extension'):
    	modify(path + '\\' +  i)


def modify(filepath:str):
        file = open(filepath, 'r+')
        lines = file.readlines()

        for i, line in enumerate(lines):
                if 'requisite' in line:
                        lines[i] = 'new line\n'
        file.close()

        with open(filepath, 'r+') as file:
                file.writelines(lines)        
