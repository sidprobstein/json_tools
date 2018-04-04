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
import operator

from utils.file import make_file_list, load_json_list

#############################################    

def main(argv):
       
    parser = argparse.ArgumentParser(description="Sorts json file using a specific key, optionally write .sorted files")
    parser.add_argument('-o', '--output', action="store_true", help="write sorted output to .sorted.json file")
    parser.add_argument('-k', '--key', required=True, help="key to use for sorting,")
    parser.add_argument('-d', '--descending', action="store_true", help="sort in descending order")
    parser.add_argument('inputlist', nargs="*", help="path to one or more json files")
    args = parser.parse_args()

    # prepare file lists
    lstFiles = make_file_list(args.inputlist)
    if lstFiles == None:
        sys.exit()

    # prepare file lists
    lstFiles = make_file_list(args.inputlist)
    if lstFiles == None:
        sys.exit()

    # initialize   
    nFiles = 0
    nRecordsTotal = 0

    # read input file(s)
    for sFile in lstFiles:
        print "sort_json.py: reading:", sFile,
        lstJson = load_json_list(sFile)
        print "found", len(lstJson), "records"
        nRecordsTotal = nRecordsTotal + len(lstJson)
        nFiles = nFiles + 1
        
        # construct new dict that is sorted correctly
        if args.descending:
            lstSorted = sorted(lstJson, key=operator.itemgetter(args.key),reverse=True)
        else:    
            lstSorted = sorted(lstJson, key=operator.itemgetter(args.key))
        
        if args.output:
            # write new file
            sOutputFile = sFile[:sFile.find('.json')] + '.sorted' + '.json'
            print "sort_json.py: writing", sOutputFile,
            try:
                fo = open(sOutputFile, 'wb')
            except Exception, e: 
                print "error:", e               
                continue
            # write the file
            try:
                json.dump(lstSorted, fo, sort_keys=True, indent=4, separators=(',', ': '))
            except Exception, e:
                print "error:", e   
                fo.close()            
                continue
            fo.close()
        else:
            # display
            print "--------------------------------------------------------------------------------"
            print json.dumps(lstSorted, sort_keys=True, indent=4, separators=(',', ': '))
            print "--------------------------------------------------------------------------------"
            

    # report
    print "sort_json.py: sorted:", nRecordsTotal, "records from", nFiles, "files" 

# end main 

#############################################    
    
if __name__ == "__main__":
    main(sys.argv)

# end
