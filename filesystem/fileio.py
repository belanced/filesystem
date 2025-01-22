from .path import Path
import json
import xml.etree.ElementTree as ET
import xmltodict
from omegaconf import OmegaConf as Conf
import pickle
from typing_extensions import List, Union

def read_txt(path: str) -> List[str]:
    valid_lines = []
    with open(path, 'r') as file: 
        lines = file.readlines(path)
        for line in lines:
            line = line.strip()
            line = line.replace('\n', '')
            if len(line) > 0: valid_lines.append(line)
    return valid_lines

def read_json(path: str) -> dict:
    data = None
    with open(path, 'r', encoding='UTF-8') as file:
        data = json.load(file)
    return data

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

def read_yaml(file_path: str):
    cfg = Conf.load(file_path)
    return cfg

def read_pickle(file_path: str):
    assert file_path.endswith('.pkl'), f'{file_path} is not a pickle file.'

    with open(file_path, 'rb') as file:
        data = pickle.load(file)
    return data


def read(path: Path):
    
    '''
    Reads a file and returns a dictionary representation of the file.
    
    Parameters:
    path (Path or str): The path to the file.
    
    Returns:
    dict: A dictionary representation of the file.
    
    Raises:
    NotImplementedError: If the file extension is not implemented yet.
    '''
    if not isinstance(path, Path): path = Path(path)
    assert path.exists(), f'{path} does not exist.'
    
    ext = path.ext()
    if ext in ['json']:
        return read_json(path)
    elif ext in ['xml']:
        return read_xml(path)
    elif ext in ['txt']:
        return read_txt(path)
    elif ext in ['yaml', 'yml']:
        return read_yaml(path)
    elif ext in ['pkl']:
        return read_pickle(path)
    else:
        raise NotImplementedError(f'Reading {ext} file is not implemented yet.')

def dump_json(path: str, data: dict, indent=4):
    if isinstance(indent, int) and indent > 0:
        with open(path, 'w') as file:
            file.write(json.dumps(data, ensure_ascii=False, indent=4))
    else:
        with open(path, 'w') as file:
            file.write(json.dumps(data, ensure_ascii=False))
    
def dump_xml(path: str, data: dict, encoding='utf-8'):
    root = ET.Element('root')
    for key, value in data.items():
        ET.SubElement(root, key).text = str(value)
    tree = ET.ElementTree(root)
    tree.write(path, encoding=encoding, xml_declaration=True)

def dump_txt(path: str, data: Union[str, List[str]]):
    if isinstance(data, list):
        data = '\n'.join(data)

    with open(path, 'w') as file:
        file.write(data)

def dump_yaml(path: str, data: dict):
    with open(path, 'w') as file:
        Conf.save(data, file)

def dump_pickle(path: str, data: dict):
    with open(path, 'wb') as file:
        pickle.dump(data, file)

def dump(path: Path, data: dict, indent=4):
    if not isinstance(path, Path): path = Path(path)
    
    ext = path.ext()
    if ext in ['json']:
        dump_json(path, data, indent=indent)
    elif ext in ['xml']:
        dump_xml(path, data)
    elif ext in ['yaml', 'yml']:
        dump_yaml(path, data)
    elif ext in ['pkl']:
        dump_pickle(path, data)
    else:
        try:
            dump_txt(path, data)
        except:
            raise NotImplementedError(f'Dumping {ext} file is not implemented yet.')




    
    

