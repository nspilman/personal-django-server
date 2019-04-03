import smtplib
from email.message import EmailMessage

def sendEmail(email, password, to, sender, subject, message):
  server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
  server.login(email, password)
  msg = EmailMessage()
  msg['Subject'] = subject
  msg['From'] = sender
  msg['To'] = to

  msg.set_content(message)

  server.send_message(msg)
  server.quit()