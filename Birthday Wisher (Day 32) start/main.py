import smtplib
import datetime as dt
import random

MY_EMAIL = "prayaspatel199@gmail.com"
MY_PASSWORD = ""

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 2:
    with open(file="quotes.txt") as data:
        quotes = data.readlines()
        quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="prayaspatel199@gmail.com", msg=f"quote\n{quote}")

