# english to pig latin
# guided program by 'automate boring stuff with python (second edition)'
print ('Enter the english message to translate into Pig Latin:')
message = input()

# creating tuple with the vowels
VOWELS = ('a', 'e', 'i', 'o', 'u'. 'y')

pigLatin = [] # A list of the words in Pig Latin
for word in message.split(): # dividing the phrase into words
	#separate the non letters at the start of this word:
	prefixNonLetters = ''
	while len(word) > 0 and not word[0].isalpha():
		prefixNonLetters += word[0]
		word = word[1:]
	if len(word) == 0:
		pigLatin.append(prefixNonLetters)
		continue