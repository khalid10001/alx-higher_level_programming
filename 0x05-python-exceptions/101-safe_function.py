#!/usr/bin/python3

def safe_function(fct, *args):
    import sys
    try:
        n = fct(*args)
        return n
    except Exception as r:
        print("Exception: {}".format(r), file=sys.stderr)
        return None
