#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_keys = list(a_dictionary.keys())

    for vdict in list_keys:
        if value == a_dictionary.get(vdict):
            del a_dictionary[vdict]

    return (a_dictionary)
