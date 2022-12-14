import smtplib
import pandas
import random
import datetime as dt

MY_EMAIL = "prayaspatel199@gmail.com"
MY_PASS = "***** "

data = pandas.read_csv("birthdays.csv")
birthdays_dictionary = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}


now = dt.datetime.now()
current_day = now.day
current_month: = now.month
today_tuple = (current_month, current_day)


if today_tuple in birthdays_dictionary:
    birthday_person = birthdays_dictionary[today_tuple]

    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter:
        new_letter = letter.read()
        final_letter = new_letter.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.@gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASS)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Wishing Happy Bday \n {final_letter}"
                            )