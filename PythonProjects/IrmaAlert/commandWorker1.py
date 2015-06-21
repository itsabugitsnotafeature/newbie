import subprocess, threading
import logging
import IrmaAlertProperties

class Command(object):
    def __init__(self, cmd):
        self.cmd = cmd
        self.process = None

    def run(self, timeout):
        def target():
            # print 'Thread started'
            logging.info("Command execution started with timeout period of " + str(timeout) + " seconds.")

            # self.process = subprocess.Popen(self.cmd, shell=True)
            self.process = subprocess.Popen(self.cmd,
                                            shell=True,
                                            stdout=subprocess.PIPE)
            IrmaAlertProperties.commandConsoleLog, err = self.process.communicate()

            logging.info("Command execution finished gracefully.")
            logging.info("#### Command console log #### \n\n" + IrmaAlertProperties.commandConsoleLog)


        thread = threading.Thread(target=target)
        thread.start()

        thread.join(timeout)
        if thread.is_alive():
            logging.info("Timeout period expired, initiating FORCEFUL TERMINATION OF COMMAND !! ")
            # print 'Terminating process'
            self.process.terminate()
            thread.join()
            logging.error("Terminating process.")
        print self.process.returncode




