import os

class Constants:
    KEY = ''
    if os.path.exists('key.txt'):
        with open('key.txt') as f:
            KEY = (f.read())
    else: 
        KEY = input('Enter TBA Auth key')
        with open('key.txt', 'w') as f:
            f.write(KEY)
    
    YEAR = 2022