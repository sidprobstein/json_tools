#!/usr/local/bin/python2.7
# encoding: utf-8
'''
@author:     Sid Probstein
@contact:    sidprobstein@gmail.com
'''

#############################################    

import sys
import argparse
import json

from utils.file import make_file_list, load_json_list

#############################################    

def main(argv):
       
    parser = argparse.ArgumentParser(description='Merges two or more json files into a .merged file')
    parser.add_argument('-o', '--outputfile', required=True, help="filename to write merged output to")
    parser.add_argument('inputlist', nargs="*", help="path to one or more json files")
    args = parser.parse_args()

    # initialize
    lstFiles = []
    nFiles = 0
    nRecords = 0
    lstMerge = []
       
    # prepare file lists
    lstFiles = make_file_list(args.inputlist)
    if lstFiles == None:
        sys.exit()
        
    for sFile in lstFiles:
        # read the input file   
        print "merge_json.py: reading:", sFile,                     
        lstJson = load_json_list(sFile)
        print "ok", len(lstJson), "records"                        
        # aggregate
        lstMerge = lstMerge + lstJson
        # count
        nFiles = nFiles + 1
        nRecords = nRecords + len(lstJson)

    # merge 
    print"merge_json.py: writing:", len(lstMerge), "records to", args.outputfile,

    try:
        fo = open(args.outputfile, 'wb')
    except Exception, e:              
        print "error:", e  
        sys.exit(e)
    try:
        json.dump(lstMerge, fo, sort_keys=True, indent=4, separators=(',', ': '))
    except Exception, e:
        print "error:", e
        sys.exit(e)
        fo.close()
    fo.close()
    print "ok"
 
# end main 

#############################################    
    
if __name__ == "__main__":
    main(sys.argv)

# end