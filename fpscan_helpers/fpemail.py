import smtplib
import datetime
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from time import gmtime, strftime

from collections import OrderedDict

def send_mail(send_to, send_from, subject="FP Scan", file=None, server="127.0.0.1", vuns=None):

    d = datetime.datetime.now()
    date = d.strftime("%A, %B %d, %Y at %H:%M")

    text = "<h2>FP Scan completed (" + date + ")</h2>"

    if vuns is not None:
        vuns_string = "<br />"
        for i, v in vuns.items():
            vuns_string = vuns_string + "<li style=\"color:#FF0000;\">%s<strong>%s</strong></li>" % (v, i)
        new_text = """
            <span style=\"color:#FF0000;\">
                We found <strong>{0}</strong> sites with vunerabilities
            </span>:
            <ul>
                {1}
            </ul>
        """.format(len(vuns), vuns_string)
        text = text + new_text
    else:
        #text = text + "<span style:color=\"#00D318;\">Congrats! We couldn't find any vunerable sites.</span>"
        text = text + "<img src=\"http://floating-point.com/fpscan.jpg\" alt=\"No Vunerabilities Found\" />"

    if ',' in send_to:
        print "multiple emails"
        send_to = send_to.split(",")
        send_to = ", ".join(send_to)

    print "building message"
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = send_from
    msg['To'] = send_to
    msg['Date'] = formatdate(localtime=True)

    msg.attach(MIMEText(text, 'html'))

    if file is not None:
        print("attaching file...")
        with open(file, "rb") as f:
            msg.attach(MIMEApplication(
                f.read(),
                Content_Disposition='attachment; filename="%s"' % f,
                Name="site_results.zip"
            ))
        print("file attached")
    smtp = smtplib.SMTP(server)
    print("sending mail...")
    smtp.sendmail(send_from, send_to, msg.as_string())
    print("mail sent\nclosing connection...")
    smtp.close()
    print("connection closed")
