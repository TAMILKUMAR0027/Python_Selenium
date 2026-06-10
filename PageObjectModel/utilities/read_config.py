from configparser import ConfigParser
from os import read


def get_data(category,key):
    config=ConfigParser()
    config.read(r"D:\Python_Selenium_Expleo\PageObjectModel\configurations\config.ini")
    return config.get(category,key)