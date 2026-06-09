import logging

from colorama import Fore


def log_generator():
    logging.basicConfig(filename="testlogreport.log",level=logging.INFO,format='%(asctime)s-%(levelname)s-%(message)s',datefmt='%y-%m-%d %H:%M:%S %p',Fore=True)
    return logging.getLogger()