

__author__ = 'salmansamie'


"""

exhibit 1
---------
with open(conf_parsed('default.json.out.path')) as json_file:
    json_decoded = json.load(json_file)
        

exhibit 2
---------
with open(conf_parsed('default.json.out.path')) as json_file:
    json_decoded = json.load(json_file)

    
exhibit 3
---------
with open(conf_parsed('default.json.out.path')) as jf:
    json_decoded = json.load(jf)
    
    
exhibit 4
---------
with open(conf_parsed('default.json.out.uniq')) as jf:
    json_decoded = json.load(jf)


exhibit 5
---------
with open(conf_parsed('default.json.out.uniq')) as dfp:
    json_decoded = json.load(dfp)

:::::::
WRITER:
::::::: 
        exhibit 2
        ---------
        with open(os.path.join(new_dir, new_json_file), 'w') as temp_file:
            temp_file.write(str(subprocess.Popen(
                ["python3.6", "xlsxToJson.py", "./data_in/xchg_list.xlsx", "Sheet1",
                 conf_parsed('default.json.out.path')]
            )))
            
        
        exhibit 1
        ---------
        with open((conf_parsed('default.m-thread_path') + ''.join(store)) + '.html', 'wb') as nfp:
            nfp.write(r.content)
            
            
        exhibit 5
        ---------
        with open(conf_parsed('default.m-thread_path') + data_block.get('ref_id') + _URI_PDF_, 'wb') as pfp:
            pfp.write(rs_body)
        pfp.close()
        
        
        exhibit 6
        ---------
        with open(conf_parsed('default.m-thread_path') + data_block.get('ref_id') + _URI_HTML_, 'wb') as rfp:
            rfp.write(rs_body)
        rfp.close()
        
        
exhibit 3
---------
with open(conf_parsed('default.json.out.path'), 'w') as json_file_wr:
    json.dump(json_decoded, json_file_wr, sort_keys=True, indent=4)
json_file_wr.close()


exhibit 4
---------
with open(conf_parsed('default.json.out.uniq'), 'w') as ujf:
    json.dump(list(uniq_data.values()), ujf, sort_keys=True, indent=4)
ujf.close()

"""