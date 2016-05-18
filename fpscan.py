import argparse,base64, getpass, httplib, os, shutil, shlex,subprocess, urllib, urllib2

from fpscan_helpers import helpers
from contextlib import closing
from collections import OrderedDict
#
# Add arguments for FTP
#
parser = argparse.ArgumentParser(description='Download Sites File from iWeb.')
parser.add_argument('-u', '--user', help="username for server", action="store", nargs=1, dest="user")
parser.add_argument('-s', '--server', help="server address with file location", action="store", nargs=1, dest="server")

args = parser.parse_args()

if args.user is not None and args.server is None:
    parser.error("--user requires --server")
elif args.server is not None and args.user is None:
    parser.error("--server requires --user")

#
# Print head / intro
#
print("""
         _______ _______     _______ _______ _______ _______
        |\     /|\     /|   |\     /|\     /|\     /|\     /|
        | +---+ | +---+ |   | +---+ | +---+ | +---+ | +---+ |
        | | F | | | P | |   | | S | | | C | | | A | | | N | |
        | +---+ | +---+ |   | +---+ | +---+ | +---+ | +---+ |
        |/_____\|/_____\|   |/_____\|/_____\|/_____\|/_____\|

01100011 01101000 01100101 01100011 01101011 01101001 01101110 01100111
01110011 01101001 01110100 01100101 01110011  01100110 01101111 01110010
01110110 01110101 01101110 01100101 01110010 01100001 01100010 01101001
        01101100 01101001 01110100 01101001 01100101 01110011
""")

#
# Get user name and password for FTP
#

if args.user is not None and args.server is not None:

    user = helpers.get_first(args.user)
    server = helpers.get_first(args.server)

    #Get Password and try to download file
    while True:
        try:
            print "exit to close\n"
            pwd = getpass.getpass('FTP Password: ')
            if pwd == 'exit':
                print "closing..."
                exit(0)
            auth = '%s:%s' % (urllib.quote(user), urllib.quote(pwd))
            req = urllib2.Request("ftp://" + auth + '@%s' % (server))
            res = urllib2.urlopen(req)
            break
        except urllib2.URLError, e:
            print "\nIncorrect password, try again"

    # Donwload the list of sites from iWeb
    if 'res' in locals():
        print('downloading sites.txt...')
        with closing(res) as r:
            if r == urllib2.URLError:
                print
            with open('sites.txt', 'wb') as f:
                shutil.copyfileobj(r, f)

    print('sites.txt donwloaded')

i = 0
l = helpers.file_len("sites.txt")
#
# Start WP Scan
#
print('scan commencing...')
helpers.printProgress(i, l, prefix = "Scan Progress:", suffix = "Complete", barLength = 50)
with open("sites.txt") as f:

    for index, line in enumerate(f):
        chomp_line = line.rstrip()
        cmd = "./wpscan/wpscan.rb --update --batch --url " + chomp_line

        args = shlex.split(cmd)
        log = open("sites/" + chomp_line + ".txt", "a")
        log.seek(0)
        log.truncate()
        log.flush()

        p = subprocess.Popen(args, stdout=log)
        p.wait()

        i += 1
        helpers.printProgress(i, l, prefix = "Scan Progress:", suffix = "Complete", barLength = 50)
