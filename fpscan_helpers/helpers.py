import sys as Sys
import glob, mmap, os, zipfile
from collections import OrderedDict
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

def detect_vuns(vdir):
    log_levels = ['[L]', '[M]', '[H]']
    lines = {}
    i = 0
    print "gathering vunerabilities for report..."
    for infile in glob.glob( os.path.join(vdir, '*.txt') ):
        with open(infile) as f:
            for l in f:
                if "We found" in l:
                    if "could not determine a version" not in l:
                        lines.update({infile.replace(vdir, ""): l.rstrip()})
                        i = i + 1
                for log in log_levels:
                    if log in l:
                        lines.update({infile.replace(vdir, ""): l.rstrip()})
                        i = i + 1

    if i > 0:
        print "found %s sites with potential vunerabilities" % (len(lines))
        return lines
    else:
        print "found no vunerable sites"
        return None
