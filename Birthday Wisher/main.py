# import smtplib
#
# my_email = "r.periyasamy097@gmail.com"
# password = "nprbjciblezkyeeg"
#
# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email,password=password)
# connection.sendmail(from_addr=my_email,to_addrs="periyasamy.r@yahoo.com",msg="Subject:Birthday whishes \n\nHappy Birthday"
#                                                                              "")
# connection.close()

import pandas
import random
import datetime as dt
import smtplib

data = pandas.read_table("quotes.txt")
list_quotes = data.values.tolist()
quotes = random.choice(list_quotes)

now = dt.datetime.now()
day = now.weekday()

my_email = "r.periyasamy097@gmail.com"
password = "nprbjciblezkyeeg"

if day == 2:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs="periyasamy.r@yahoo.com",msg=f"Subject:Monday motivation\n\n{quotes}")


