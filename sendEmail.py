import smtplib
from email.mime.text import MIMEText


def sendEmail(credentialsPath, recipientsPath, subject, msg):  
    with open(credentialsPath) as f:
        lines = f.read().split('\n')
        username = lines[0]
        fromEmail = username + "@gmail.com"
        password = lines[1]

    recipients = []
    with open(recipientsPath, 'r') as f:
        recipients = f.read().split('\n')

    message = MIMEText(msg)
    message['Subject'] = subject
    message['From'] = fromEmail
    message['To'] = ", ".join(recipients)

    server = smtplib.SMTP('smtp.gmail.com:587')  
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(fromEmail, recipients, message.as_string())  
    server.quit()
