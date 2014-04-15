#! /usr/bin/python
#-*- coding:utf-8 -*-
#Filename: printException.py
import sys
import traceback

def printException(excArgs, limit = None, file = sys.stdout):
    """
    use this api:
        1.import sys
        2. import printException as prex
        3. prex.printExection(sys.exc_info(),limit = None,file = sys.stdout)

        optional args:
            limit:  specify the number of trace frames to be print on file (default sys.stdout)
            file:   specify where the traceback message to be display

        example:
            prex.printException(sys.exc_info(), limit = 1, file = sys.stdout)
            
            or 

            prex.printException(sys.exc_info())
    """
    exc_type, exc_value, exc_traceback = excArgs
    traceback.print_exception(exc_type, exc_value, exc_traceback, limit, file)

