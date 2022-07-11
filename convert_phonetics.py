import pandas as pd

# read CSV data
data = pd.read_csv('./data/nato_phonetic_alphabet.csv')

# Turn into a {A: Alfa} dictionary with iterrows()
phonetic_dict = {row['letter']: row['code'] for (index, row) in data.iterrows()}

user_input = input('Enter a word: ').upper()  # Gets user's input and converts string into upper case for comparison
output = [phonetic_dict[char] for char in user_input]  # Stores output
print(f'Converting string...\n {output}')
