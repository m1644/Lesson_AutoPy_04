import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import yaml


with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    fromaddress = testdata["fromaddress"]
    toaddress = testdata["toaddress"]
    mypass = testdata["mypass"]

reportname = "./log.txt"

msg = MIMEMultipart()
msg["From"] = fromaddress
msg["To"] = toaddress
msg["Subject"] = "Отчет теста!"

with open(reportname, "rb") as f:
    part = MIMEApplication(f.read(), Name=basename(reportname))
    part['Content-Disposition'] = 'attachment; filename="%s"' % basename(reportname)
    msg.attach(part)

body = "Тест сайта test-stand.gb.ru"
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
server.login(fromaddress, mypass)
text = msg.as_string()
server.sendmail(fromaddress, toaddress, text)
server.quit()
