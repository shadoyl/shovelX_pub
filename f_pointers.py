#!/usr/local/bin/python3

import json

__author__ = 'salmansamie'


# File pointers for respective file objects
class Pointers:

    def __init__(self, target_file=None, mode=None, data=None):
        self.target_file = target_file              # file nameand path to load/store
        self.data = data                            # data to load/store
        self.mode = mode                            # mode on the data

    # Object loader for files
    def sys_loader(self):
        with open(self.target_file) as load_pointer:
            sysld = json.load(load_pointer)
        load_pointer.close()
        return sysld

    # Writer object for non-json files
    def sys_writer_4file(self):
        with open(self.target_file, self.mode) as write_pointer:
            handler = write_pointer.write(self.data)
        write_pointer.close()
        return handler

    # Writer object for json files
    def sys_writer_4json(self):
        with open(self.target_file, self.mode) as write_pointer:
            handler = json.dump(self.data, write_pointer, sort_keys=True, indent=4)
        write_pointer.close()
        return handler
