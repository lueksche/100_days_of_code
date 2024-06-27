# import smtplib

# my_email = "lukassmtptest@gmail.com"
# password = "khcx tvji fywp jjik"
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, 
#                         to_addrs="deibel_lukas@gmx.de", 
#                         msg="Subject:Happy Birthday\n\nThis is the message body")
#     connection.close()

import datetime as dt

now = dt.datetime.now()
year = now.year
weekday = now.weekday
