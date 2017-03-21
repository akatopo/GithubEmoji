# -*- encoding: utf-8 -*-
# CSW: ignore

"""
For updating the json list. It cannot be run by the final user.

To run, you can just built it, but you need to have python installed on your system.

What you can also to is run it from sublime text iteslf. Just paste this in the console:

from GithubEmoji.getemojis import getemojis; getemojis()
"""

import json
import sys
import urllib.request

def getemojis():
    valid = []
    print('loading from internet...', end=' ', flush=True)
    page = urllib.request.urlopen('https://raw.githubusercontent.com/github/gemoji/master/db/emoji.json')
    print('Done!\nReading page...', flush=True, end=' ')
    objs = json.loads(page.read().decode('utf-8'))
    print('Done!\nConverting...', end=' ', flush=True)
    for obj in objs:
        for alias in obj['aliases']:
            valid.append([alias, obj.get('emoji', ''), obj.get('description', '')])
    print('Done!\nWriting file...', end=' ', flush=True)
    with open('emoji.json', 'wb') as fp:
        fp.write(bytes(json.dumps(valid, fp, ensure_ascii=False, indent=2), 'utf-8'))
    print('Done!')

if __name__ == '__main__':
    getemojis()
