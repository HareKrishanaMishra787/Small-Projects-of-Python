
#TODO 1. Create a dictionary in this format:

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict  = {row.letter :row.code for (index, row) in data.iterrows()}
#print(phonetic_dict)
def generate_phonetic():
    word = input("Enter the word: ").upper()
    try:
        output = [phonetic_dict[n] for n in word]
    except KeyError:
        print("Sorry , only letters in the alphabet please")
        generate_phonetic()
    else:
        print(output)
generate_phonetic()


