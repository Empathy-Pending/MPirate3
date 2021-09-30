from tkinter import *
import os


def linearSearch():
    search = searchBox.get(1.0, END)
    print(search)


def createData():
    #  create later
    pass


def setup():
    f = open(os.path.split(os.path.dirname(__file__))[0] + r'\userData\data', 'r')
    data = f.read().splitlines()
    f.close()

    for i in range(len(data)):
        if i == 0 and data == '':
            createData()
        else:
            pass
    print(data)
    return data


setup()

