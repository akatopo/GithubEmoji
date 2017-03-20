# -*- encoding: utf-8 -*-
# CSW: ignore

import json
import sys
import urllib.request

def main():
    valid = []
    # with open('full-emoji.json', encoding=sys.getfilesystemencoding()) as fp:
    #     objs = json.load(fp)
    print('loading from internet...', end=' ', flush=True)
    page = urllib.request.urlopen('https://raw.githubusercontent.com/github/gemoji/master/db/emoji.json')
    print('Done!\nReading page...', flush=True, end=' ')
    objs = json.loads(page.read().decode('utf-8'))
    print('Done!\nConverting...', end=' ', flush=True)
    for obj in objs:
        for alias in obj['aliases']:
            valid.append([':{}: {}\t{}'.format(alias, obj.get('emoji', ''),
                                               obj.get('description', '')),
                          alias + ':'])
    print('Done!\nWriting file...', end=' ', flush=True)
    with open('emoji.json', 'wb') as fp:
        fp.write(bytes(json.dumps(valid, fp, ensure_ascii=False, indent=2), 'utf-8'))
    print('Done!')

if __name__ == '__main__':
    main()
