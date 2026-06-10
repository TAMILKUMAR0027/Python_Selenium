from configparser import ConfigParser


def get_config(category,key):
    config=ConfigParser()
    config.read("D:\\Python_Selenium_Expleo\\DemoBlaze_login\\config.ini")
    return config.get(category,key)