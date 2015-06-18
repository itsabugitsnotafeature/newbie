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


'''
Mail Parameters
'''
#Credentials_Incoming
gmail_user='<gmail_username>'
gmail_pwd='<gmail_password>'

#Credentials_Outgoing
outgoing_user='<outgoing_receiver>@gmail.com'

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

targetMonthNum = 7
targetYearNum = 2027

resultRegExpString = 'Result: ([A-Z])\w+, ([A-Z])\w+ ([0-9])*'
resultDateRegExpString = '([A-Z])\w+, ([A-Z])\w+ ([0-9])*'
monthReExpString = 'January|February|March|April|May|June|July|August|September|October|November|December'
yearReExpString = '2015|2016'
