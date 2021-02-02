import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
data = pd.DataFrame(data)

my_dict = {row.letter: row.code for _, row in data.iterrows()}
my_dict2 = {l: c for (l, c) in zip(data.letter, data.code)}


def generate_phonetic():
    my_input = input("Enter the word: ")
    try:
        result = [my_dict2.get(n) for n in list(my_input.upper())]
        # result2 = [my_dict2[letter] for letter in list(my_input.upper())]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(result)


generate_phonetic()
