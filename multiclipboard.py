# imports
import sys
import clipboard
import json
import pandas as pd
from tabulate import tabulate

# constants
SAVED_DATA = 'clipboard.json'


def save_data(path, data):
    """Writes data into a json file."""
    with open(path, 'w') as f:
        json.dump(data, f)


def load_data(path):
    """Reads json file."""
    try:
        with open(path, 'r') as f:
            data = json.load(f)
            return data
    except:
        return {}


# Commands setup & validation
if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == 'save':
        key = input('Enter a key: ')
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print(f'Data saved into "{key}" key!')

    elif command == 'load':
        key = input('Enter a key: ')
        if key in data:
            clipboard.copy(data[key])
            print(f'Data from "{key}" copied to clipboard.')
        else:
            print(f'Uh oh! Key "{key}" does not exist...')
    elif command == 'list':

        output = pd.DataFrame(list(data.items()), columns=[
                              'Key', 'Stored data'])
        output.index = range(1, output.shape[0] + 1)

        print(tabulate(output, headers='keys', tablefmt='psql', showindex=False))
    else:
        print('Invalid command.')
else:
    print('Please pass exactly one command.')
