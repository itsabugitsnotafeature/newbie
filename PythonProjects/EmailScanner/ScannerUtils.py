__author__ = 'ununoctium'


import ScannerUtils
import ScannerProperties
import smtplib
import os
import poplib
import time
import re
import fileinput

from email import parser
from subprocess import call
import logging
import sys
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import email, getpass, imaplib, os
import commands
import commandWorker

'''
Mail Parameters
'''
pop_conn = poplib.POP3_SSL('pop.gmail.com')
pop_conn.user('recent:'+ScannerProperties.gmail_user)
pop_conn.pass_(ScannerProperties.gmail_pwd)



'''
Method to fetch all messages from inbox
'''
def getEmail():

    #Get messages from server:
    logging.debug('Fetching messages from inbox.')
    messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]

    # Concat message pieces:
    logging.debug('Concatinating all messages')
    messages = ["\n".join(mssg[1]) for mssg in messages]

    #Parse message into an email object:
    messages = [parser.Parser().parsestr(mssg) for mssg in messages]

    # save each messages
    logging.debug('Starting to save each message.')
    for message in messages:
        saveMessage(message)

    logging.debug('Done receiving messages. Quitting method call.')
    pop_conn.quit()



'''
Method to setup environment
Variables : Initializing Logger, Working Directory, Base Directory, emailCounter initialization
'''
def setup():


    setupLogger();
    logging.debug('Initializing working directory and other environment varaibles.')

    timeStamp = getTimeStamp()
    ScannerProperties.destinationDirectory = os.path.join(os.path.realpath(ScannerProperties.emailFolderName),
                                                     (ScannerProperties.downloadFolderName + str(timeStamp)) )

    emailCounter = 1
    # Check if Destination directory exists : Else make one
    if not os.path.exists(ScannerProperties.destinationDirectory):
        os.makedirs(ScannerProperties.destinationDirectory)

    logging.debug('Done with setup().')



'''
Method to setup 'logger'
'''
def setupLogger():

    if ( os.path.isfile(ScannerProperties.logFileName) is True ):
         print "*****************************************************"
         print "*****************************************************"
         print "OLD log file found. Renaming with current timestamp."

         newFileName = ScannerProperties.logFileName[:16] + str(getTimeStamp()) + ".txt"
         os.rename( ScannerProperties.logFileName, newFileName )

         # print "Renamed and saved at :" + newFileName
         with open(ScannerProperties.logFileName, 'w') as fout:
             fout.write('')
             fout.close()

    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',
                        filename=ScannerProperties.logFileName,
                        level=logging.DEBUG )
    # define a Handler which writes INFO messages or higher to the sys.stderr
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    # set a format which is simpler for console use
    formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
    # tell the handler to use this format
    console.setFormatter(formatter)
    # add the handler to the root logger
    logging.getLogger('').addHandler(console)
    # Now, we can log to the root logger, or any other logger. First the root...

    logging.debug('Logger setup successful.')



'''
Method to save each email 'message' along with
its attachments.
'''
def saveMessage(message):

    emailSubject = str(message['subject'])

    logging.debug('Saving email message.')
    # logging.debug('[Email_Subject]: ' + emailSubject )

    baseEmailFileNameFileName = os.path.join(ScannerProperties.destinationDirectory, emailSubject[:14])
    eachFileName = baseEmailFileNameFileName + str(ScannerProperties.emailCounter) + ".txt"

    if ScannerProperties.activateServiceString in emailSubject:
        logging.debug(' ++ Trigger for Service activation received successfully. ++ ')
        setTriggerServiceFlag()




    if ScannerProperties.terminateScannerString in emailSubject:
        logging.debug(' ### TERMINATE SCANNER CODE RECEIVED #### ')
        resetEmailScannerFlag()
        logging.debug('Termination flag set to: ' + str(ScannerProperties.enableScannerFlag) )

    ## Save Email in file
    messageFile = open(eachFileName, 'wb')
    messageFile.write(str(message))
    messageFile.close()
    increment_emailCounter_by_one()

    logging.debug('Email saved.')
    logging.debug('Looking for attachments.')

    for part in message.walk():
        if part.get('Content-Disposition') is None:
            logging.debug('No attachments found.')
            continue

        logging.debug('Attachments found.')
        attachmentFilename = part.get_filename()
        counter = 1

        # if there is no filename, we create one with a counter to avoid duplicates
        if not attachmentFilename:
            attachmentFilename = 'part-%03d%s' % (counter, 'bin')
            counter += 1

        logging.debug("Attachment found. Saving file:" + attachmentFilename)

        attachmentPath = os.path.join(ScannerProperties.destinationDirectory, attachmentFilename)
        #Check if its already there
        if not os.path.isfile(attachmentFilename) :
            # finally write the stuff
            fp = open(attachmentPath, 'wb')
            fp.write(part.get_payload(decode=True))
        logging.debug('Done saving attachment.')
    logging.debug('Done saving message !')



'''
Method to increment Global Email Counter
'''
def increment_emailCounter_by_one():
    # global emailCounter

    logging.debug('Incrementing global email counter')
    ScannerProperties.emailCounter += 1
    logging.debug('New Value:' + str(ScannerProperties.emailCounter) )



'''
Method to start User Service
'''
def startService():

    logging.debug("Starting Service!")

    sendEmailReply(ScannerProperties.acknowledgementSubject,
                    ScannerProperties.acknowledgementBody,
                    ScannerProperties.attachmentsAck)

    # Method to setup okc parameters
    # setupOkcPropertyFile()

    logging.debug("Starting Service.")
    executeCommand(ScannerProperties.commandToExecute)

    logging.debug("\n Python : Done executing Service, replying back with report.")
    sendEmailReply( ScannerProperties.replySubject,
                    ScannerProperties.commandConsoleLog,
                    ScannerProperties.attachmentsAck)

    resetTriggerServiceFlag()








def executeCommand(commandToExecute):
    from subprocess import Popen

    logging.debug("######################################################")
    logging.debug("########         HERE    WE  GO             ##########")
    logging.debug("######################################################")



    logging.debug("Executing Command ::" + commandToExecute)

    commandWorkerObject = commandWorker.Command(commandToExecute)

    commandWorkerObject.run( getCommandTimeOutPeriod() )

    logging.debug("Command execution COMPLETED !")
    return




'''
Replaces the line containing 'searchExp'
    with 'replaceExp' in a given file
'''
def replaceAll(filePath,searchExp,replaceExp):
    for line in fileinput.input(filePath, inplace=1):
        if searchExp in line:
            line = line.replace(line,replaceExp)
            line += "\n"
        sys.stdout.write(line)



'''
Returns False : If email Scanner Diabled
        True : If email Scanner Enabled
'''
def isEmailScannerEnabled():
    return ( ScannerProperties.enableScannerFlag )



'''
Returns False : If Service Flag is Diabled
        True : If Service Flag is Enabled
'''
def getServiceFlagStatus():
    return ( ScannerProperties.triggerServiceFlag )


'''
Returns Time out period for each command
'''
def getCommandTimeOutPeriod():
    return ( ScannerProperties.commandTimeOut )


'''
Returns seconds to sleep
'''
def getSleepTimeInterval():
    return ( ScannerProperties.scanIntervalSeconds )


'''
Adds sleep Cycle
'''
def addSleep(seconds):
    time.sleep( seconds )



'''
Disable Email Scanner Flag
'''
def resetEmailScannerFlag():
    ScannerProperties.enableScannerFlag = False
    logging.debug("Email Scanner flag DISABLED. ")



'''
Enable Email Scanner Flag
'''
def setEmailScannerFlag():
    ScannerProperties.enableScannerFlag = True
    logging.debug("Email Scanner flag ENABLED. ")




'''
Enable Service Trigger Flag
'''
def setTriggerServiceFlag():
    ScannerProperties.triggerServiceFlag = True
    logging.debug("Service trigger flag ENABLED. ")


'''
Disable Service Trigger Flag
'''
def resetTriggerServiceFlag():
    ScannerProperties.triggerServiceFlag = False
    logging.debug("Service trigger flag Disabled. ")


'''
Method to send Email Response
'''
def sendEmailReply(emailSubject,emailBody,attachments):
    logging.debug("Sending email.")

    gmail_user_email = ScannerProperties.gmail_user+"@gmail.com"
    emailMessage = MIMEMultipart()
    emailMessage['Subject'] = emailSubject
    emailMessage['From'] = gmail_user_email
    emailMessage['To'] = ScannerProperties.outgoing_user

    # That is what u see if dont have an email reader:
    emailMessage.preamble = 'Multipart massage.\n'

    # This is the textual part:
    part = MIMEText(emailBody)
    emailMessage.attach(part)

    # This is the attachment part :
    for eachAttachment in attachments:
        eachAttachment = os.path.join('', eachAttachment)

        part = MIMEApplication(open(eachAttachment,"rb").read())
        part.add_header('Content-Disposition', 'eachAttachment', filename=eachAttachment)
        emailMessage.attach(part)


    # Send the email
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
        server.ehlo()
        server.starttls()
        server.login(gmail_user_email, ScannerProperties.gmail_pwd)
        server.sendmail(emailMessage['From'], emailMessage['To'], emailMessage.as_string())
        server.close()
        logging.debug('Successfully sent the mail.')
    except:
        logging.debug('Failed to send mail !!')

    logging.debug('Done sending email.')



def getGmailViaImap():

    logging.debug('Fetching messages from gmail inbox.')

    # connecting to the gmail imap server
    m = imaplib.IMAP4_SSL("imap.gmail.com")

    logging.debug('Logging in.')
    m.login(ScannerProperties.gmail_user,ScannerProperties.gmail_pwd)
    m.select("[Gmail]/All Mail") # here you a can choose a mail box like INBOX instead


    logging.debug('Mail downloaded, seperating unseen messages.')
    resp, items = m.search(None, "UNSEEN")
    items = items[0].split() # getting the mails id

    if not items :
        logging.debug("* No New Messages : Returning to caller ! *")
        return

    logging.debug('New Unseen messages detected.')
    for emailid in items:
        logging.debug('Saving one email with following credentials.')

        resp, data = m.fetch(emailid, "(RFC822)") # fetching the mail, "`(RFC822)`" means "get the whole stuff", but you can ask for headers only, etc
        email_body = data[0][1] # getting the mail content
        mail = email.message_from_string(email_body) # parsing the mail content to get a mail object

        logging.debug('[From:]' + mail["From"] )
        logging.debug('[Subject:]' + mail["Subject"] )
        saveMessage(mail)



def getTimeStamp():
    return int(time.time())





