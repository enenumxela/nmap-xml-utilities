# nmap-xml-utilities

Utilities to process nmap XML output.

## Scripts

* [Merge nmap xml files](#merge-nmap-xml-filesnmap-merge-xml)
* [Parse nmap xml file](#parse-nmap-xml-filenmap-parse-xml)

### [Merge nmap xml files](./nmap-merge-xml)

Merge Multiple nmap xml output files into a single xml file.

```bash
nmap-merge-xml -h
```

```text
usage: nmap-merge-xml [-h] [-f FILE] [-d DIR] [-q]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  parse FILE
  -d DIR, --dir DIR     Parse all xml in directory
  -q, --quiet           don't print status messages to stdout
```

### [Parse nmap xml file](./nmap-parse-xml)

Parse nmap xml output file to extract bits of information.

```bash
nmap-parse-xml -h
```

```text
usage: nmap-parse-xml [-h] [-ips] [-ports] [-service SERVICE] [-service-prefix PREFIX] [-separator SEPARATOR] FILE

positional arguments:
  FILE                  Nmap XML output file

optional arguments:
  -h, --help            show this help message and exit
  -ips                  list of live ipv4s
  -ports                list open ports
  -service SERVICE      service to filter by
  -service-prefix PREFIX
                        service prefix to filter by
  -separator SEPARATOR  output separator
```