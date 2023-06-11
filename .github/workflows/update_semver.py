import json
import sys


def main():
    with open('./package.json', 'rt', encoding='utf-8') as f:
        j = json.load(f)
    newver = sys.argv[1]
    oldver = j['version']
    print(f'from {oldver} to {newver}')
    j['version'] = newver
    with open('./package.json', 'wt', encoding='utf-8') as f:
        json.dump(j, f, ensure_ascii=False, indent=4, sort_keys=True)


if __name__ == '__main__':
    main()
