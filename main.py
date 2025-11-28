import argparse
import cantools
import json
import zipfile
import pathlib
import os
import xml.etree.ElementTree as ET

key = '{ "key": "value", "key": "value", "key": "value"}'

key2 = {'keys':'val'}
key2['pair'] = 'ars'

keisy = str({"1":"1"})
# print(keisy)

add = { "key1": "pair3" }
myvar = json.loads(key)
myvar.update(add)

# print(json.dumps(myvar))

# with open('dict.json', 'r') as dict:
#     filejson = json.loads(dict.read())
#     filejson.update(add)


# with open('dict.json', 'w') as json_final:
#     json_final.write(json.dumps(filejson))


def unpack_the_zip():

    zipfile_path = pathlib.Path('./Data_to_extract/Tasks.zip')

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



def xml_changer():
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
        # ternary 
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

def db_checker():
    db = cantools.database.load_file('./extracted_tasks/task1/DataSetC.dbc')
    answer = db.messages
    # print(db)

    get_message = db.get_message_by_name("ControlCommand")
    print(get_message.signals)

    for ans in answer:
        # print('Full answer - ', ans)
        for signal in ans.signals:
            print(signal.name, \
                    signal.start, \
                    signal.length, \
                    signal.conversion.scale, \
                    signal.minimum, signal.maximum, \
                    signal.unit, \
                    signal.receivers)

# argparse section
parser = argparse.ArgumentParser(description='Process some tasks.')
parser.add_argument('-z', '--zoo', help='Print animals')
parser.add_argument('-n', '--numerics', help='Numeric sum', type=float, nargs='*')
parser.add_argument('-v', '--verbose', type=int, choices=[1,2,3], help='Enable verbose output 1, 2, 3 etc.')
parser.add_argument('--unpack', action='store_true', help='Unpack the zip files')
parser.add_argument('--checkdb', action='store_true', help='Check the DBC file')
parser.add_argument('--changexml', action='store_true', help='Change the XML file')
parser.add_argument('--pack', action='store_true', help='Pack the modified files into a zip')

args = parser.parse_args()

# print(args)

if args.numerics is not None:
    print(f'Numeric inputs: {args.numerics}')
    print(sum(args.numerics))

if args.unpack:
    unpack_the_zip()

if args.checkdb:
    db_checker()

if args.changexml:
    xml_changer()

if args.pack:
    pack_the_zip()

if args.verbose is not None:
    match args.verbose:
        case 1:
            print('Verbose level 1 enabled')
        case 2:
            print('Verbose level 2 enabled')
        case 3:
            print('Verbose 3 enabled')
        # never called because of argparse choices
        case _:
            print('Wrong verbose input')

if args.zoo is not None:
    match args.zoo:
        case 'cats' | 'cat':
            print('Meow! Meow!')
        case 'dogs':
            print('Woof! Woof!')
        case 'birds':
            print('Chirp! Chirp!')
        case _:
            print("That's not an animal. \nBut you are!")



unpack_the_zip()
db_checker()
xml_changer()
pack_the_zip()