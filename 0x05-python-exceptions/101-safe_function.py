#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        func_result = fct(*args)
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(e))
        func_result = None
    return(func_result)
