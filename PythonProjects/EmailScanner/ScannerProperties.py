import poplib

'''
# Directory Location(s)
'''
downloadFolderName = 'seek_'
emailFolderName =  'ScanHistory'
destinationDirectory = ''
logFileName = 'log/Scanner.log'


'''
# Global Parameters
'''
emailCounter = 0
scanIntervalSeconds = 10
commandTimeOut = 1000
triggerServiceFlag = False
enableScannerFlag = False
activateServiceString = 'ACTIVATE_ERMA_VISIT'
terminateScannerString = 'TERMINATE_ERMA_VISIT'

commandToExecute = "mvn --version "
commandConsoleLog = ''


'''
Mail Parameters
'''
#Credentials_Incoming
gmail_user='whenisirmavisiting'
gmail_pwd='whenishightide'

#Credentials_Outgoing
outgoing_user='whenisirmavisiting@gmail.com'

pop_conn = poplib.POP3_SSL('pop.gmail.com')
pop_conn.user('recent:'+gmail_user)
pop_conn.pass_(gmail_pwd)

#Payload
replySubject = "Here you go dear !"
replyBody = commandConsoleLog

acknowledgementSubject = "Master Acknowledgement !"
acknowledgementBody = 'Ack Message : Ping received successfully'
attachmentsAck = []
