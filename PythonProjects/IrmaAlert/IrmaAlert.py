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

'''
def main():

    iteration = 0
    IrmaAlertUtils.setup()
    IrmaAlertUtils.setEmailScannerFlag()
    # For Debug only
    IrmaAlertUtils.startService()

    # while (  IrmaAlertUtils.isEmailScannerEnabled() ) :
    #     if not iteration == 0:
    #         logging.debug('Iteration complete. Hibernate for ' + str( IrmaAlertUtils.getSleepTimeInterval() ) + ' seconds.')
    #         IrmaAlertUtils.addSleep( IrmaAlertUtils.getSleepTimeInterval() )
    #
    #     logging.debug('Starting program.')
    #     logging.debug('Iteration #' + str(iteration) )
    #     IrmaAlertUtils.getGmailViaImap()
    #
    #     if IrmaAlertUtils.getServiceFlagStatus():
    #         IrmaAlertUtils.startService()
    #     else:
    #         logging.debug("No trigger received thus far.")
    #
    #     iteration +=1

    logging.debug('Goodbye Master !! \n'
                  '**** Terminating program ****')



if __name__ == '__main__':
  main()
