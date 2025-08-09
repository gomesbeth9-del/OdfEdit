# Utility functions for OdfEdit_linux.py

def myint(val, default=None):
    try:
        if val is None:
            return default
        return int(val)
    except (ValueError, TypeError):
        return default

def mystr(val, default=None):
    if val is None:
        return default
    return str(val)

def myfloat(val, default=None):
    try:
        if val is None:
            return default
        return float(val)
    except (ValueError, TypeError):
        return default

def myfloat2str(val):
    try:
        return f"{float(val):.3f}"
    except (ValueError, TypeError):
        return "0.000"

def path2ospath(path):
    import os
    return os.path.normpath(path)
