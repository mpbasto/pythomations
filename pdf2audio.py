import sys
import time
import json
import pyttsx3
from PyPDF2 import PdfReader


speaker = pyttsx3.init()

if len(sys.argv) == 2:
    command = sys.argv[1]

    if command == 'read':
        filepath = input(
            'This is your PDF to audio converter. To start, please enter filepath: ')
        reader = PdfReader(filepath)
        page_range = len(reader.pages)
        for page in range(page_range):
            text = reader.pages[page].extract_text()  # get text from PDF file
            # remove unnecessary spacing and line breaks
            clean_text = text.strip().replace('\n', ' ')
            print('Converting file...')
            time.sleep(3)
            speaker.say(clean_text)
            speaker.runAndWait()
            speaker.stop()

    elif command == 'save':
        filepath = input(
            'This is your PDF to audio converter. To start, please enter filepath: ')
        reader = PdfReader(filepath)
        page_range = len(reader.pages)
        for page in range(page_range):
            text = reader.pages[page].extract_text()  # get text from PDF file
            # remove unnecessary spacing and line breaks
            clean_text = text.strip().replace('\n', ' ')
            speaker.save_to_file(text, '../Desktop/audio_output.mp3')
            speaker.runAndWait()
            print('Success! Audio file saved as audio_output.mp3! Enjoy 🎧')
            speaker.stop()
    else:
        print('Invalid command.')
else:
    print('Please pass exactly one command.')
