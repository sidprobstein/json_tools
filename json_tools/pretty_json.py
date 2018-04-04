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
       
    parser = argparse.ArgumentParser(description='Pretty prints json files')
    parser.add_argument('inputlist', nargs="*", help="path to one or more json files")
    args = parser.parse_args()

    # prepare file lists
    lstFiles = make_file_list(args.inputlist)
    if lstFiles == None:
        sys.exit()
        
    for sFile in lstFiles:
        lstJson = load_json_list(sFile)
        print "pretty_json.py:", sFile
        print "--------------------------------------------------------------------------------"
        print json.dumps(lstJson, sort_keys=True, indent=4, separators=(',', ': '))
        print "--------------------------------------------------------------------------------"
    # end for
    
# end main 

#############################################    
    
if __name__ == "__main__":
    main(sys.argv)

# end