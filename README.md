# fp-scan
A tool used to automate scanning many WordPress sites with [WPScan](http://wpscan.org/) / [CMSmap](https://github.com/Dionach/CMSmap).

### FEATURES
- Uses domains in a sites.txt to scan.
- Saves results in a txt sites/example.com.txt
- Download generated .txt from server
- Email .zip to specified address with short summary


### INSTALL

Prerequisites:
- [WPScan](http://wpscan.org/)
- [CMSmap](https://github.com/Dionach/CMSmap)
- Python >= 2.7
- Git

Supported:
- Linux
- OSX

####Installing

    git clone https://github.com/cobraclamp/fp-scan.git
    cd fp-scan
    touch sites.txt

Install [WPScan](http://wpscan.org/) into the root directory
Install [CMSmap](https://github.com/Dionach/CMSmap)
* If you do not with to install wpscan/CMSmap directly inside, change the path in [helpers/scanner](https://github.com/cobraclamp/fp-scan/blob/master/fpscan_helpers/scanner.py#L14)
* Add domains to be scanned, each on a new line
* arguments support getting the file from FTP server

### USAGE

`python fpscan.py`

    --user      | -u <ftp username> Username of FTP
    --server    | -s <ftp url>      URL of FTP server including path to sites.txt

    --email     | -e <emails>       Comma separated list of emails

#### Examples

Download sites.txt from a production server before running

`python fpscan.py -u admin -s ftp.example.com/sites.txt`

Email results

`python fpscan.py -e first@examples.com,second@example.com`
