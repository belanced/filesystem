from .path import Path
import json
import xml.etree.ElementTree as ET
import xmltodict
from typing_extensions import List, Union

def read_json(path: str):
    data = None
    with open(path, 'r') as file:
        data = json.loads(file)
    return data

def read_txt(path: str) -> List[str]:
    valid_lines = []
    with open(path, 'r') as file: 
        lines = file.readlines(path)
        for line in lines:
            line = line.strip()
            line = line.replace('\n', '')
            if len(line) > 0: valid_lines.append(line)
    return valid_lines

# def xml_to_dict(element):
#     '''
#     Recursively converts an XML element and its children to a dictionary.
    
#     Parameters:
#     element (xml.etree.ElementTree.Element): The root element of the XML tree.
    
#     Returns:
#     dict: A dictionary representation of the XML element.
#     '''
#     # Initialize the dictionary
#     result = {}
    
#     # Add the element's attributes to the dictionary
#     if element.attrib:
#         result.update(element.attrib)
    
#     # Process child elements
#     children = list(element)
#     if children:
#         # Use the tag name as the dictionary key
#         child_dict = {}
#         for child in children:
#             child_result = xml_to_dict(child)
#             if child.tag in child_dict:
#                 if isinstance(child_dict[child.tag], list):
#                     child_dict[child.tag].append(child_result)
#                 else:
#                     child_dict[child.tag] = [child_dict[child.tag], child_result]
#             else:
#                 child_dict[child.tag] = child_result
#         result[element.tag] = child_dict
#     else:
#         # If there are no children, add the element's text
#         result[element.tag] = element.text.strip() if element.text else None
    
#     return result

def read_xml(file_path: str):
    '''
    Reads an XML file and converts it to a dictionary.
    
    Parameters:
    file_path (str): The path to the XML file.
    
    Returns:
    dict: A dictionary representation of the XML file.
    '''
    # tree = ET.parse(file_path)
    # root = tree.getroot()
    with open(file_path, 'r') as file:
        data = file.read()
    # data = read_txt(file_path)
    return xmltodict.parse(data)

def read(path: Path):
    if not isinstance(path, Path): path = Path(path)
    
    ext = path.ext()
    if ext == 'json':
        return read_json(path)
    elif ext == 'xml':
        return read_xml(path)
    elif ext == 'txt':
        return read_txt(path)
    else:
        raise NotImplementedError(f'Reading {ext} file is not implemented yet.')

def dump_json(path: str, data: dict, indent=None):
    if isinstance(indent, int) and indent > 0:
        with open(path, 'w') as file:
            json.dump(data, file, indent)
    else:
        with open(path, 'w') as file:
            json.dump(data, file)
    
def dump_xml(path: str, data: dict):
    dump_xml(path, data)

def dump_txt(path: str, data: Union[str, List[str]]):
    if isinstance(data, list):
        data = '\n'.join(data)

    with open(path, 'w') as file:
        file.write(data)




    
    

