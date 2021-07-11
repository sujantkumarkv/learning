MY_EMAIL = "yagamilight1362@gmail.com"
PASSWORD = "YAGAMIRAITOprince123#"

import pandas
import smtplib
import random
from datetime import datetime as dt

letter_file = "letter_templates/letter_.txt"

# 4. Send the letter generated in step 3 to that person's email address.
def send_mail(birthday_msg, mail_id):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        #starttls() - TRANSPORT LAYER SECURITY , protects the content of mail
        #like if someone intercepts mail in between,it wld be in encrypted form :)
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=mail_id,
            msg=f"Subject: Happy Birthday\n\n{birthday_msg}")

############################################################3
#             
# now= datetime.now()
today = (dt.now().day, dt.now().month)

# 2. Check if today matches a birthday in the birthdays.csv

data_read = pandas.read_csv("birthdays.csv")  # read data from csv file.
data = pandas.DataFrame(data_read)

# new_dict= {(day, month) for (day, month) in data.loc[]}
# data_dict= {
#     (dt.datetime.day, dt.datetime.month): (data.loc[0]["day"], data.loc[0]["month"])
# }
# THE ABOVE CODE HAS LIMITATION THAT WE NEED 2 SPECIFY ROW INDEX IN loc[index]; so can't iterate in python list/dict comprehension.
# birthdays_dict = {
#     (month, day): data_row
# }

birthdays_data = {(data_row["day"], data_row["month"]): data_row for ( _, data_row ) in data_read.iterrows()}
# index here isn't needed can be replaced by _
# WE RE-CREATED THE FORM GIVEN ABOVE as pandas.DataFrame.iterrows() iterates over DataFrame rows as (index, Series) pairs.

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name
# from birthdays.csv

# if (today_month, today_day) in birthdays_dict:
if today in birthdays_data:
    birthday_boy = birthdays_data[today]["name"]
    birthday_boy_mail = birthdays_data[today]["email"]
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter:
        # string.replace(oldvalue, newvalue, count)
        birthday_msg = letter.read().replace("[NAME]", birthday_boy)
        send_mail(birthday_msg=birthday_msg, mail_id=birthday_boy_mail)

############################################################################


