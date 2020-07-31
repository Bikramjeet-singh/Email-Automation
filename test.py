import pandas as pd
import time
import ssl
import smtplib
from socket import gaierror
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

e = pd.read_csv("your_csv_file.csv")     #insert your csv file here.

fromname='sender_name'
fromaddr='sender_email@gmail.com'        #sender credentials  here.
frompass='sender_pass'
subject = 'Subject here'




for row in e.itertuples():

    time.sleep(3)

    server = smtplib.SMTP_SSL('smtp.gmail.com',timeout=2000)
   
    server.connect('smtp.gmail.com',465)
    server.ehlo()
    server.login(fromaddr,frompass)
    time.sleep(3)

    toaddr= row.Mail_id
    

    msg=MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject
    body= ("""
  


        """  
        #Body here.

        """

    """)

    msg.attach(MIMEText(body, 'plain'))


    fp = open('image_file_here.jpeg','rb')    #Attachment as jpg file here.
    img = MIMEImage(fp.read())
    fp.close()
    img.add_header('Content-ID', '<{}>'.format('image_file_here.jpeg'))
    msg.attach(img)
    text = msg.as_string()
    try:
        server.sendmail(fromaddr, toaddr, text)
        print("Email to {} is sent successfully".format(row.Mail_id))
        server.quit()
        time.sleep(2)
    except Exception as e:
        print('Email to could not be sent :( because {}'.format(str(e)))
