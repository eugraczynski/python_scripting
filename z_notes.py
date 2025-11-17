import argparse
import json
import zipfile
import pathlib
import os
import xml.etree.ElementTree as ET

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



def pack_the_zip():
    zipfile_path = pathlib.Path('packed_config.zip')
    mydir = 'extracted_tasks'
    with zipfile.ZipFile(zipfile_path, 'w') as zip_ref:
        for dirpath, b, filenames in os.walk(mydir):
            zip_ref.write(dirpath)
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                zip_ref.write(filepath)
        zip_ref.write('DataSetB_modified.xml')

pack_the_zip()

tree = ET.parse('./extracted_tasks/task1/DataSetB.xml')
root = tree.getroot()

itered = root.iter('Signal')
# print('DEBUG - Itered by "Signal":\n', itered)
notitered = root.findall('.//TxMessage/Signal[@name="Temperature"]')
# print("DEBUG - Itered by findall(//path/to/file'):\n", notitered)

root.append(ET.Element('Signal', attrib={'name':'Last Signal','datatype':'int','unit':'units','offset':'0'}))

def pew(elem):
    elem.attrib['name'] = 'HOTHOTHOTHOT'
    root.find('.//TxMessage').append(ET.Element('Signal', attrib={'name':'NewSignal'}))
    
for elem in notitered:
    pew(elem) if elem.attrib['name'] == 'Temperature' and \
    elem.attrib['datatype'] == 'float' and \
    elem.attrib['unit'] == 'Celsius' and \
    elem.attrib['offset'] == '0' \
        else notitered.remove(elem)

# should be at the end of file to apply indentation to whole xml
ET.indent(tree, space='    ', level=0)

root.append(ET.Element('Tail', attrib={'MyTail':'MyRules'}))
root.tail = '\n\nthis is tail, hi'

tree.write('./DataSetB_modified.xml')


