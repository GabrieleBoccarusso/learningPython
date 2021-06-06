from json import load
from difflib import SequenceMatcher
data = load(open("data/data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    else:
        return findSimilar(w)

def findSimilar(w):
    for i in data.keys(): # linear search O(n)
        # print(i)
        if SequenceMatcher(a = w, b = i).ratio() > 0.8:
            return "maybe you meant " + i


def main() -> int:
    loop: str = 'y'
    word: str = ''

    while(loop[0] == 'y'):
        word = input("enter a word: ")
        print(translate(word))

        loop = input("do you want to enter another word? ")

    return 0

main()