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
        1. Get Irma Visit algorithm is only accurate until Aig of 2022.
            The reason behind this is that starting next month (September),
            Aunt visits on 1st september, so the penultimate day falls in August,
            which is the previous month.. hence its never reported.

            From that point on, all reports are 1 day delayed until a similar
            event happens.

    Needed Features :
        1.
'''
def main():

    iteration = 0
    IrmaAlertUtils.setup()
    IrmaAlertUtils.setEmailScannerFlag()

    '''
    Debug 1 : Run service Without scanning email
    '''
    # IrmaAlertUtils.startService()


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
