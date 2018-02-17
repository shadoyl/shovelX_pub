#!/usr/local/bin/python3

import tabulate
import json

__author__ = 'salmansamie'


# For status reporting
def sys_report_src_xlsx():
    json_obj = json.loads(open('./data_out/xchg_list.json').read())

    valid_uri = []
    valid_xlsx = []
    valid_exchg_id = []

    invalid_uri = []
    invalid_xlsx = []
    invalid_exchg_id = []

    for ix in json_obj["data"]:

        if "http" in ix["URI"]:
            valid_uri.append(ix["URI"])
            valid_exchg_id.append(ix["Exchange Name"])
            valid_xlsx.append(ix["Number"])

        elif "http" not in ix["URI"]:
            invalid_uri.append(ix["URI"])
            invalid_exchg_id.append(ix["Exchange Name"])
            invalid_xlsx.append(ix["Number"])

    # tabulate URI with VALID address
    tr_count_val = range(1, len(valid_uri) + 1)
    headers_val = ['Exchange Name', 'Calendar URI', 'Exchange ID']
    table_val = zip(tr_count_val, valid_exchg_id, valid_uri, valid_xlsx)
    valid_table = tabulate.tabulate(table_val, headers=headers_val, tablefmt='grid')

    # tabulate URI with INVALID address
    tr_count_inval = range(1, len(invalid_uri) + 1)
    headers_inval = ['Exchange Name', 'Calendar URI', 'Exchange ID']
    table_inval = zip(tr_count_inval, invalid_exchg_id, invalid_uri, invalid_xlsx)
    invalid_table = tabulate.tabulate(table_inval, headers=headers_inval, tablefmt='grid')

    return [valid_table, invalid_table, dict(zip(valid_exchg_id, valid_uri))]
