import logging
from pyfiglet import Figlet
from termcolor import colored
import random


def Welcome():
    num = random.randint(1, 3)
    if num == 1:
        print()
        f = Figlet(font="banner3-D")
        print(colored(f.renderText("TuLi"), 'red'))
    elif num == 2:
        f = Figlet(font="isometric2")
        print(colored(f.renderText("TuLi"), 'yellow'))
    if num == 3:
        f = Figlet(font="standard")
        print(colored(f.renderText("TuLi"), 'green'))


def Logger():
    Log_Format = "%(levelname)s %(asctime)s - %(message)s"

    logging.basicConfig(filename="logfile.log",
                        filemode="a",
                        format=Log_Format,
                        level=logging.INFO)

    return logging.getLogger()
