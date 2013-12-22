wolverineGradeGraber
====================

This program can be used to grab grades from Wolverine Access, save it to your local disk, and send email notifications if there are changes.

### Installation
Some simple things you need to run: 
* python and its selenium library
* a gmail account
* a Firefox browser (for other browsers, some additional drivers are required. Will be supported in future releases)

Scripts for installing selenium are in `install.sh`, run it by `$ sh install.sh`

I'm always ready to help anyone who wants to try.

### Get it running

In command line: `python main.py UNIQNAME PW EMAIL_SENDER EMAIL_PW EMAIL_RECEIVER`
Replace the following parameters:
* `UNIQNAME` is your umich unique name
* `PW` is your umich password
* `EMAIL_SENDER` is gmail account name (It must be something@gmail.com currently)
* `EMAIL_PW` is gmail password
* `EMAIL_RECEIVER` is the receiver of the notification

For example, my wolverine username is `ethanjyx` and password is `jyxjyxjyx`(Hmm is this true?), I have a gmail account `johnestar.wag@gmail.com` and password `youknow` and I want to send notifications to my umich email `ethanjyx@umich.edu`, then the command line would be:
`python main.py ethanjyx jyxjyxjyx johnestar.wag@gmail.com youknow ethanjyx@umich.edu`

### How it works?
With the help of selenium, the program will grab the grades from Wolverine Access every 10 seconds. It saves current version of transcript and compares with previous versions. If there are changes, emails will be sent. 

`oldtranscript.txt` will always contain the latest transcript. Msg sent will simply be 'New grade has been posted!'

### Final words
Wish everybody great grades and Merry Christmas!...