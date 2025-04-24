import datetime as dt
import random
import smtplib
my_email = "Your email ID"
password= "Your password"
x = dt.datetime.now()


if x.weekday() == 5:# Suppose today was saturday so it weekday num is 5
    with open("quotes.txt") as quotes:
        contents = quotes.readlines()
        quote = random.choice(contents)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs="tarunmishra12122002@gmail.com"
                            ,msg=f"Subject:best_wishes\n\n{quote}")




