import helpers, shlex, subprocess

def scan(sitelist):

    i = 0
    l = helpers.file_len(sitelist)

    print('scan commencing...')
    helpers.printProgress(i, l, prefix = "Scan Progress:", suffix = "Complete", barLength = 50)
    with open(sitelist) as f:

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

    print('scan completed.')
