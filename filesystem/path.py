import os, glob
from typing_extensions import List

def parse_filepath(path: str) -> List[str]:
    els = path.split('/')
    valid_els = []
    for el in els:
        if el == '.': continue
        elif el == '..': valid_els.pop()
        elif el == '~': valid_els.append(os.environ['HOME'])
        else: valid_els.append(el)
    newpath = '/'.join(valid_els)
    return os.path.abspath(newpath)


class Path(str):
    path: str

    def __init__(self, path: str=None):
        if path is None:
            self.path = os.getcwd()
            return 

        self.path = parse_filepath(path)

    def __str__(self) -> str:
        return self.path

    def __repr__(self) -> str:
        return str(self)
    
    def __truediv__(self, other: str) -> 'Path':
        return Path(os.path.join(self.path, other))
    
    @staticmethod
    def cwd() -> 'Path':
        return Path(os.getcwd())
    
    @staticmethod
    def home() -> 'Path':
        return Path(os.environ['HOME'])
    
    @staticmethod
    def proj() -> 'Path':
        current_dir = Path.cwd()
        parent_dirs = [current_dir]
        while True:
            upper_dir = parent_dirs[-1].parent()
            parent_dirs.append(upper_dir)
            if upper_dir == '/': break
        
        parent_dirs = parent_dirs[::-1]
        for this_dir in parent_dirs:
            if '.git' in this_dir.listdir():
                return this_dir
        return Path.cwd()
    
    def isabspath(self) -> bool:
        return self.path[0] == '/'
    
    def basename(self) -> str: 
        return os.path.basename(self.path)
    
    def stem(self) -> str:
        els = self.basename().split('.')
        return '.'.join(els[:-1])
    
    def ext(self) -> str:
        return self.basename().split('.')[-1]
    
    def dirname(self) -> str:
        return os.path.dirname(self.path)
    
    def parent(self) -> 'Path':
        return Path(self.dirname())
    
    def children(self) -> List['Path']:
        '''
        Returns:
            List[Path]: The children of the current path.
        '''
        els = os.listdir(self.path)
        return sorted([Path(os.path.join(self.path, el)) for el in els])
    
    def exists(self) -> bool:
        return os.path.exists(self.path)
    
    def isfile(self) -> bool:
        return os.path.isfile(self.path)
    
    def isdir(self) -> bool:
        return os.path.isdir(self.path)
    
    def islink(self) -> bool:
        return os.path.islink(self.path)
    
    def listdir(self) -> List[str]:
        return os.listdir(self.path)
    
    def glob(self, pattern: str) -> List['Path']:
        els = glob.glob(os.path.join(self.path, pattern), recursive=True)
        return sorted([Path(el) for el in els])
    
    def mkdir(self):
        os.makedirs(self.path, exist_ok=True)

    def copy(self, dst: str, verbose: bool=True):
        opt = '-rfv' if verbose else '-rf'
        os.system(f'cp {opt} {self.path} {dst}')

    def remove(self, verbose: bool=True):
        opt = '-rfv' if verbose else '-rf'
        os.system(f'rm {opt} {self.path}')
