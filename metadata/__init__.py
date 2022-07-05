class MetaData:
    def __init__(self,name):
        self.__name = name
        self.__origin= {}
        self.__image_path = {}

    def add_id(self,origin,tv_id):
        self.__origin[origin] = tv_id

    def get_id(self,origin):
        return self.__origin.get(origin)


    def set_image_path(self,type,path):
        self.__image_path[type] = path

    def get_image_path(self,type):
        return self.__image_path[type]
