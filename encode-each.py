#!/usr/bin/python
import argparse
import base64

from os import path
from sys import argv

parser = argparse.ArgumentParser(prog="encode-each", description="Loop through lines of file and base64 encode each one")
parser.add_argument('inputfile', type=argparse.FileType('r', encoding='UTF-8'))
parser.add_argument('--outfile', type=argparse.FileType('w'), help='save results')
parser.add_argument('--exceptions', type=argparse.FileType('w'), help='save exceptions')

def encode(file, outfile, exceptionfile):

    lines = file.readlines()
    results = ""
    exceptions = ""
    for line in lines:
        try:
            linebytes = line.encode('ascii')
            b64line_bytes = base64.b64encode(linebytes)
            b64line_string = b64line_bytes.decode('ascii')
            if outfile:
                results = results + f'{b64line_string}\n'
            print(b64line_string)
        except Exception as e:
            if exceptionfile:
                exceptions += line
            print(f'could not encode {line}')

    if outfile:
        outfile.write(results)
    if exceptionfile:
        exceptionfile.write(exceptions)
        
if __name__ == '__main__':
    args = parser.parse_args()
    encode(args.inputfile, args.outfile, args.exceptions)
