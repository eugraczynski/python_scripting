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


zipfile_path = pathlib.Path('Tasks.zip')

with zipfile.ZipFile(zipfile_path, 'r') as zip_ref:
    zip_ref.extractall(pathlib.Path('extracted_tasks/'))

zipfile_path = pathlib.Path('./extracted_tasks/Task1.zip')

with zipfile.ZipFile(zipfile_path, 'r') as zip_ref:
    zip_ref.extractall(pathlib.Path('extracted_tasks/task1'))


zipfile_path = pathlib.Path('./extracted_tasks/Task2.zip')

with zipfile.ZipFile(zipfile_path, 'r') as zip_ref:
    zip_ref.extractall(pathlib.Path('extracted_tasks/task2'))


import xml.etree.ElementTree as ET

tree = ET.parse('./extracted_tasks/task1/DataSetB.xml')
ET.indent(tree, space='    ', level=0)
# print(type(tree))
# print(tree.getroot())
root = tree.getroot()
# print(root.tag, root.attrib['name'], root[0][0])

# for child in root:
#     print(child)




itered = root.iter('Signal')
notitered = root.findall('.//Signal')
print(notitered)

root.findall('.//Signal[@name="Temperature"]')
root.append(ET.Element('Signal', attrib={'name':'NewSignal','datatype':'int','unit':'units','offset':'0'}))

def pew(elem):
    elem.attrib['name'] = 'HOTHOTHOTHOT'
    elem.tail
    root.find('.//TxMessage').append(ET.Element('Signal', attrib={'name':'NewSignal'}))
    
for elem in notitered:
    pew(elem) if elem.attrib['name'] == 'Temperature' and \
    elem.attrib['datatype'] == 'float' and \
    elem.attrib['unit'] == 'Celsius' and \
    elem.attrib['offset'] == '0' \
        else notitered.remove(elem), 
    # pew(elem)
    print(elem.attrib)
tree.write('./DataSetB_modified.xml')
# [elem.tag for elem in root.iter()]
