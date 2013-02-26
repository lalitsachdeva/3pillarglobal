import smtplib

sender = 'lalit.sachdeva@3pillarglobal.com'
receivers = 'priyanka.gupta@3pillarglobal..com'

message = """From: From Person <lalit.sachdeva@3pillarglobal.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('smtp.googlemail.com',993)
   smtpobj.login("lalit.sachdeva@3pillarglobal.com","password")
   smtpObj.sendmail(sender, receivers, message)         
   print ("Successfully sent email")
except SMTPException:
   print ("Error: unable to send email")