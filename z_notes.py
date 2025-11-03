import argparse
import json
import zipfile
import pathlib
import sqlite3

key = '{ "key": "value", "key": "value", "key": "value"}'

key2 = {'keys':'val'}
key2['pair'] = 'ars'

# keisy = str({"1":"1"})
# print(key["nested_object"]["key2"])
# print(keisy)

add = { "key1": "pair3" }
myvar = json.loads(key)
# myvar.update(add)

# print(json.dumps(myvar))


# with open('dict.json', 'r') as dict:
#     filejson = json.loads(dict.read())
# filejson.update(add)


# with open('dict.json', 'w') as json_final:
#     json_final.write(json.dumps(filejson))


zipfile_path = pathlib.Path('./extracted_tasks/Task1.zip')

with zipfile.ZipFile(zipfile_path, 'r') as zip_ref:
    zip_ref.extractall(pathlib.Path('extracted_tasks/task1'))


zipfile_path = pathlib.Path('./extracted_tasks/Task2.zip')

with zipfile.ZipFile(zipfile_path, 'r') as zip_ref:
    zip_ref.extractall(pathlib.Path('extracted_tasks/task2'))

conn = sqlite3.connect('./extracted_tasks/tast1/jsonDataSetC.dbc')
cursor = conn.cursor()

