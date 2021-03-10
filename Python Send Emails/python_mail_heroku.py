import os
import smtplib
import imghdr
from email.message import EmailMessage
import urllib.request
import io


EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

contacts = ['ssss@gmail.com']

msg = EmailMessage()
msg['Subject'] = 'Hello from python'
msg['From'] = EMAIL_ADDRESS
msg['To'] = contacts
msg.set_content('This is a plain text email')

m="hellooooooo"
msg.set_content('normal message as a alternative of html')
msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <img src="https://picsum.photos/500" width=100%>
    </body>
</html>
""", subtype='html')


'''
<!DOCTYPE html>
<html>
<style>
	.parent{
    position:relative;
    }
    img{
    padding:0;
    }
    
    .child{
    position:absolute;
    top:0;
    left:0;
    bottom:0;
    right:0;
    }
</style>
    <body>
    <div class="parent">
     <img src="https://picsum.photos/500" width=100%>
    </div>
    <div class="child">
    <p>hello brother </p>
    </div>
    
    
       
    </body>
</html>
'''




with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
    print("Mail Sent")
