import json
import sys


def main():
    semver = sys.argv[1]
    with open('../../package.json', 'wt', encoding='utf-8') as f:
        j = json.load(f)
        j['version'] = semver[1:]
        json.dump(j, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()
