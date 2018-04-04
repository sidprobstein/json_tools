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
       
    parser = argparse.ArgumentParser(description="Scans json files for specific keys/values")
    parser.add_argument('-k', '--keys', required=True, help="key/value list in format key=value, | delimited")
    parser.add_argument('inputlist', nargs="*", help="path to one or more json files")
    args = parser.parse_args()

    # prepare file lists
    lstFiles = make_file_list(args.inputlist)
    if lstFiles == None:
        sys.exit()
        
    # initialize
    nFiles = 0
        
    # handle multiple keys passed in as argument
    
    lstKVs = []
    if args.keys.find('|') > -1:
        lstKVs = args.keys.split('|')
    else:
        # must be only one
        lstKVs.append(args.keys)        

    for sFile in lstFiles:
        # scan each input file
        lstJson = load_json_list(sFile)
        nFiles = nFiles + 1
        nRecord = 0
        nMatch = 0
        for jRecord in lstJson:
            nRecord = nRecord + 1
            bMatch = False
            for kv in lstKVs:
                k = kv
                v = None
                if kv.find('='):
                    k = kv[:kv.find('=')]
                    v = kv[kv.find('=')+1:]
                if jRecord.has_key(k):
                    if v:
                        if str(jRecord[k]) == v:
                            bMatch = True
                        else:
                            bMatch = False
                        # end if
                    else:
                        bMatch = True
                    # end if
                else:
                    bMatch = False
                # end if 
                if not bMatch:
                    break
            # end for
            if bMatch:
                nMatch = nMatch + 1
                print "scan_json.py: matched:", sFile, "record:", nRecord
                print "--------------------------------------------------------------------------------"
                print json.dumps(jRecord, sort_keys=True, indent=4, separators=(',', ': '))
                print "--------------------------------------------------------------------------------"
        # report            
        if nMatch > 0:    
            print "scan_json.py: found:", nMatch, "matches"
        # end for
    # end for
        
# end main 

#############################################    
    
if __name__ == "__main__":
    main(sys.argv)

# end
