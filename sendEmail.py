import smtplib
from email.mime.text import MIMEText


def sendEmail(toAddr, subject, msg, credentialsFile):  
    with open(credentialsFile) as f:
        lines = f.read().split('\n')
        username = lines[0]
        fromEmail = username + "@gmail.com"
        password = lines[1]

    message = MIMEText(msg)
    message['Subject'] = subject
    message['From'] = fromEmail
    message['To'] = toAddr

    server = smtplib.SMTP('smtp.gmail.com:587')  
    server.starttls()  
    server.login(username, password)  
    server.sendmail(fromEmail, toAddr, message.as_string())  
    server.quit()
