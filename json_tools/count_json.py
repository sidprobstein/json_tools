#!/usr/local/bin/python2.7
# encoding: utf-8
'''
@author:     Sid Probstein
@contact:    sidprobstein@gmail.com
'''

#############################################    

import sys
import argparse

from utils.file import make_file_list, load_json_list

#############################################    

def main(argv):
       
    parser = argparse.ArgumentParser(description="Count the number of records in json files")
    parser.add_argument("inputlist", nargs="*", help="path to one or more json files")
    args = parser.parse_args()

    # prepare file lists
    lstFiles = make_file_list(args.inputlist)
    if lstFiles == None:
        sys.exit()
     
    # initialize   
    nFiles = 0

    # process the files
    for sFile in lstFiles:
        print "count_json.py: reading:", sFile,
        lstJson = load_json_list(sFile)
        nFiles = nFiles + 1
        print "found:", len(lstJson), "records"
                             
    # end for
        
# end main 

#############################################    
    
if __name__ == "__main__":
    main(sys.argv)

# end
