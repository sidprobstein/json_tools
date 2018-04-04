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
       
    parser = argparse.ArgumentParser(description="Remove duplicates from json files using one or more key/value pairs, optionally write .deduped files")
    parser.add_argument('-o', '--output', action="store_true", help="write de-duplicated output to .deduped.json")
    parser.add_argument('-k', '--keys', required=True, help="key or keys to use for duplicate detection, | delimited")
    parser.add_argument('inputlist', nargs="*", help="path to one or more json files")
    args = parser.parse_args()

    # prepare keys for duplicate detection    
    lstKeys = []
    if args.keys.find('|') > -1:
        lstKeys = args.keys.split('|')
    else:
        lstKeys.append(args.keys)        
    
    # prepare file lists
    lstFiles = make_file_list(args.inputlist)
    if lstFiles == None:
        sys.exit()

    # initialize   
    nFiles = 0
    nRecordsTotal = 0
    nDupesTotal = 0

    # read input file(s)
    for sFile in lstFiles:
        print "dedupe_json: reading:", sFile,
        lstJson = load_json_list(sFile)
        print "found", len(lstJson), "records"
        nRecordsTotal = nRecordsTotal + len(lstJson)
        nFiles = nFiles + 1

        # find duplicates
        dictRecords = {}
        for jRecord in lstJson:
            sTmpKey = ""
            for key in lstKeys:
                if not jRecord.has_key(key):
                    print "dedupe_json: record missing key:", key, jRecord
                    continue
                sTmpKey = sTmpKey + str(jRecord[key]) + '_'
            if dictRecords.has_key(sTmpKey):
                dictRecords[sTmpKey] = dictRecords[sTmpKey] + 1
                jRecord['DUPLICATE'] = 'Y'
            else:
                dictRecords[sTmpKey] = 1
                jRecord['DUPLICATE'] = 'N'

        # report
        nDupes = 0
        for key, value in dictRecords.items():
            if value > 1:
                nDupes = nDupes + (value - 1)
                print "dedupe_json: duplicate:", str(key), "(" + str(value) + ")"
    
        print "dedupe_json: found:", nDupes, "duplicates",
        if nDupes == 0:
            print ":-)"
        else:
            print ":-\\"
        nDupesTotal = nDupesTotal + nDupes

        # remove duplicates
        print "dedupe_json: removing:", nDupes, "duplicates"
        lstDeduped = []
        for jRecord in lstJson:
            if jRecord['DUPLICATE'] == 'Y':
                continue
            del jRecord['DUPLICATE']
            lstDeduped.append(jRecord)
        # sanity check
        if (len(lstDeduped) + nDupes) != len(lstJson):
            print "ERROR!"
            sys.exit(1)
    
        if args.output:
            # write new file
            sOutputFile = sFile[:sFile.find('.json')] + '.deduped' + '.json'
            print "dedupe_json: writing:", sOutputFile,
            try:
                fo = open(args.outputfile, 'wb')
            except Exception, e: 
                print "error:", e               
                continue
            # write the file
            try:
                json.dump(lstDeduped, fo, sort_keys=True, indent=4, separators=(',', ': '))
            except Exception, e:
                print "error:", e   
                fo.close()            
                continue
            fo.close()
            print "ok"
        else:
            # display
            print "--------------------------------------------------------------------------------"
            print json.dumps(lstDeduped, sort_keys=True, indent=4, separators=(',', ': '))
            print "--------------------------------------------------------------------------------"

    # report
    fPercentDupes = float(nDupesTotal) / float(nRecordsTotal) 
    print "dedupe_json.py: removed:", nDupesTotal, "duplicates from", nRecordsTotal, "records (%0.2f)" % fPercentDupes, "in", nFiles, "files" 
    
# end main 

#############################################    
    
if __name__ == "__main__":
    main(sys.argv)

# end
