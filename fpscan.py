import argparse, os, urllib, urllib2

from fpscan_helpers import helpers, fpftp, fpemail, scanner
from collections import OrderedDict

#
# DEFAULTS
#
SEND_FROM = "Agent Smith<agentsmith@fpscan.com>"

#
# Add arguments for FTP
#
parser = argparse.ArgumentParser(
    description='Download Sites File from iWeb.'
)
parser.add_argument(
    '-u', '--user',
    help="username for server",
    action="store", nargs=1, dest="user"
)
parser.add_argument(
    '-s', '--server',
    help="server address with file location",
    action="store", nargs=1, dest="server"
)
parser.add_argument(
    '-e', '--email',
    help="define emails to send to seaprated by commas",
    action="store", nargs=1, dest="emails"
)

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
    fpftp.ftp_conn(user, server)
else:
    print("No FTP settings detected. moving on...")

#
# Start WP Scan
#
scanner.scan("./sites.txt")

if args.emails is not None:

    helpers.zipdir('scan_results.zip', './sites')
    emails = helpers.get_first(args.emails)
    vuns = helpers.detect_vuns('./sites')
    fpemail.send_mail(emails, SEND_FROM, file='scan_results.zip', vuns=vuns)

else:
    print("No emails detected. moving on...")

print "Completed Scan."
