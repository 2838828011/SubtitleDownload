from os import listdir
from os.path import isfile, isdir


class SimpleFile:
    def __init__(self, father_path, files: list, dirs: list):
        self.__father_path = father_path
        self.__files = files
        self.__dirs = dirs

    def files(self):
        return tuple([f'{self.__father_path}{_}' for _ in self.__files])

    def dirs(self):
        return tuple([f'{self.__father_path}{_}' for _ in self.__dirs])

    def __find(self, data: list, path, full=True ,func = lambda x,y:x==y) -> bool or str:
        find = None
        for i in data:
            if func(i,path) is True:
                if full is True:
                    find = f'{self.__father_path}{i}'
                else:
                    find = i
        return find

    def find_file(self, path, full=True ,func = lambda x,y:x==y):
        return self.__find(self.__files, path, full=full ,func = func)

    def find_dir(self, path, full=True ,func = lambda x,y:x==y):
        return self.__find(self.__dirs, path, full=full ,func = func)


def get_child(path: str) -> SimpleFile:
    if path[-1] != '/':
        path = path + '/'

    if isdir(path):
        files, dirs = [], []
        for i in listdir(path):
            if isdir(f'{path}{i}'):
                dirs.append(i)
            elif isfile(f'{path}{i}'):
                files.append(i)
        return SimpleFile(
            father_path=path,
            files=files,
            dirs=dirs
        )

    else:
        return SimpleFile(
            father_path=path,
            files=[],
            dirs=[]
        )
