import json
import sys
import re

def main():

    abbrev_file = 'journal_abbreviations.json'
    with open(abbrev_file) as f:
        journal_abbrev = json.load(f)

    infile = sys.argv[1]
    with open(infile, 'r') as f:
        file = f.read()
        lines = file.split('\n')

    for i, line in enumerate(lines):
        if 'journal = ' in line:
            journal = re.search(r'(?<=\{).*?(?=\})', line).group(0)
            if journal in journal_abbrev:
                lines[i] = line.replace(journal, journal_abbrev[journal])

    with open(infile, 'w') as f:
        filedata = '\n'.join(lines)
        f.write(filedata)

if __name__ == '__main__':
    main()