import smtplib
import datetime
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from time import gmtime, strftime

def send_mail(send_to, send_from, subject="FP Scan", file=None, server="127.0.0.1"):

    d = datetime.datetime.now()
    date = d.strftime("%A, %B %d, %Y at %H:%M")

    text = "FP Scan completed (" + date + ")"

    print "building message"
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = send_from
    msg['To'] = send_to
    msg['Date'] = formatdate(localtime=True)

    msg.attach(MIMEText(text))


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
