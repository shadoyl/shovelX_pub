
import configparser
import os

__author__ = 'salmansamie'

'''', 'dasd', ''
; Changing the [DEFAULT] without understanding will result
; in non-functioning execution to the program execution.

'''


def config_setter():
    config = configparser.ConfigParser()

    # ./data_out/xchg_list.json
    config['DEFAULT'] = {
        'default.json.out.pa': os.path.join('./data_shovelled', ''),
        'default.json.out.uniq': './data_out/uniq_set.json',
        'default.m-thread_path': './data_shovelled/',
    }

    config['SETTINGS'] = {
        'settings.out.dir': './data_out/',
        'settings.json.con': 'xchg_list.json',
    }

    with open('tes.ini', 'w') as fp:
        config.write(fp)

config_setter()


def config_get():
    conget = configparser.ConfigParser()
    conget.read('tes.ini')

    #print(conget.sections())
    print((conget['DEFAULT']['default.json.out.pa']))


config_get()

'''
def conf_parsed(param):
    config = configparser.ConfigParser()
    config.read('./conf/config.ini')

    if param.startswith('default'):
        return config['DEFAULT'][param]

    elif param.startswith('settings'):
        return config['SETTINGS'][param]

    else:
        exit(0)


conf_parsed('')
'''