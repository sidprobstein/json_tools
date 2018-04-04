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
import os

from utils.file import make_file_list, load_json_list

#############################################    

def main(argv):
       
    parser = argparse.ArgumentParser(description='Splits json files into .split.value files based on the value of a specified key')
    parser.add_argument('-k', '--key', required=True, help="key to use for splitting")
    parser.add_argument('inputlist', nargs="*", help="path to one or more json files")
    args = parser.parse_args()

    # prepare file lists
    lstFiles = make_file_list(args.inputlist)
    if lstFiles == None:
        sys.exit()
     
    # initialize   
    nFiles = 0
    nRecordsTotal = 0
    lstOutputFiles = []

    # process the files
    for sFile in lstFiles:
        print "split_json.py: reading:", sFile,
        lstJson = load_json_list(sFile)
        nFiles = nFiles + 1
        print "found:", len(lstJson), "records",
        nRecordsTotal = nRecordsTotal + len(lstJson)
                
        # split the file
        for jRecord in lstJson:
            # does the record have the key?
            if jRecord.has_key(args.key):
                # yes, write it
                sOutputFile = sFile[:sFile.find('.json')] + '.' + jRecord[args.key] + '.json'
                if not sOutputFile in lstOutputFiles:
                    print "split_json.py: splitting file on value:", args.key, '=', jRecord[args.key]
                    lstOutputFiles.append(sOutputFile)
                if os.path.exists(sOutputFile):
                    # append
                    try:
                        fo = open(sOutputFile, 'ab')
                    except Exception, e:              
                        print "split_json.py: error:", e  
                        continue
                    try:
                        fo.write(',')
                        json.dump(jRecord, fo, sort_keys=True, indent=4, separators=(',', ': '))
                    except Exception, e:
                        print "split_json.py: error:", e
                        fo.close()
                        continue
                    fo.close()
                else:
                    try:
                        fo = open(sOutputFile, 'wb')
                    except Exception, e:              
                        print "split_json.py: error:", e  
                        continue
                    try:
                        fo.write('[')
                        json.dump(jRecord, fo, sort_keys=True, indent=4, separators=(',', ': '))
                    except Exception, e:
                        print "split_json.py: error:", e
                        fo.close()
                        continue
                    fo.close()
            else:
                print "split_json.py: warning: record missing key in file", sFile
        # end for
         
        # finalize the split files       
        for sFile in lstOutputFiles:
            print "split_json.py: finishing:", sFile, 
            try:
                fo = open(sFile, 'ab')
            except Exception, e:              
                print "split_json.py: error:", e  
                continue
            try:
                fo.write(']')
            except Exception, e:
                print "split_json.py: error:", e
                fo.close()
                continue
            fo.close()
            print "ok"
        # end for
        
        print "split_json.py: split:", sFile, "into", len(lstOutputFiles), "files on key", args.key
     
    # end for
         
# end main 

#############################################    
    
if __name__ == "__main__":
    main(sys.argv)

# end