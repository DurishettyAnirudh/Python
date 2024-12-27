from email.message import EmailMessage
from password import user_mail, user_password
import ssl
import smtplib
import os

file_path1 = "mail.txt"
file_path2 = "password.txt"
if not(os.path.exists(file_path1) and os.path.exists(file_path2)):
    with open(file_path1, "w") as f:
        f.write("mail")

    with open(file_path2, "w") as f:
        f.write("password")

# declare sende password and reciever
with open("mail.txt","r") as em: email_sender = em.read()
with open("password.txt","r") as em: email_password = em.read()
with open("rmail.txt","r") as em: email_reciever = em.read()

# declare subject body
subject = "Danger alert! Unsuccessful attempt to login"
body = """
If you watch this, 
then successfully alert has been sent and its working
"""


# frame email
em = EmailMessage()
em['from'] = email_sender
em['to'] = email_reciever
em['subject'] = subject
em.set_content('image attatched')


def sendMessage():
    # attatch the image
    with open ('Culprit.jpg', 'rb') as f:
        file_data = f.read()
        file_type = 'jpeg'
        file_name = f.name
    em.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
    context= ssl.create_default_context()


    # send the image using smtp service
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_reciever, em.as_string())
