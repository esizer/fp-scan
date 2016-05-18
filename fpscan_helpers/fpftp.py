import getpass, urllib, urllib2, shutil
from contextlib import closing

def ftp_conn(user, server):
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
