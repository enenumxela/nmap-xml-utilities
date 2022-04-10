# nmap-utils

* [Merge nmap xml files](#merge-nmap-xml-files)

## [Merge nmap xml files](./merge-nmap-xml)

Merge Multiple nmap xml output files into a single xml file.

```bash
merge-nmap-xml -h
```

```text
usage: merge-nmap-xml [-h] [-f FILE] [-d DIR] [-q]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  parse FILE
  -d DIR, --dir DIR     Parse all xml in directory
  -q, --quiet           don't print status messages to stdout
```

## [Parse nmap xml file](./parse-nmap-xml)

Parse nmap xml output file to extract bits of information.