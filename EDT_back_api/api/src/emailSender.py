from email.message import EmailMessage
import smtplib

sender = "workepsi9@outlook.com"
#recipient = "testwork@yopmail.com"

def sendMailText(message, recipient):
    email = EmailMessage()
    email["From"] = sender
    email["To"] = recipient
    email["Subject"] = "Test Email"
    email.set_content(message)

    smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
    smtp.starttls()
    smtp.login(sender, "oCCR?HoR$NRFi6@Q")
    smtp.sendmail(sender, recipient, email.as_string())
    smtp.quit()