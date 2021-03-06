# json_tools

Tools for working with json files such as preparing them for indexing...

* Handles single (canonical) json files 
* Handles files which contain arrays of json
* Most scripts accept multiple file specs, wildcards, etc

See descriptions below!

---

# count_json.py
Counts the number of records in json files

## Usage
```
python count_json.py [-h] filespec
```

## Arguments
```
-h requests help
filespec must be the path to one or more json files
```

## Notes
* count_json.py reports the total number of files it scanned, and the count of records in each
* single json files are counted as one record

---

# dedupe_json.py
Remove duplicates from json files using one or more key/value pairs, optionally write .deduped files

## Usage
```
python dedupe_json.py [-h] [-o] -k "KEY1|KEY2|...|KEYn" filespec
```

## Arguments
```
-h requests help
-o will cause dedupe_json.py to write a .deduped version of each file 
filespec must be the path to one or more json files
```
## Notes
* dedupe_json.py considers a record to be a duplicate when the aggregate of all key values are not unique within the file
* dedupe_json.py retains on the the first record to have this unique key; all subsequent duplicates are dropped

---

# fetch_json.py
Request a restful URL and store the returned json in a file

## Usage
```
python fetch_json.py [-h] [-o outputfile] uri
```

## Arguments
```
-h requests help
-o outputfile specifies the name which the response from uri will be written
uri is the uri to a restful web service
```

## Notes
* fetch_json.py will report the standard HTTP error codes, if it encounters one
* fetch_json.py does not currently support redirects

---

# merge_json.py
Merges two or more json files into a .merged file

## Usage
```
python merge_json.py [-h] [-o] filespec
```

## Arguments
```
-h requests help
-o outputfile specifies the name which the merged json data wil be written
filespec must be the path to one or more json files
```

## Notes
* merge_json.py currently operates in memory (sorry) so a core dump will occur if you try to merge more files than there is RAM

---

# pretty_json.py
Pretty prints json files

## Usage
```
python pretty_json.py [-h] filespec
```

## Arguments
```
-h requests help
filespec must be the path to one or more json files
```

## Notes
* pretty_json.py uses the standard python format to pretty print files

---

# profile_json.py
Prints each level of keys in the first record of json files

## Usage 
```
python profile_json.py [-h] filespec
```

## Arguments
```
-h requests help
filespec must be the path to one or more json files
```

## Notes
* Still a work in progress

---

# scan_json.py

## Usage
```
python scan_json.py [-h] -k "KEY1=VALUE1|KEY2=VALUE2|...|KEYn=VALUEn" filespec
```

## Arguments
```
-h requests help
-k specifies one or more keys, and optionally values, to scan for
filespec must be the path to one or more json files
```

## Notes
* scan_json.py scans each file in filespec, and reports record numbers that match all specified keys/values
* if no value is specified, existance of the key is checked

---

# sort_json.py
```
python sort_json.py [-h] [-o] -k KEY filespec
```

## Arguments
```
-h requests help
-o will cause jsort.py to write a .sorted version of each file 
-k KEY specifies the sort key
-d makes the sort descending (default is ascending)
filespec must be the path to one or more json files
```

## Notes
* sort_json.py sorts json files using the specified key

---

# spit_json.py

## Usage
```
python jsplit.py [-h] [-o] -k KEY filespec
```

## Arguments
```
-h requests help
-k KEY specifies the key to split records on 
-o will cause jsplit.py to copy records with the specified KEY = VALUE into .split.VALUE files
filespec must be the path to one or more json files
```

## Notes
* split_json.py writes records with KEY blank into a .None file
* split_json.py does not write out files that are missing KEY entirely

