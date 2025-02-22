import smtplib
from account import *
from email.message import EmailMessage
import random

nicknames = ["유재석", "박명수", "정형돈", "정형돈", "조세호"]

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    for nickname in nicknames:
        msg = EmailMessage()
        msg["Subject"] = "파이썬 특강 신청합니다."
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = EMAIL_ADDRESS

        content = "/".join(nickname, str(random.randint(1000, 9999)))
        msg.set_content(content)
        smtp.send_message(msg)
        print(nickname + "님이 메일 발송 완료")
