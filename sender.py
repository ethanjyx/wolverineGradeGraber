import smtplib

class EmailSender:
	def __init__(self, username, password, target):
		self.server = smtplib.SMTP('smtp.gmail.com', 587)
		self.server.starttls()
		self.server.login(username, password)
		self.target = target
		return

	def sendNotification(self, msg):
		self.server.sendmail("you", self.target, msg)
		return