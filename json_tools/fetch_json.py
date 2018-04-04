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
import requests

#############################################    

def main(argv):
       
    parser = argparse.ArgumentParser(description='Request a restful URL and store the returned json in a file')
    parser.add_argument('-o', '--outputfile', help="filename to store")
    parser.add_argument('uri', required=True, help="uri to the web service")
    args = parser.parse_args()
   
    url = args.uri
    
    print "fetch_json.py: requesting:", url,
    res = requests.get(url)
    if res.ok:
        
        jData = json.loads(res.content)
                
        if args.outputfile:
            # store the file            
            try:
                f = open(args.outputfile, 'wb')
            except Exception, e:    
                print "error:", e            
                f.close()
                sys.exit(e)
            print "ok,", len(jData), "bytes received, storing:", args.outputfile,
            try:
                json.dump(jData, f, sort_keys=True, indent=4, separators=(',', ': '))
            except Exception, e:
                print "error:", e
                sys.exit(e)
            f.close()
            print "ok"
        else:
            # display on screen
            print "--------------------------------------------------------------------------------"
            print json.dumps(jData, sort_keys=True, indent=4, separators=(',', ': '))
            print "--------------------------------------------------------------------------------"
        # end if args.outputfile

    else:
        # display HTTP error
        res.raise_for_status()
        
    # end if res.ok
    
    # success reading
    res.close()
    
# end main 

#############################################    
    
if __name__ == "__main__":
    main(sys.argv)

# end