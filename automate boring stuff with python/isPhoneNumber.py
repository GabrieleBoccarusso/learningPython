'''
program that check a phone number without regex from 'automate boring stuff'
copied to see the difference between using and non using regex
03.24.2021 - mm/dd/yyyy
'''
def isPhoneNumber(text):
	if len(text) != 12: # 1: check if the string is 12 characters
		return False
	for i in range(0, 3):
		if not text[i].isdecimal(): # 2: check if first three numbers are numbers
			return False
	if text[3] != '-': # 3: check if there is the hyphen
		return False
	for i in range(4, 7):
		if not text[i].isdecimal(): # 4: check id there are three more numbers
			return False
		if text[7] != '-': # 5: checking another hyphen
			return False
	for i in range(8, 12):
		if not text[i].isdecimal(): # 6: checking 3 numbers again
			return False
		return True # 7: if it get past everything it returns true

'''
print('Is 415-555-4242 a phone number?')
print(isPhoneNumber('415-555-4242'))
print('Is Moshi moshi a phone number?')
print(isPhoneNumber('Moshi moshi'))
'''
# finding a phone number in a larger string
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
	chunk = message[i:i+12] # 1: on each iteration 12 character get assigned to chunk
	if isPhoneNumber(chunk): # 2: if chunk pass the text it is printed
		print('Phone number found: ' + chunk)
print('Done')
'''
example by the author:
'Call me at 4'
'all me at 41'
'll me at 415'
'l me at 415-'
. . . and so on.
'''