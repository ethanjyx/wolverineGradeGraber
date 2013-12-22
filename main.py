from selenium import webdriver
import time
import sys
import os
import filecmp
#import selenium.webdriver.support.ui as ui

browser = webdriver.Firefox()
browser.get('https://csprod.dsc.umich.edu/services/student')
#wait = ui.WebDriverWait(browser, 120) # time out after 10 seconds
browser.find_element_by_id('login').send_keys(sys.argv[1])
browser.find_element_by_id('password').send_keys(sys.argv[2])
browser.find_element_by_id('loginSubmit').click()
#wait.until(lambda driver: browser.find_elements_by_id('ptifrmtgtframe'))
browser.switch_to_frame('TargetContent')
browser.find_element_by_xpath("//a[@title='View an unofficial copy of your academic transcript.']").click()
#wait.until(lambda driver: browser.find_elements_by_id('ptifrmtgtframe'))
browser.switch_to_frame('TargetContent')
browser.find_element_by_id('GO').click()

#wait.until(lambda driver: browser.find_element_by_id('ptifrmtgtframe').find_element_by_id('M_SR_TSCRPT_HDR_MESSAGE_PARM1'))

time.sleep(10)

browser.switch_to_default_content()
browser.switch_to_frame('TargetContent')
#print browser.page_source.encode('utf-8')

results = browser.find_elements_by_xpath("//*[contains(@id, 'win0divDERIVED_TSCRPT_TSCRPT_COMP_DATA')]")

transcript = ''

for r in results:
    transcript += r.text + '\n'

f = open('transcript.txt', 'w')
f.write(transcript)
f.close()

if os.path.isfile('oldtranscript.txt'): # old transcript exists
	if not filecmp.cmp('transcript.txt', 'oldtranscript.txt'): # new grades have been entered
		#send_email()
		print ''
		os.system('rm oldtranscript.txt; mv transcript.txt oldtranscript.txt')
else: # old transcript does not exist, which means this is the first time running this script
	os.system('mv transcript.txt oldtranscript.txt; rm transcript.txt')

browser.quit()