# -*- coding: utf-8 -*-
"""Скрипт для парсинга xml"""
import os

from bs4 import BeautifulSoup


def get_xml(file):
    """ Функция находит строку содержащую минифицированный xml код """
    output = "xml code not found"
    for line in file:
        if ("<" in line and "</" in line):
            output = line.split('"', 1)[1] 
            while (output[-1] != '"'):
                output = output[:-1]
            output = output[:-1]

            output = output.replace("\n", "")
            output = output.replace("\t", "")
            output = BeautifulSoup(output).prettify()

    return output


# Дирректория входных данных
path_input = 'input/'
# Дирректория выходных данных
path_output = 'output/'

# Перебор файлов в директории input/ с последующей записью выхода в output/
for filename in os.listdir(path_input):
    file_input = open(path_input + filename, 'r')
    file_output = open(path_output + filename.split(".")[0]+".xml", 'w')

    file_output.write(get_xml(file_input))

    print(filename)
