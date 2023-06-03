import base64

from os import path
from sys import argv

filename = argv[1] or 'mysql-blind'

if path.isfile(filename):
    file = open(filename)
else:
    raise Exception(f'File Not Found: {filename}')

lines = file.readlines()

for line in lines:
    linebytes = line.encode('ascii')
    b64line_bytes = base64.b64encode(linebytes)
    b64line_string = b64line_bytes.decode('ascii')
    print(b64line_string)

