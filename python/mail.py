from smtplib import SMTP
from email.utils import formataddr
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase


def sendMail():

    smtp_server = ''

    from_name = ''
    from_addr = ''

    to_addrs = ['']
    cc_addrs = ['']
    
    filename = ''
    subject = ''
    message = ''

    msg = MIMEMultipart()
    msg.attach(MIMEText(message, 'html'))
    msg['To'] = ", ".join(to_addrs)
    msg['CC'] = ", ".join(cc_addrs)
    msg['From'] = formataddr((from_name, from_addr))
    msg['Subject'] = subject 

    if filename != '':
        attachment = open(filename, 'rb')
        p = MIMEBase('application', 'octet-stream')
        p.set_payload(attachment.read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', 'attachment; filename= %s' % filename)
        msg.attach(p)

    SMTP(smtp_server).sendmail(from_addr, to_addrs+cc_addrs, msg.as_string())

    return

sendMail()
