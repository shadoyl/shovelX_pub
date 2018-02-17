#!/usr/local/bin/python3

import os
from bs4 import BeautifulSoup
import lxml

__author__ = 'salmansamie'


def merger_index():
    files = os.listdir('data_shovelled')
    new_list = list()

    try:
        for file in files:
            if file.endswith('.html'):
                # link to conf file after the construct below
                new_list.append(os.path.abspath(os.path.join('data_shovelled', file)))

        for index in new_list:
            print("***" + index)
            fp = open(index, 'r')
            soup = BeautifulSoup(fp, "html.parser")

            print(soup.prettify())

    except UnicodeDecodeError:
        pass


merger_index()
