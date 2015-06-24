import re

__author__ = 'ununoctium'

import poplib
import os
import time
import IrmaAlertUtils
from email import parser
import logging
import sys
import IrmaAlertProperties


'''
NOTE :
    Known Bug :
        1. Get Irma Visit algorithm is only accurate until Aug of 2022.
            The reason behind this is that starting next month (September),
            Aunt visits on 1st september, so the penultimate day falls in August,
            which is the previous month.. hence its never reported.

            From that point on, all reports are 1 day delayed until a similar
            event happens.

            Another theory is that its probably caused by leap year bullshit.

        2. **[DONE] : Emails with UPPER CASE subject lines are not being marked as read once mail is downloaded.
        3. Like "may" or "aug" get triggered even when untended. Example straings are nAUGhty and mayweather.


    Needed Features :
        1. **[DONE] : Extract senders email address.
        2. **[DONE] : Smart text in reply, adding new wisdom with each mail.
        3. **[DONE] : Better Trigger string.
        4. **[DONE] : Better termination string.
        5. **[DONE] : Default value for daysSinceFirstFlow should be days to current month.
        6. **[DONE] : Reply if parameter unreadable
        7. **[DONE] : Initialize defaults for all property files
        8. Scale to other business partners.
        9. **[DONE] : If date given before May 2015. Tell tina to stop being naughty.
        10. Enable Debug Flag in Main.
        11. Code Cleanup : regex refactor
        12. **[DONE] : Termination string confirmation email.
        13. Leap year adjustments.
        14. IF two activation mails are sent consicutively, at same time.
        15. Notification email once Serivce is triggered by User.

'''

def main():

    iteration = 0
    IrmaAlertUtils.setup()
    IrmaAlertUtils.setEmailScannerFlag()

    '''
    Debug 1 : Run service Without scanning email
    '''
    # IrmaAlertUtils.startService()
    # print IrmaAlertUtils.getNewWisdom()


    while (  IrmaAlertUtils.isEmailScannerEnabled() ) :
        if not iteration == 0:
            logging.debug('Iteration complete. Hibernate for ' + str( IrmaAlertUtils.getSleepTimeInterval() ) + ' seconds.')
            IrmaAlertUtils.addSleep( IrmaAlertUtils.getSleepTimeInterval() )

        logging.debug('Starting program.')
        logging.debug('Iteration #' + str(iteration) )
        IrmaAlertUtils.getGmailViaImap()

        if IrmaAlertUtils.getServiceFlagStatus():
            IrmaAlertUtils.startService()
        else:
            logging.debug("No trigger received thus far.")

        iteration +=1

    logging.debug('Goodbye Master !! \n'
                  '**** Terminating program ****')



if __name__ == '__main__':
  main()
