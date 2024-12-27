from email.message import EmailMessage
import ssl
import smtplib
import os
import sys
import mysql.connector
import cv2

file_path1 = "mail.txt"
file_path2 = "password.txt"



row_index = sys.argv[1]
print(row_index)


#configure database
DB_CONFIG = {
'host': 'localhost',
'port': 3306,
'user': 'root',
'password': 'root',
'database': 'client_upload'
}


# connect to database
# conn = mysql.connector.connect(**DB_CONFIG)
# cursor = conn.cursor()
# cursor.execute(
#             'SELECT serial_number, title, category, video_path, privacy_status, description, keywords, date_time FROM videos where serial_number = %s', (row_index,))
# rows = cursor.fetchall()
# print(rows)
# row = rows[0]
# serial_number, title, category, video_path, privacy_status, description, keywords, date_time = row

title = "Hello world!"
video_path = "app_directory/Recording.mp4"
description = "this is a test sample of description"


#to capture first frame of the video
f = cv2.VideoCapture("../"+video_path) 
rval, frame = f.read()
cv2.imwrite('thumbnail.jpg', frame)
f.release()



# declare sende password and reciever
with open("mail.txt","r") as em: email_sender = em.read()
with open("password.txt","r") as em: email_password = em.read()
with open("rmail.txt","r") as em: email_reciever = em.read()

# declare subject body
subject = title
body = description


# frame email
em = EmailMessage()
em['from'] = email_sender
em['to'] = email_reciever
em['subject'] = subject
em.set_content('image attatched')


def sendMessage():
    # attatch the image
    with open ("thumbnail.jpg", 'rb') as f:
        file_data = f.read()
        file_type = 'jpg'
        file_name = f.name
    em.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
    context= ssl.create_default_context()
    if file_name:
        print (file_name)


    # send the image using smtp service
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_reciever, em.as_string())

sendMessage()