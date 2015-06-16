__author__ = 'ununoctium'

import poplib
import os
import time
import ScannerUtils
from email import parser
import logging
import sys
import ScannerProperties


'''

'''
def main():

    iteration = 0
    ScannerUtils.setup()
    ScannerUtils.setEmailScannerFlag()
    # ScannerUtils.resetCrawlerFlag()

    while (  ScannerUtils.isEmailScannerEnabled() ) :
        if not iteration == 0:
            logging.debug('Iteration complete. Hibernate for ' + str( ScannerUtils.getSleepTimeInterval() ) + ' seconds.')
            ScannerUtils.addSleep( ScannerUtils.getSleepTimeInterval() )

        logging.debug('Starting program.')
        logging.debug('Iteration #' + str(iteration) )
        ScannerUtils.getGmailViaImap()

        if ScannerUtils.getServiceFlagStatus():
            ScannerUtils.startService()
        else:
            logging.debug("No trigger received thus far.")

        iteration +=1

    logging.debug('Goodbye Master !! \n'
                  '**** Terminating program ****')



if __name__ == '__main__':
  main()
