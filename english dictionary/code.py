from json import load
from difflib import SequenceMatcher, get_close_matches
data = load(open("data/data.json"))

def translate(w) -> str:
    ret_var = ''
    w = w.lower()
    # of the word is the data
    if w in data:
        # we return the word
        ret_var = data[w]
    else: # otherwise
        # we check if there is a similar word 
        diff_w = get_close_matches(w, data.keys(), n = 1)
        if diff_w == []:
            ret_var = "the word doesn't exists"
        else:
            ret_var = "maybe you meant " + diff_w[0]
    
    # beware of spaghetti code
    return ret_var

def main() -> int:
    loop: str = 'y'
    word: str = ''

    while(loop[0] == 'y'):
        word = input("enter a word: ")
        word = translate(word)
        # if the word content is a list means that we 
        # received a list of meanings
        if type(word) == list:
            for i in range(len(word)):
                print("definition", i+1, ':', word[i])
        else: # otherwise we receive a simple message to display
            print(word)


        loop = input("do you want to enter another word? ")

    return 0

main()