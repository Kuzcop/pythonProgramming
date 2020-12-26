#!/bin/python

from commonImports import *

class logLib(): 

    def startlogging(self, fname):
        #fname = "testlogging.txt"
        subprocess.getstatusoutput("rm {}".format(fname))

        logger = logging.getLogger('amantest')
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        fh = logging.FileHandler(fname)
        fh.setLevel(logging.DEBUG)

        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.DEBUG)

        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        logger.addHandler(fh)
        logger.addHandler(ch)
        
        return logger


    def stoplogging(self):
        logging.shutdown()

