import xml.etree.ElementTree as Et
from file import *

class TVShow:
    def __init__(self):
        self.__names = {
            'title':'',
            'original_title':'',
            'search_title':''
        }
        self.__episodes = {}
        self.__image_path = {}
        self.__origin = {}

    def add_id(self, origin, tv_id):
        self.__origin[origin] = tv_id

    def get_id(self, origin):
        return self.__origin.get(origin)


    def set_episode(self, season_number, episode_number, path):
        if season_number not in self.__episodes:
            self.__episodes[season_number] = {}
        self.__episodes[season_number][episode_number] = {
            'path': path
        }

    def set_name(self,type,value):
        self.__names[type] = value

    def get_name(self,type):
        return self.__names.get(type)




def load_tv(root_path: str) -> TVShow:
    """

    :param path:输入视频的根目录
                下面必须要有tvshow.nfo文件
                季文件夹下必须要有season.nfo
    :return: TVShow
    """
    tv_root = get_child(root_path)
    tv_show_full_path = tv_root.find_file('tvshow.nfo')
    if tv_show_full_path is not None： #这个根目录下面有tvshow.nfo

    tv_show_nfo = Et.parse(tv_show_full_path)
    title = tv_show_nfo.getroot().find('title').text
    original_title = tv_show_nfo.getroot().find('originaltitle').text
    tmdb = tv_show_nfo.getroot().find('tmdbid').text
    tv_show = TVShow()
    tv_show.set_name('title',title)
    tv_show.set_name('original_title',original_title)
    tv_show.set_name('search_title',original_title)
    tv_show.add_id('tmdb', tmdb)
    return tv_show


if __name__ == '__main__':
    a=load_tv('D:\\下载')
    print(a.get_name('title'))
