import pandas as pd
import urllib.request
import urllib.parse
import os

# DECK ID
# - Original EIK+ -> -12
# - G4, G5        -> -16
# - G6            -> -34
# - G7            -> -37
# - Revised (AG2) -> -30
# - Artifex       -> -31
# - Bubulcus      -> -32
# - Wizkids       -> -33
# - Corbarius     -> -36
# - J4            -> -38
DECK_ID = -38

def main():
    get_html_source()
    convert_to_csv()
    terminate()

def get_html_source():
    url = 'http://playagricola.com/Agricola/Cards/index.php'
    data = {
        's': 'type',
        'v': 'all',
        'p': 1,
        'i': 2000,
        'm': '',
        'parm': '',
        'parm2': '',
        'parm3': '',
        'parm4': '',
        'parm5': DECK_ID,
        'user': 'Unknown.',
        'password': '',
        'reg': -1
    }
    body = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url, body)
    with urllib.request.urlopen(req) as res:
        with open('index.html', mode='w') as f:
            f.write(res.read().decode('utf-8'))

def convert_to_csv():
    dfs = pd.read_html('index.html')
    df = dfs[2][['deck', 'type', 'name', 'text', 'cost', 'vps', 'prereq']]
    print(df)
    df.to_csv('result.csv')

def terminate():
    os.remove('index.html')

if __name__ == '__main__':
    main()
