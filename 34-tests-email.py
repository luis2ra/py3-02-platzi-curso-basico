import smtplib

s=smtplib.SMTP("smtp.gmail.com", 587)
s.starttls()
s.login(user="luis2ra@gmail.com", password="erazinekvncavvci")
message='''
From: luis2ra@gmail.com
Subject: Esto es una prueba

This is a test 
'''
s.sendmail(from_addr="luis2ra@gmail.com", to_addrs="luis.altuve@protonmail.com", msg=message)
