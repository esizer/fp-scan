import sys as Sys
import os, zipfile
#
# Get the first item from a list
#
def get_first(iterable, default=None):
    if iterable:
        for item in iterable:
            return item
    return default

#
# Get the Length of the file for progress
#
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

#
#Print iterations progress
#
def printProgress (iteration, total, prefix = '', suffix = '', decimals = 2, barLength = 100):
    filledLength    = int(round(barLength * iteration / float(total)))
    percents        = round(100.00 * (iteration / float(total)), decimals)
    bar             = '#' * filledLength + '-' * (barLength - filledLength)
    Sys.stdout.write('%s [%s] %s%s %s\r' % (prefix, bar, percents, '%', suffix)),
    Sys.stdout.flush()
    if iteration == total:
        print("\n")

def zipdir(zname, zdir):
    with zipfile.ZipFile(zname, 'w', zipfile.ZIP_DEFLATED) as zf:
        for dirname, subdirs, files in os.walk(zdir):
            for f in files:
                zf.write(os.path.join(dirname, f))
