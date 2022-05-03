import json
import os
from difflib import get_close_matches as cm
from tokenize import String

if os.path.exists("InteractiveDictionary\data.json"):
    data = json.load(open("InteractiveDictionary\data.json"))
else:
    print("No data file")
    exit

def lookFor(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.capitalize() in data:
        return data[word.capitalize()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        similars = cm(word, data.keys(), 5, 0.8)
        if len(similars) > 0:
            print("the word does not exit. These are the nearest ones: ")
            dictionary =[]
            index = 1
            for w in similars:
                dictionary.append(w)
                print(index , " : " ,w)
                index+=1
            inp = int(input ("Does any of these words what you tried to write ? type the number near the word  to look for it or %s to close " %index))
            if inp > 0 & inp < index :
                return data[dictionary[inp - 1]]
        return "The word is not included in the dictionary"


word = input("Give a word: ")
print(lookFor(word))