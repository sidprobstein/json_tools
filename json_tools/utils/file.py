#!/usr/local/bin/python2.7
# encoding: utf-8
'''
@author:     Sid Probstein
@contact:    sidprobstein@gmail.com
'''

#############################################    
# tools for opening json files, including arrays

import json
import os
import glob

#############################################    

def make_file_list(filespec):

    lstFiles = []
           
    if filespec:
        if type(filespec) == list:
            # list, glob each one, then aggregate
            for item in filespec:
                for f in glob.glob(item):
                    lstFiles.append(f)
        else:
            # not list, just do it
            lstFiles = glob.glob(filespec)
 
    return lstFiles

# end def

#############################################    
# open a json file; intended for special handling
# leaves file open!!

def open_json(sFilename):
    
    if not os.path.exists(sFilename):
        print "error: not found"
        return None
    try:
        f = open(sFilename, 'r')
    except Exception, e:
        print "error:", e
        return None
    return f

# end def

#############################################    
# open and load a json file, returning a list to operate on
# automatically closes file after loading

def load_json_list(sFilename):
    
    f = open_json(sFilename)
    if not f:
        return 
    try:
        jsonData = json.load(f)
    except Exception, e:
        print "error:", e
        f.close()
    f.close()
    
    if type(jsonData) == list:
        jsonList = jsonData
    else:
        # single record, make list of 1
        jsonList = []
        jsonList.append(jsonData)
        
    return jsonList

# end def
