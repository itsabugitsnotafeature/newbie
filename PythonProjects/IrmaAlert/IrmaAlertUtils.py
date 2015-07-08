import base64

__author__ = 'ununoctium'



import IrmaAlertProperties
import smtplib
import poplib
import time
import fileinput
import requests
import re
import logging
import sys
import email, imaplib, os



from email import parser
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

receivedMonthChar = ''
daysSinceFirstFlow = ''

queryMonthNum = ''
queryYearNum = ''

queenBeeEmail = ''

'''
Mail Parameters
'''
pop_conn = poplib.POP3_SSL('pop.gmail.com')
pop_conn.user('recent:'+IrmaAlertProperties.gmail_user)
pop_conn.pass_(IrmaAlertProperties.gmail_pwd)



'''
Getter for queryMonthNum
'''
def getQueryMonthNum():
    global queryMonthNum
    return queryMonthNum


'''
Setter for queryMonthNum
'''
def setQueryMonthNum(thisMonth):
    global queryMonthNum
    queryMonthNum = thisMonth
    logging.debug("Successfylly set query MONTH to Integer Value :" + str(thisMonth) )
    return


'''
Setter for queryYearNum
'''
def setQueryYearNum(thisYear):
    global queryYearNum
    queryYearNum = thisYear
    logging.debug("Successfylly set query YEAR to Integer Value :" + str(thisYear) )
    return



'''
Getter  for queryYearNum
'''
def getQueryYearNum():
    global queryYearNum
    return queryYearNum



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
    global daysSinceFirstFlow
    global queryMonthNum
    global queryYearNum


    setupLogger();
    logging.debug('Initializing working directory and other environment varaibles.')

    timeStamp = getTimeStamp()
    IrmaAlertProperties.destinationDirectory = os.path.join(os.path.realpath(IrmaAlertProperties.emailFolderName),
                                                     (IrmaAlertProperties.downloadFolderName + str(timeStamp)) )

    emailCounter = 1
    # Check if Destination directory exists : Else make one
    if not os.path.exists(IrmaAlertProperties.destinationDirectory):
        os.makedirs(IrmaAlertProperties.destinationDirectory)


    queryMonthNum = IrmaAlertProperties.targetMonthNum
    queryYearNum = IrmaAlertProperties.targetYearNum
    daysSinceFirstFlow = calculateDaysSinceFirstFlow()
    setQueenBeeEmail( IrmaAlertProperties.outgoing_user )

    logging.debug('Done with setup().')




'''
Method to setup 'logger'
'''
def setupLogger():

    if ( os.path.isfile(IrmaAlertProperties.logFileName) is True ):
         print "*****************************************************"
         print "*****************************************************"
         print "OLD log file found. Renaming with current timestamp."

         newFileName = IrmaAlertProperties.logFileName[:16] + str(getTimeStamp()) + ".txt"
         os.rename( IrmaAlertProperties.logFileName, newFileName )

         # print "Renamed and saved at :" + newFileName
         with open(IrmaAlertProperties.logFileName, 'w') as fout:
             fout.write('')
             fout.close()

    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',
                        filename=IrmaAlertProperties.logFileName,
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


def replyToUser(status):
    if status.lower().__contains__("unexpected"):
        sendEmailReply( IrmaAlertProperties.unExpectedConditionSubject,
                        IrmaAlertProperties.unExpectedConditionBody,
                        IrmaAlertProperties.emailAttachments
                        )
        return




def saveMessage(message):

    emailSubject = str(message['subject'])
    logging.debug('Saving email message.' )

    baseEmailFileNameFileName = os.path.join(IrmaAlertProperties.destinationDirectory, emailSubject[:14])
    eachFileName = baseEmailFileNameFileName + str(IrmaAlertProperties.emailCounter) + ".txt"

    # Trigger to Terminate Scanner
    # if ( IrmaAlertProperties.terminateScannerString in emailSubject ):
    if ( IrmaAlertProperties.terminateScannerString in emailSubject.lower() ):
        terminateScanner()


    ## Save Email in file
    messageFile = open(eachFileName, 'wb')
    messageFile.write(str(message))
    messageFile.close()
    increment_emailCounter_by_one()

    logging.debug('Email saved.')
    logging.debug('Looking for attachments.')

    for part in message.walk():

        encodingType = message['Content-Transfer-Encoding']

        if part.get_content_type() == 'text/plain':
            logging.debug( "Saving body content." )
            #
            # If sender address contain outlook or hotmail.
            # if (    (str(getQueenBeeEmail()).lower().__contains__("outlook") )
            #         or
            #         ( str(getQueenBeeEmail()).lower().__contains__("hotmail") )
            #         or
            #         ( str(getQueenBeeEmail()).lower().__contains__("yahoo") )
            #     ):
            #     emailBodyContent = base64.b64decode( part.get_payload() )
            if str(encodingType).__contains__("base64"):
                emailBodyContent = base64.b64decode( part.get_payload() )

            else:
                emailBodyContent = part.get_payload()

            # Trigger to start service : Email Subject contains know string
            if ( IrmaAlertProperties.activateServiceString in emailSubject.lower() ):
                logging.debug(' ++ Trigger for Service activation received successfully. ++ ')

                extractedMonth = extractRegExIgnoreCase(IrmaAlertProperties.monthRegExString, emailBodyContent)
                if extractedMonth is None:
                    logging.error("Unable to read Month from sender's email content.");
                    replyToUser("unExpectedCondition");
                    return

                logging.debug("Extracted Month : " + extractedMonth)
                setQueryMonthNum( getMonthNum(extractedMonth) )

                # extractedYear = re.search(IrmaAlertProperties.yearRegExString, emailBodyContent).group(0)
                extractedYear = extractRegEx(IrmaAlertProperties.yearRegExString, emailBodyContent)
                if extractedYear is None:
                    logging.error("Unable to read Year from sender's email content.");
                    replyToUser("unExpectedCondition");
                    return


                logging.debug("Extracted Year : " + extractedYear)
                setQueryYearNum( int(extractedYear) )
                setTriggerServiceFlag()



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

        attachmentPath = os.path.join(IrmaAlertProperties.destinationDirectory, attachmentFilename)
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
    IrmaAlertProperties.emailCounter += 1
    logging.debug('New Value:' + str(IrmaAlertProperties.emailCounter) )



'''
Method to start User Service
'''


def notifyUser(appendedMessage):
    sendEmailReply( IrmaAlertProperties.notificationSubject,
                    IrmaAlertProperties.notificationBody + appendedMessage ,
                    []
                    )


def startService():
    global daysSinceFirstFlow


    appendedMessage = "\n QueryMonthNum " + str(getQueryMonthNum()) + \
                      " \n QueryYearNum : " + str(getQueryYearNum()) + "\n\n";
    notifyUser(appendedMessage);


    daysSinceFirstFlow = calculateDaysSinceFirstFlow()

    if daysSinceFirstFlow == -1:
        logging.debug("Invalid request caught. Returning to main().")
        resetTriggerServiceFlag()
        return

    logging.debug("Starting Service!")
    logging.debug("Days since first flow : " + str(daysSinceFirstFlow) )


    
    visitDate = getIrmaVisits(daysSinceFirstFlow)

    fetchedWisdom = getNewWisdom()
    emailBody = visitDate + "\n\n" + "But remember, " + fetchedWisdom +  "\n\nXoXo \nAunt Irma" + ". "

    logging.debug("\n Python : Done executing Service, replying back with report.")

    sendEmailReply( IrmaAlertProperties.replySubject,
                    emailBody,
                    IrmaAlertProperties.emailAttachments)

    resetTriggerServiceFlag()




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
    return ( IrmaAlertProperties.enableScannerFlag )



'''
Returns False : If Service Flag is Diabled
        True : If Service Flag is Enabled
'''
def getServiceFlagStatus():
    return ( IrmaAlertProperties.triggerServiceFlag )


'''
Returns Time out period for each command
'''
def getCommandTimeOutPeriod():
    return ( IrmaAlertProperties.commandTimeOut )


'''
Returns seconds to sleep
'''
def getSleepTimeInterval():
    return ( IrmaAlertProperties.scanIntervalSeconds )


'''
Adds sleep Cycle
'''
def addSleep(seconds):
    time.sleep( seconds )



'''
Disable Email Scanner Flag
'''
def terminateScanner():
    logging.debug(' ### TERMINATE SCANNER CODE RECEIVED #### ')
    sendEmailReply(IrmaAlertProperties.terminationSubject,
                   IrmaAlertProperties.terminationBody,
                   IrmaAlertProperties.emailAttachments)

    resetEmailScannerFlag()
    logging.debug('Termination flag set to: ' + str(IrmaAlertProperties.enableScannerFlag) )
    return



'''
Disable Email Scanner Flag
'''
def resetEmailScannerFlag():
    IrmaAlertProperties.enableScannerFlag = False
    logging.debug("Email Scanner flag DISABLED. ")



'''
Enable Email Scanner Flag
'''
def setEmailScannerFlag():
    IrmaAlertProperties.enableScannerFlag = True
    logging.debug("Email Scanner flag ENABLED. ")




'''
Enable Service Trigger Flag
'''
def setTriggerServiceFlag():
    IrmaAlertProperties.triggerServiceFlag = True
    logging.debug("Service trigger flag ENABLED. ")


'''
Disable Service Trigger Flag
'''
def resetTriggerServiceFlag():
    IrmaAlertProperties.triggerServiceFlag = False
    logging.debug("Service trigger flag Disabled. ")


'''
Method to send Email Response
'''
def sendEmailReply(emailSubject,emailBody,attachments):
    logging.debug("Sending email to user.")

    gmail_user_email = IrmaAlertProperties.gmail_user+"@gmail.com"
    emailMessage = MIMEMultipart()
    emailMessage['Subject'] = emailSubject
    emailMessage['From'] = gmail_user_email
    # emailMessage['To'] = IrmaAlertProperties.outgoing_user
    if emailSubject == IrmaAlertProperties.notificationSubject :
        emailMessage['To'] = IrmaAlertProperties.notifying_user
    else :
        emailMessage['To'] = getQueenBeeEmail()

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
        server.login(gmail_user_email, IrmaAlertProperties.gmail_pwd)
        server.sendmail(emailMessage['From'], emailMessage['To'], emailMessage.as_string())
        server.close()
        logging.debug('Successfully sent the mail.')
    except:
        logging.debug('Failed to send mail !!')

    logging.debug('Done sending email.')


'''
Method to receive mail from user-defined GMAIL Accunt
'''
def getGmailViaImap():

    logging.debug('Fetching messages from gmail inbox.')

    # connecting to the gmail imap server
    m = imaplib.IMAP4_SSL("imap.gmail.com")

    logging.debug('Logging in.')
    m.login(IrmaAlertProperties.gmail_user,IrmaAlertProperties.gmail_pwd)
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

        logging.debug('From: ' + mail["From"] )

        sendersEmail = str(mail["From"])
        # sendersEmail = re.search(IrmaAlertProperties.emailIdRegExString, sendersEmail,re.IGNORECASE).group(0)
        sendersEmail = extractRegExIgnoreCase(IrmaAlertProperties.emailIdRegExString, sendersEmail)
        setQueenBeeEmail(sendersEmail)

        logging.debug('Subject: ' + mail["Subject"] )
        saveMessage(mail)


'''
Method to get Linux-epoc timeStamp
'''
def getTimeStamp():
    return int(time.time())


'''
Method that returns the penultimate day for
Aunt Irma's visit.
'''


def validateResults(resultString):
    global receivedMonthChar
    global daysSinceFirstFlow
    global queryMonthNum

    if ( getExpectedMonthChar(queryMonthNum) == receivedMonthChar ):
        logging.debug("ValidateResult: Correct result obtained")
        return resultString

    else :
        logging.debug("\n ***** ValidateResult: Error correcting results. ***** ")


        while ( getExpectedMonthChar(queryMonthNum) != receivedMonthChar ):
            logging.debug("ValidateResult: Result for revised daysSinceFirstFlow ["+ str(daysSinceFirstFlow) +"] is =>" + resultString)
            daysSinceFirstFlow +=IrmaAlertProperties.diffBetweenEachVisit
            resultString = getIrmaVisits(daysSinceFirstFlow)

        return  resultString


def calculateDaysSinceFirstFlow():
    MONTHS_PER_YEAR = 12
    global queryYearNum

    if (not checkValidRequesst()):
        logging.error("Invalid query request. Sending a slap on the wrist !")
        # sys.exit()
        sendEmailReply( IrmaAlertProperties.invalidQuerySubject,
                        IrmaAlertProperties.invalidQueryBody,
                        IrmaAlertProperties.emailAttachments
                        )
        return -1



    #     Send Email Saing invalid date


    if ( queryYearNum == 2015 ):
        daysSinceFirstFlow = IrmaAlertProperties.diffBetweenEachVisit * \
                 ( queryMonthNum -
                   IrmaAlertProperties.firstStartMonth
                   )
        logging.info('Total delta calculated [Year 2015]: ' + str(daysSinceFirstFlow) )

    else:
        multiplier = queryYearNum - IrmaAlertProperties.firstStartYear

        daysSinceFirstFlow = (
            IrmaAlertProperties.diffBetweenEachVisit * \
                (
                    ( MONTHS_PER_YEAR * multiplier ) +
                        (
                            queryMonthNum -
                            IrmaAlertProperties.firstStartMonth + 1
                        )
                )
        )

    if ( daysSinceFirstFlow < 0 ):
        logging.error("*****  DOOOODE : Look into this. Value for daysSinceFirstFlow is "
                      "Negative. \nCalculated value : " + str(daysSinceFirstFlow) + " ***** ")
        replyToUser("unExpectedCondition");
        return -1

    return daysSinceFirstFlow


def getAbsoluteFirstData():
    dd = str( IrmaAlertProperties.firstStartDate )
    mm = str(  IrmaAlertProperties.firstStartMonth )
    yy = str( IrmaAlertProperties.firstStartYear )

    return " " + dd + "/" + mm + "/" + yy + " "


def checkValidRequesst():
    global queryMonthNum
    global queryYearNum


    if (
        (queryMonthNum <= IrmaAlertProperties.firstStartMonth and queryYearNum == 2015)
            or
        ( queryYearNum < 2015)
    ):

        logging.error(' Cant go to time before ' + \
              getAbsoluteFirstData() + '. \nBreaks ' \
              'my <3logic<3 to say this Princess. \nSorry ! ')
        status = False
    else:
        logging.debug("Request found to be Valid. \nGood Girl !")
        status = True

    return status



def getIrmaVisits(daysSinceFirstFlow):
    global receivedMonthChar
    global queryYearNum

    getUrl = constructGetUrl(IrmaAlertProperties.firstStartMonth,
                             IrmaAlertProperties.firstStartDate,
                             IrmaAlertProperties.firstStartYear,
                             daysSinceFirstFlow)
    logging.info("getURL Value: "+ getUrl)


    getNextUrl = constructGetUrl(IrmaAlertProperties.firstStartMonth,
                                 IrmaAlertProperties.firstStartDate,
                                 IrmaAlertProperties.firstStartYear,
                                 daysSinceFirstFlow + IrmaAlertProperties.diffBetweenEachVisit)
    logging.info("getNextUrl Value: "+ getNextUrl)


    getCallReply = makeGetCall(getUrl)
    # receivedDate = re.search(IrmaAlertProperties.resultRegExpString, getCallReply).group(0)
    receivedDate = extractRegEx(IrmaAlertProperties.resultRegExpString, getCallReply)

    # receivedDate = re.search(IrmaAlertProperties.resultDateRegExpString, receivedDate).group(0)
    receivedDate = extractRegEx(IrmaAlertProperties.resultDateRegExpString,receivedDate)

    # receivedMonthChar = re.search(IrmaAlertProperties.monthRegExString, receivedDate,re.IGNORECASE).group(0)
    receivedMonthChar = extractRegExIgnoreCase(IrmaAlertProperties.monthRegExString, receivedDate)

    getCallReply = makeGetCall(getNextUrl)
    # nextReceivedDate = re.search(IrmaAlertProperties.resultRegExpString, getCallReply).group(0)
    nextReceivedDate = extractRegEx(IrmaAlertProperties.resultRegExpString, getCallReply)

    # nextReceivedDate = re.search(IrmaAlertProperties.resultDateRegExpString, nextReceivedDate).group(0)
    nextReceivedDate = extractRegEx(IrmaAlertProperties.resultDateRegExpString, nextReceivedDate)

    # nextReceivedMonthChar = re.search(IrmaAlertProperties.monthRegExString, nextReceivedDate,re.IGNORECASE).group(0)
    nextReceivedMonthChar = extractRegExIgnoreCase(IrmaAlertProperties.monthRegExString, nextReceivedDate)


    if (receivedMonthChar == nextReceivedMonthChar):
        resultString = "Bae, \n\n This happens to be one of your lucky months.\n " \
                       "I am going to be visiting you twice. Yahoo ! " \
                       " Please don't get samosa for my welcome, suna hai aajkal Haija bada faail rakha hai. Anyhow, " \
                       "here are the dates.\n\n" \
                       "First visit is day after : " + str(receivedDate) + " " + str(queryYearNum)
        resultString += "\nSecond visit is day after : " + str(nextReceivedDate) + " " + str(queryYearNum) + ". "

    else:
        resultString = "Bae, \n\nI'll pay you a visit day after " + str(receivedDate) + " " + str(queryYearNum) +". "

    resultString = validateResults(resultString)
    logging.info("Returning Result : "+ resultString)

    return resultString




'''

'''
def constructGetUrl(theMonth, theDate, theYear, theDelta):
    return 'http://www.timeanddate.com/date/dateadded.html?m1=' + \
           str(theMonth) + \
           '&d1=' + \
           str(theDate) + \
           '&y1=' + \
           str(theYear) + \
           '&type=add&ay=&am=&aw=&ad=' + \
           str(theDelta)



'''

'''
def makeGetCall(getUrl):
    r = requests.get(getUrl)
    return r.content


'''

'''
def getExpectedMonthChar(thisMonthNum):
    options = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return options[thisMonthNum]



'''

'''
def getMonthNum(thisMonthChar):

    # if "jan" in thisMonthChar:
    if thisMonthChar.lower().__contains__("jan"):
        monthId = 1
    if thisMonthChar.lower().__contains__("feb"):
        monthId = 2
    if thisMonthChar.lower().__contains__("mar"):
        monthId = 3
    if thisMonthChar.lower().__contains__("apr"):
        monthId = 4
    if thisMonthChar.lower().__contains__("may"):
        monthId = 5
    if thisMonthChar.lower().__contains__("jun"):
        monthId = 6
    if thisMonthChar.lower().__contains__("jul"):
        monthId = 7
    if thisMonthChar.lower().__contains__("aug"):
        monthId = 8
    if thisMonthChar.lower().__contains__("sep"):
        monthId = 9
    if thisMonthChar.lower().__contains__("oct"):
        monthId = 10
    if thisMonthChar.lower().__contains__("nov"):
        monthId = 11
    if thisMonthChar.lower().__contains__("dec"):
        monthId = 12

    return monthId


'''
Getter for queenBeeEmail
'''
def getQueenBeeEmail():
    global queenBeeEmail
    return queenBeeEmail
'''
Setter for queenBeeEmail
'''
def setQueenBeeEmail(emailAddress):
    global queenBeeEmail
    queenBeeEmail = emailAddress
    logging.debug("Queen Bee Email Address saved. Value :" + emailAddress)
    return


def getNewWisdom():
    wisdomReply = makeGetCall(IrmaAlertProperties.wisdomUrl)
    wisdomReply = extractRegEx(IrmaAlertProperties.wisdomRegExExtractor, wisdomReply )
    wisdomReply = wisdomReply.replace("&quot;","")

    logging.debug("Wisdom Fetched : " + wisdomReply)
    return wisdomReply


def extractRegExIgnoreCase( regularExpression, inputString ):
    result = re.search(regularExpression, inputString, re.IGNORECASE)
    if result is None :
        logging.error( "No reg-ex matches found for regex :" +  regularExpression)
        return None
    return result.group(0)


def extractRegEx( regularExpression, inputString ):
    result = re.search(regularExpression, inputString )
    if result is None :
        logging.error( "No reg-ex matches found for regex :" +  regularExpression)
        return None
    return result.group(0)










