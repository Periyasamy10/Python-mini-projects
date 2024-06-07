##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import pandas
import datetime as dt
import random
import smtplib

data = pandas.read_csv("birthdays.csv")

now = dt.datetime.now()

greeting_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

for index, row in data.iterrows():
    if now.month == row["month"] and now.day == row["day"]:
        letter_random = random.choice(greeting_list)
        letter = "letter_templates/" + letter_random
        PLACEHOLDER = "[NAME]"
        with open(letter) as file:
            file_data = file.read()
            new_letter = file_data.replace(PLACEHOLDER,row["name"])
            my_mail = "r.periyasamy097@gmail.com"
            password = "yqzsdgcyzojuyetc"
            receiver_mail = row["email"]
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_mail,password=password)
                connection.sendmail(from_addr=my_mail,
                                    to_addrs=receiver_mail,
                                    msg=f"Subject:Birthday Greeting\n\n{new_letter}")

