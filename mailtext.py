import smtplib
from email.mime.text import MIMEText
import datetime

def send_mail():
    to = 'xxyyyzzz@gmail.com'
    from_email = 'email_id_is@gmail.com'
    from_email_pass = '*******'
    smtpserver = smtplib.SMTP('smtp.gmail.com',587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()

    smtpserver.login(from_email,from_email_pass)

    at_time = datetime.date.today()
    c = datetime.time()
    msg = MIMEText('The Pit is Full on %s' % at_time.strftime('%b %d %y') )
    msg['Subject'] = 'Raspberry PI3'
    msg['From'] = 'behungrybefoolish007@gmail.com'
    msg['To'] = '15ucc043@lnmiit.ac.in'

    smtpserver.sendmail(from_email,[to],msg.as_string())
    smtpserver.quit()


