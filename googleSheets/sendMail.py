import smtplib
from email.message import EmailMessage
from .getBlogContent import blogHeaders
import datetime


def sendBlogEmail(address):
  server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
  server.login("lobsteautravel", "$uchaBud")
  msg = EmailMessage()
  msg['Subject'] = datetime.date.today().strftime("%B %d, %Y") + " - Claire and Nate's Travel Blog Update"
  msg['From'] = "Claire and Nate's Travel Blog"
  msg['To'] = address

  msgContentPlain = ""
  msgContentHTML = ""

  for post in blogHeaders:
      msgContentPlain += f"""
      {post['title']} - {post['pubDate']}
      {post['desc']}
      {post['author']}
      \
      \
      """
      msgContentHTML +=f""" 
      <br>
      <h3> <a href = {post['link']}>{post['title']} - {post['pubDate']} </a></h3>
      <p>{post['desc']}</p>
      <p><b>{post['author']}</b></p>
      
      """


  msg.set_content(f"""
  Hello friends and family,

  Here are our most recent travel blog posts - 

  {msgContentPlain}

  For all our posts, go to thebahblog.com
  """)

  msg.add_alternative(f"""\
  <html>
    <head></head>
    <body>
    <div class = 'container jumbotron'>
      <p>Hello friends and family,</p>
      <p><b>Here are our most recent travel blog posts - </b></p>
        {msgContentHTML}
        <br>
        <p>For all our posts, go to <a href="http://thebahblog.com">thebahblog.com</a>
        </p>
    </div>
    </body>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
  </html>
  """,subtype='html')

  server.send_message(msg)
  server.quit()
