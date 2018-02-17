#!/usr/local/bin/python3

import configparser
import os

__author__ = 'salmansamie'


config = configparser.ConfigParser()


def conf_setter():
    config['DEFAULT'] = {
        ';Path for xlsx file containing url and market IDs': '',
        'default.in.xlsx' : os.path.join('data_in', 'xchg_list.xlsx'),

        '\n;Caching location within the project': '',
        'default.shovell' : os.path.join('data_shovelled', ''),
    }

    with open(os.path.join('conf', 'config.ini'), 'w') as fp:
        config.write(fp)


# Getter for configuration file
def conf_getter(param):
    try:
        config.read(os.path.join('conf', 'config.ini'))

        if param.startswith('default.'):
            return config['DEFAULT'][param]

        # set any setting.VAR for setting up any user-defined
        # variables at the configurator.conf_setter() function
        elif param.startswith('settings.'):
             return config['SETTINGS'][param]

        else:
            print('Invalid entry queried in config.ini')
            exit(0)

    except KeyError:
        print("Keyerror found. Operation is not allowed.")
