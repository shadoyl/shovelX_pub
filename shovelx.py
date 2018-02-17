#!/usr/local/bin/python3

from grab import Grab
import json
import shutil
import requests
import errno
import sys
import ast
import xlrd
from configurator import *
from report_cli import sys_report_src_xlsx
from f_pointers import Pointers
from threading import Thread

__author__ = 'salmansamie'

# Use store_exception[] list for global available exceptions records
# fix report cli
# ocr table scanner implementation


class ShovelX:
    def __init__(self, url):
        self.url = url

    # urllib from grab.go
    def sys_grab_module(self):
        print(self)
        grab_res = Grab(timeout=100)
        grab_res.setup(follow_location=True, connect_timeout=30)
        res_code = grab_res.go(self).code
        try:
            if res_code < 400:
                res = grab_res.go(self)
                return res.body

        except TimeoutError:
            print("Timeout thrown.")

    # In case grab/urllib module doesn't work, use request module
    def sys_request_module(self):
        r = requests.get(self, verify=False)
        # To get the ref_id for file name
        json_decoded = Pointers(conf_getter('default.to.json')).sys_loader()

        # Now to store the data to file
        store = [i['ref_id'] for i in json_decoded['data'] if self in i['URI']]
        Pointers(
            (conf_getter('default.shovell') + ''.join(store)) + '.html', 'wb', r.content
        ).sys_writer_4file()

    # Converts xlsx file to json dict
    @staticmethod
    def xlsx_dict_data():
        try:
            # get and set workbook info
            workbook = xlrd.open_workbook(conf_getter('default.in.xlsx'))

            # Getting the first Sheet of the xlsx file
            sheet_index = workbook.sheet_names()
            worksheet = workbook.sheet_by_name(sheet_index[0])

            # parse worksheet and create dict
            keys = [v.value for v in worksheet.row(0)]
            data = []
            for row_number in range(worksheet.nrows):
                if row_number == 0:
                    continue
                row_data = {}
                for col_number, cell in enumerate(worksheet.row(row_number)):
                    row_data[keys[col_number]] = cell.value
                data.append(row_data)

            jsdata = json.dumps({'data': data})

            return jsdata       # part 1: returned for data memoization

        except errno as e:
            print(e)

    # Add ref_id and generate unique list for
    @staticmethod
    def sys_ref_id_distinct():
        # Type casting from class 'str' to 'dict'
        __STR_KVAL__ = ast.literal_eval(ShovelX.xlsx_dict_data())

        # creating ref_id and update json data
        for ix in __STR_KVAL__['data']:
            u_exchg = (str(int(ix['Number'])) + '_') + (ix['Exchange Name'].replace(' ', '_'))
            ix.update({"ref_id": u_exchg})

        # Distinct URI
        distinct_data = {x['URI']: x for x in __STR_KVAL__['data']}
        listed_kval = json.dumps(list(distinct_data.values()), sort_keys=True, indent=4)
        return listed_kval      # uniq done complete

    # Eliminating non-HTTP URI
    @staticmethod
    def sys_validated_data():
        __STR_LIST__ = ast.literal_eval(ShovelX.sys_ref_id_distinct())
        validated_json = [entry for entry in __STR_LIST__ if entry['URI'].startswith('http')]
        return validated_json

    # Call sys_grab_module and local cache: IN url = OUT resp.body
    def sys_size_of(self):
        # if the response returns logical byte
        if sys.getsizeof(ShovelX.sys_grab_module(self)) != 0:       # if the returned byte is not null
            return ShovelX.sys_grab_module(self)

        elif sys.getsizeof(ShovelX.sys_request_module(self)) != 0:
            return ShovelX.sys_request_module(self)

# EOF: class ShovelX


# Thread initializer for each task under sys_proc_thread
# multithreading has been found to be more stable than multiprocessing
def thread_start():
    json_decoded = ShovelX.sys_validated_data()
    for data_blk in json_decoded:
        try:
            thread = Thread(target=sys_proc_thread, args=(data_blk,))
            thread.start()
        except Exception as e:
            print("Thread error detected. At thread_start(): " + str(e))


# Store exceptions from the
store_exception = []


# html and pdf dumped to respective path
def sys_proc_thread(data_blk):
    uri = data_blk.get('URI')
    try:
        rs_body = ShovelX.sys_size_of(data_blk.get('URI'))        # if the size is not 0
        _PDF_ = '.pdf'
        _HTML_ = '.html'
        _XLSX_ = '.xlsx'

        # create respective file formats to store data
        # Pdf writer to file
        if data_blk.get('URI').endswith(_PDF_):
            Pointers(conf_getter('default.shovell') + data_blk.get('ref_id') + _PDF_, 'wb', rs_body).sys_writer_4file()

        # Excel writer to file
        elif data_blk.get('URI').endswith(_XLSX_):
            Pointers(conf_getter('default.shovell') + data_blk.get('ref_id') + _XLSX_, 'wb', rs_body).sys_writer_4file()

        # Html writer to file
        else:
            Pointers(conf_getter('default.shovell') + data_blk.get('ref_id') + _HTML_, 'wb', rs_body).sys_writer_4file()

    except Exception as e:
        store_exception.append(uri)
        print("\nOrigin: " + uri)
        print("Error info: " + str(e) + '\n')
        pass                            # continue

    # TESTS
    #print(store_exception)
    #print(len(store_exception))


# Prepare data_shovelled path before local caching
def prepare_path():
    dir_data_shovelled = conf_getter('default.shovell')
    if os.path.isdir(dir_data_shovelled):               # rmdir if '/data_shovelled/' exists => volatile
        shutil.rmtree(dir_data_shovelled)
    os.makedirs(dir_data_shovelled)                     # make new dir for cache


# Remove files at ./data_shovelled with size of zero bytes
def rm_zero_byte():
    cur_path = os.getcwd()
    data_shovelled_path = conf_getter('default.shovell')
    shovelled_path = os.path.join(cur_path, data_shovelled_path)
    file_list = list(os.listdir(shovelled_path))        # list files at ./data_shovelled

    store_dict = dict()
    for index in file_list:
        index_path = shovelled_path + "/" + index
        index_size = os.path.getsize(index_path)        # Calculate size for files at ./data_shovelled
        store_dict[index] = index_size                  # Create dict(filename, size) for ./data_shovelled

    # get files of zero sizes
    file_keys = [key for key, value in store_dict.items() if value == 0]

    # remove all files with zero sizes in ./data_shovelled
    for file in file_keys:
        data_file = (os.getcwd() + '/' + conf_getter('default.shovell') + file)
        os.remove(data_file)
    return True


# Perfom synchronized data operations
def fetch_classify_cache():
    ShovelX.xlsx_dict_data()                # xlsx to json data conversion
    ShovelX.sys_ref_id_distinct()           # create ref_ids for indexes
    ShovelX.sys_validated_data()            # http validation before network layer exec

    prepare_path()                          # prepare path for ./data_shovelled


if __name__ == '__main__':
    conf_setter()                            # configuration setter for conf.ini data in configurator()
    #fetch_classify_cache()                  # prepare input data
    print(ShovelX.xlsx_dict_data())
    #thread_start()                          # start multi-thread
    #rm_zero_byte()                          # remove zero byte data files from ./data_shovelled

    #print(sys_report_src_xlsx()[0])     # (optional) reporting
