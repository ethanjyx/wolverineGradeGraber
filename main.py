from sender import EmailSender
from graber import GradeGraber
import time
import sys
import os
import filecmp

curTranscript = 'transcript.txt'
oldTranscript = 'oldtranscript.txt'

while True:
	graber = GradeGraber()
	graber.grab(sys.argv[1], sys.argv[2], curTranscript)

	if os.path.isfile(oldTranscript): # old transcript exists
		if not filecmp.cmp(curTranscript, oldTranscript): # new grades have been entered
			msg = 'New grade has been posted!'
			print msg
			emailSender = EmailSender(sys.argv[3], sys.argv[4], sys.argv[5])
			emailSender.sendNotification(msg)
			os.system('rm oldtranscript.txt; mv transcript.txt oldtranscript.txt')
	else: # old transcript does not exist, which means this is the first time running this script
		os.system('mv transcript.txt oldtranscript.txt')

	time.sleep(10)