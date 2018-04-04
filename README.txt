=============
json_tools
=============

Tools for working with json files such as preparing them for indexing

* Handles single (canonical) json files 
* Handles files which contain arrays of json
* Most scripts accept multiple file specs, wildcards, etc

jcount.py:  count the number of records in json files
jdedupe.py: remove duplicates from json files using one or more key/value pairs, optionally write .deduped files
jfetch.py:  request a restful URL and store the returned json in a file
jmerge.py:  merges two or more json files into a .merged file
jpretty.py: pretty prints json files
jprofile.py:   scans json files and prints the heirarchy of key values
jscan.py:	scans json files for specific keys/values 
jsort.py:   sorts json file using a specific key, optionally write .sorted files
jsplit.py:  splits json files into .split.value files based on the value of a specified key
 
 
jcount.py
--------
python jcount.py [-h] filespec

Arguments
---------
-h requests help
filespec must be the path to one or more json files

Notes
-----
* jcount.py reports the total number of files it scanned, and the count of records in each
* single json files are counted as one record


jdedupe.py
--------
python dedupe.py [-h] [-o] -k "KEY1|KEY2|...|KEYn" filespec

Arguments
---------
-h requests help
-o will cause jdedupe.py to write a .deduped version of each file 
filespec must be the path to one or more json files

Notes
-----
* jdedupe.py considers a record to be a duplicate when the aggregate of all key values are not unique within the file
* jdedupe.py retains on the the first record to have this unique key; all subsequent duplicates are dropped


jfetch.py
--------
python jfetch.py [-h] [-o outputfile] uri

Arguments
---------
-h requests help
-o outputfile specifies the name which the response from uri will be written
uri is the uri to a restful web service

Notes
-----
* jfetch.py will report the standard HTTP error codes, if it encounters one
* jfetch.py does not currently support redirects


jmerge.py
--------
python jmerge.py [-h] [-o] filespec

Arguments
---------
-h requests help
-o outputfile specifies the name which the merged json data wil be written
filespec must be the path to one or more json files

Notes
-----
* jmerge.py currently operates in memory (sorry) so a core dump will occur if you try to merge more files than there is RAM


jpretty.py
--------
python jpretty.py [-h] filespec

Arguments
---------
-h requests help
filespec must be the path to one or more json files

Notes
-----
* jpretty.py uses the standard python format to pretty print files


jprofile.py
--------
python .py [-h] filespec

Arguments
---------
-h requests help
filespec must be the path to one or more json files

Notes
-----
* jprofile.py prints out the keys at each level of a particular json record, using the first record as a sample


jscan.py
--------
python jscan.py [-h] -k "KEY1=VALUE1|KEY2=VALUE2|...|KEYn=VALUEn" filespec

Arguments
---------
-h requests help
-k specifies one or more keys, and optionally values, to scan for
filespec must be the path to one or more json files

Notes
-----
* jscan.py scans each file in filespec, and reports record numbers that match all specified keys/values
* if no value is specified, existance of the key is checked

jsort.py
--------
python jsort.py [-h] [-o] -k KEY filespec

Arguments
---------
-h requests help
-o will cause jsort.py to write a .sorted version of each file 
-k KEY specifies the sort key
-d makes the sort descending (default is ascending)
filespec must be the path to one or more json files

Notes
-----
* jsort.py sorts json files using the specified key


jsplit.py
--------
python jsplit.py [-h] [-o] -k KEY filespec

Arguments
---------
-h requests help
-k KEY specifies the key to split records on 
-o will cause jsplit.py to copy records with the specified KEY = VALUE into .split.VALUE files
filespec must be the path to one or more json files

Notes
-----
* jsplit.py writes records with KEY blank into a .None file
* jsplit.py does not write out files that are missing KEY entirely