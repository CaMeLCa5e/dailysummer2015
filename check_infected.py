#! usr/bin/python 

"""Checks for sync requests during update"""

import os
import smtplib

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

log_file = "/var/log/rcs.log"
detected_file = "/var/log/detected"

def send_mail(line):
	content = "Infected machine \n%s" % line
	try:
		msg = MIMEMultipart()
		msg["Subject"] = "AV Monitor Results"
		msg["From"] = "email@email.com"
		body = MIMEText(content, 'txt')
		msg.attach(body)
		smtp = smtplib.SMTP("mail.email.com", 25)
		smtp.sendmail(msg["From"], msg["To"].split(","), msg.as_string())
		smtp.quit()
	except Exception as e:
		print "Impossible to send mail: %s" % e

def delete_logfile():
	pass

def stop():
	with open(detected_file, 'w') as f:
		f.write("")

def trigger(cont):
	send_mail(cont)
	delete_logfile()
	stop()

def main():
	if os.path.exists(detected_file):
		exit()
	print "not exited"
	if os.path.exists(log_file):
		with open(log_file, "r") as f:
			cont = f.read()
			if "RCS-SYNC" in cont:
				print "Infected machine detected"
				trigger(cont)

if __name__ == '__main__':
	main()
