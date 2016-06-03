import helpers, shlex, subprocess, os

def scan(sitelist):

    i = 0
    l = helpers.file_len(sitelist)

    print('scan commencing...')
    helpers.printProgress(i, l, prefix = "Scan Progress:", suffix = "Complete", barLength = 50)
    with open(sitelist) as f:

        for index, line in enumerate(f):

            chomp_line = line.rstrip()

            wp_cmd = "./wpscan/wpscan.rb --update --batch --url " + chomp_line + " --enumerate vp"
            cmsmap_cmd = "./CMSmap/cmsmap.py -t " + chomp_line + " -o sites/cmsmap_" + chomp_line + "_log.txt"

            run("wp", chomp_line, wp_cmd)
            run("cms", chomp_line, cmsmap_cmd)

            os.remove("./sites/" + chomp_line + "_cms.txt")

            i += 1
            helpers.printProgress(i, l, prefix = "Scan Progress:", suffix = "Complete", barLength = 50)

    print('scan completed.')

def run(prefix, domain, cmd):
    args = shlex.split(cmd)
    log = open("./sites/" + domain + "_" + prefix + ".txt", "a")
    log.seek(0)
    log.truncate()
    log.flush()

    p = subprocess.Popen(args, stdout=log)
    p.wait()
