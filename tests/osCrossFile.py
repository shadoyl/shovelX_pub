import os

__author__ = 'salmansamie'


print(os.path.join('data_out', 'xchg_list.json'))
print(os.path.normpath('./data_out/uniq_set.json'))
print(os.path.join('data_shovelled', ''))       # <--here is the problem
                                                # this is fixed with the empty char

print("\nwubba lubba dub dub\n\n")

print(os.walk('./data_shovelled'))