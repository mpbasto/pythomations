import pandas as pd

# read CSV data
data = pd.read_csv('./data/nato_phonetic_alphabet.csv')

# Turn into a "{A: Alfa}" dictionary with iterrows()
phonetic_dict = {row['letter']: row['code'] for (index, row) in data.iterrows()}

def generate_phonetics():
    """
    Function that gets the user's input (type ```str```) and converts each character into the respective phonetic counterpart, as per the NATO Alphabet.
    """
    user_input = input('Enter a word: ').upper()  # Gets user's input and converts string into upper case for comparison
    try:
        output = [phonetic_dict[char] for char in user_input]  # Stores output
    except KeyError:
        print('Sorry, only letters in the alphabet please.')
        generate_phonetics()
    else:
        print(f'Converting string...\nOutput: {output} \nGoodbye! 👋')


generate_phonetics()
