import json
import sys


def main():
    semver = sys.argv[1]
    with open('./package.json', 'rt', encoding='utf-8') as f:
        j = json.load(f)
    oldver = j['version']
    newver = semver[1:]
    print(f'from {oldver} to {newver}')
    j['version'] = newver
    with open('./package.json', 'wt', encoding='utf-8') as f:
        json.dump(j, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()
