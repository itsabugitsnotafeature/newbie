import poplib

'''
# Directory Location(s)
'''
downloadFolderName = 'seek_'
emailFolderName =  'ScanHistory'
destinationDirectory = ''
logFileName = 'log/IrmaAlert.log'


'''
# Global Parameters
'''
emailCounter = 0
scanIntervalSeconds = 10
commandTimeOut = 1000
triggerServiceFlag = False

enableScannerFlag = False
activateServiceString = 'riddle'
terminateScannerString = 'disasastrophe'

commandToExecute = "mvn --version "
commandConsoleLog = ''


'''
Mail Parameters
'''
#Credentials_Incoming
gmail_user=''
gmail_pwd=''

#Credentials_Outgoing
outgoing_user='@gmail.com'

pop_conn = poplib.POP3_SSL('pop.gmail.com')
pop_conn.user('recent:'+gmail_user)
pop_conn.pass_(gmail_pwd)

#Payload
replySubject = "Here you go dear !"
replyBody = commandConsoleLog

acknowledgementSubject = "Master Acknowledgement !"
acknowledgementBody = 'Ack Message : Ping received successfully'

invalidQuerySubject = "Look what you did !"
invalidQueryBody = " Sweetie, \nI don't yet have the smarts deal with the twisted ass date you" \
                   " sent. Better luck next time ! \n\nXoXo \nAunt Irma"

unExpectedConditionSubject = "Oops ! Something Unexpected happened"
unExpectedConditionBody = " I'm Sorry Honey, \nSomething bad just happened, and I happen to be a dumb program.\n" \
                            " Can you please ask nicely one more time. Ignore my prior email. \n" \
                            " Basically, just dumb it down for me babe. \n\nXoXo \nAunt Irma"


attachmentsAck = []


'''
IRMA Service API Parameters
'''
# url = 'http://www.timeanddate.com/date/dateadded.html?m1=12&d1=22&y1=2015&type=add&ay=&am=&aw=&ad=26e'
diffBetweenEachVisit = 26

firstStartDate   = 28
firstStartMonth  = 5
firstStartYear   = 2015

targetMonthNum = 6
targetYearNum = 2015

resultRegExpString = 'Result: ([A-Z])\w+, ([A-Z])\w+ ([0-9])*'
resultDateRegExpString = '([A-Z])\w+, ([A-Z])\w+ ([0-9])*'
# monthRegExString = 'January|February|March|April|May|June|July|August|September|October|November|December'
monthRegExString = 'jan[A-Z]*|feb[A-Z]*|mar[A-Z]*|apr[A-Z]*|may|jun[A-Z]*|jul[A-Z]*|aug[A-Z]*|sep[A-Z]*|oct[A-Z]*|nov[A-Z]*|dec[A-Z]*'
yearRegExString = '20[0-9][0-9]'
emailIdRegExString = '\w+@[\w.-]+|\{(?:\w+, *)+\w+\}@[\w.-]+'

