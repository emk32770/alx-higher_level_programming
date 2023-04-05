#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        prc = a / b
    except (TypeError, ZeroDivisionError):
        prc = None
    finally:
        print("Inside result: {}".format(prc))
    return (prc)
