import os
import smtplib
import imghdr
from email.message import EmailMessage
#for image
from PIL import Image
import urllib.request
import io


EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

contacts = ['df7@gmail.com']

msg = EmailMessage()
msg['Subject'] = 'Hello from python'
msg['From'] = EMAIL_ADDRESS
msg['To'] = contacts
msg.set_content('This is a plain text email')

#for sending html as a mail
#or
'''
msg.set_content('normal message as a alternative of html')
msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <img src="interflix.netlify.com" width=100%>
    </body>
</html>
""", subtype='html')

#sending an image from local
with open("abc.jpg","rb") as f:
    file_data=f.read()
    file_type=imghdr.what(f.name)
    file_name=f.name
'''
#sending an image from url

URL="https://picsum.photos/500"
with urllib.request.urlopen(URL) as url:
    file_data = url.read()
    file_type="jpg"
msg.add_attachment(file_data,maintype="image",subtype=file_type,filename="abc.jpg")
'''
#sending pdf from local
with open("sample.pdf","rb") as f:
    file_data=f.read()
    file_name=f.name
msg.add_attachment(file_data,maintype="application",subtype="octet-stream",filename=file_name)    
'''
'''
#sending resume from url
URL_PDF='https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf'
with urllib.request.urlopen(URL_PDF) as url:
    file_data = url.read()
    file_type="pdf"
msg.add_attachment(file_data,maintype="application",subtype="octet-stream",filename="abc.pdf")
'''

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
    print("Mail Sent")
