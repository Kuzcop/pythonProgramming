#!/bin/python

from commonImports import *

class commonLib():
    
    def runcmd(self, logger, cmd):
        
        exit_code,output=subprocess.getstatusoutput(cmd)
        logger.info(output)
        
        return exit_code, output