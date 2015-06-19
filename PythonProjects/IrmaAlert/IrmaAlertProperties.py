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
activateServiceString = 'riddle-me-this!'
terminateScannerString = 'bhai-tu-bass-kar'

commandToExecute = "mvn --version "
commandConsoleLog = ''

# kkkk - ho gaya
'''
Mail Parameters
'''
#Credentials_Incoming
gmail_user='<user>'
gmail_pwd='<pass>'

#Credentials_Outgoing
outgoing_user='<user>@gmail.com'

pop_conn = poplib.POP3_SSL('pop.gmail.com')
pop_conn.user('recent:'+gmail_user)
pop_conn.pass_(gmail_pwd)

#Payload
replySubject = "Here you go dear !"
replyBody = commandConsoleLog

acknowledgementSubject = "Master Acknowledgement !"
acknowledgementBody = 'Ack Message : Ping received successfully'
attachmentsAck = []


'''
IRMA Service API Parameters
'''
# url = 'http://www.timeanddate.com/date/dateadded.html?m1=12&d1=22&y1=2015&type=add&ay=&am=&aw=&ad=26e'
diffBetweenEachVisit = 26

firstStartDate   = 28
firstStartMonth  = 5
firstStartYear   = 2015

targetMonthNum = 9
targetYearNum = 2022

resultRegExpString = 'Result: ([A-Z])\w+, ([A-Z])\w+ ([0-9])*'
resultDateRegExpString = '([A-Z])\w+, ([A-Z])\w+ ([0-9])*'
# monthRegExString = 'January|February|March|April|May|June|July|August|September|October|November|December'
monthRegExString = 'jan[A-Z]*|feb[A-Z]*|mar[A-Z]*|apr[A-Z]*|may|jun[A-Z]*|jul[A-Z]*|aug[A-Z]*|sep[A-Z]*|oct[A-Z]*|nov[A-Z]*|dec[A-Z]*'
yearRegExString = '20[0-9][0-9]'


