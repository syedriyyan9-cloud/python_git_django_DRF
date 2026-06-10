#example

file = open('example.txt', 'w')
file.write('Hello, world!')
file.close()


file = open('example.txt', 'r')
content = file.read()
print(content)
file.close()

with open('example.txt', 'w') as f:
    f.write('Automatically closed!')
# No need to call .close() - it's done for you

with open('example.txt', 'r') as f:
    for line in f:
        print(line.strip())  # strip() removes the newline

import csv

with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['Alice', 30, 'New York'])

import csv

with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(f'Name: {row[0]}, Age: {row[1]}, City: {row[2]}')


import csv

with open('data.csv', 'r') as f:
    dict_reader = csv.DictReader(f)
    for row in dict_reader:
        print(row['Name'], row['Age'])

import csv

with open('output.csv', 'w', newline='') as f:
    fieldnames = ['Name', 'Age']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Name': 'Bob', 'Age': 25})

import json

data = {'name': 'Alice', 'age': 30, 'city': 'New York'}
with open('data.json', 'w') as f:
    json.dump(data, f)  # writes directly to file

import json

with open('data.json', 'r') as f:
    loaded = json.load(f)  # reads from file
print(loaded['name'])      # 'Alice'
print(type(loaded))        # dict

import json

data = {'name': 'Bob', 'hobbies': ['reading', 'gaming']}
json_string = json.dumps(data, indent=2, sort_keys=True)
print(json_string)

import json

bad_json = '{"name": "Charlie", "age": 025}'  # leading zero in number
try:
    data = json.loads(bad_json)
except json.JSONDecodeError as e:
    print(f'Invalid JSON: {e}')

with open('image.jpg', 'rb') as src, open('copy.jpg', 'wb') as dst:
    dst.write(src.read())  # copies binary data chunk by chunk

with open('large.bin', 'rb') as f:
    while chunk := f.read(4096):  # walrus operator reads 4KB at a time
        #process(chunk)  # do something with binary data
        pass

from pathlib import Path

p = Path('data')
p.mkdir(exist_ok=True)          # create directory safely
(p / 'info.txt').write_text('Hello')  # Path joins like /
print(Path('info.txt').read_text())

import tempfile

with tempfile.NamedTemporaryFile(mode='w', delete=True) as tmp:
    tmp.write('secret data')
    tmp.seek(0)                 # go back to start before reading
    print(tmp.read())           # file is automatically deleted after block

import pickle

data = {'list': [1, 2, 3], 'tuple': (4, 5)}
with open('data.pkl', 'wb') as f:
    pickle.dump(data, f)
with open('data.pkl', 'rb') as f:
    restored = pickle.load(f)   # tuple comes back as tuple!


