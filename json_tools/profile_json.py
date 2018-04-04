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

def profileDict(dictInput, sKey, sLevel):
    
    if sKey == None:
        # start at top level of dict
        for key, value in dictInput.items():
            print sLevel + key,
            dictNext = dictInput[key]
            if isinstance(dictNext, list):
                print '[' + str(len(dictNext)) + ']'
                sLevel = sLevel + '\t'
                profileDict(dictNext[0], None, sLevel)
                sLevel = ""
            else:
                print
            if isinstance(dictNext, dict):
                sLevel = sLevel + '\t'
                profileDict(dictNext, None, sLevel)
                sLevel = ""
        # end for
    else:
        return profileDict(dictInput['sKey'], None, '')
        
    # end if
    
    return 0

#############################################    

def main(argv):
       
    parser = argparse.ArgumentParser(description='Scans json files and prints the heirarchy of key values')
    parser.add_argument('inputlist', nargs="*", help="path to one or more json files")
    args = parser.parse_args()

    # prepare file lists
    lstFiles = make_file_list(args.inputlist)
    if lstFiles == None:
        sys.exit()
        
    # read input file(s)
    for sFile in lstFiles:
        print "profile_json.py: profiling:", sFile
        lstJson = load_json_list(sFile)
        print "--------------------------------------------------------------------------------"
        # profile the first record
        profileDict(lstJson[0], None, '')
        print "--------------------------------------------------------------------------------"
    # end for
    
# end main 

#############################################    
    
if __name__ == "__main__":
    main(sys.argv)

# end