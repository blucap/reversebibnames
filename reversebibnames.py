#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 12:43:14 2019

@author: martien
"""
import sys
import re
from pandas.io import clipboard


def get_names(s, option):
    # s = 'Johan Almenberg, Markus Andersson, Daniel Buncic, Cristina Cella, Paolo Giordani, Anna Grodecka, Kasper Roszbach, Gabriel S{\\"{o}}derberg'
    # s = 'Kate Duguid, Colby Smith and Joshua Franklin'
    d = {'z': 'Zotero', 'b': 'BibTex'}
    s = re.sub(r' and ', ', ', s.strip(), flags=re.MULTILINE)
    s = [x.strip() for x in s.split(",")]
    bibtex = ""
    zotero = ""

    for lname, fname in [q.split(" ") for q in s]:
        t = fname + ', ' + lname
        print(t)
        bibtex = bibtex + t + ' and '
    #print('\n')
    for fname, lname in [q.split(" ") for q in s]:
        t = fname + ', ' + lname
        #print(t)
        zotero = zotero + t + '\n'
    bibtex = re.sub(r' and$', '', bibtex.strip(), flags=re.MULTILINE)
    print('\nFor BibTex:\n' + bibtex)
    print('\nFor Zotero:\n' + zotero)
    if option == 'b':
        clipboard.copy(bibtex)
    else:
        clipboard.copy(zotero)
    print('Clipboard copy for', d[option])
    print('\nDone\n')
    return bibtex


def main(argv, option):
    if len(argv) > 1:
        if isinstance(argv, str):
            if argv.startswith('--help'):
                print("\nUsage for BibTex: reversebibnames -b 'Kate Duguid, Colby Smith and Joshua Franklin'")
                print("Usage for Zotero: reversebibnames -z 'Kate Duguid, Colby Smith and Joshua Franklin'\n")
            else:
                print(f"\n:{argv}.")
                try:
                    print(f"+{str(argv)}.\n")
                    return get_names(argv, option)
                except:
                    print("Check your inputs.")
    return ""


#z = main(s)


if __name__ == "__main__":
    # print(len(sys.argv))
    if len(sys.argv) == 2:
        #print('two')
        main(sys.argv[1], 'z')
    elif len(sys.argv) == 3:
        #print('three')
        if sys.argv[1].lower() in ['b', 'z']:
            main(sys.argv[2], sys.argv[1])
        else:
            print("\nPlease add string")
    else:
        print("\nPlease add string")