# nmap-xml-utilities

Utilities to process nmap XML output.

## Scripts

* [Merge nmap xml files](#merge-nmap-xml-files)
* [Parse nmap xml file](#parse-nmap-xml-file)

### [Merge nmap xml files](https://raw.githubusercontent.com/enenumxela/nmap-xml-utilities/main/merge-nmap-xml.py)

Merge Multiple nmap xml output files into a single xml file.

#### Installation

```bash
curl -sL https://raw.githubusercontent.com/enenumxela/nmap-xml-utilities/main/merge-nmap-xml.py > ~/.local/bin/merge-nmap-xml
```

#### Uage

```bash
merge-nmap-xml.py -h
```

```text
usage: merge-nmap-xml [-h] [-f FILE] [-d DIR] [-q]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  parse FILE
  -d DIR, --dir DIR     Parse all xml in directory
  -q, --quiet           don't print status messages to stdout
```

### [Parse nmap xml file](https://raw.githubusercontent.com/enenumxela/nmap-xml-utilities/main/parse-nmap-xml.py)

Parse nmap xml output file to extract bits of information.

#### Installation

```bash
curl -sL https://raw.githubusercontent.com/enenumxela/nmap-xml-utilities/main/parse-nmap-xml.py > ~/.local/bin/parse-nmap-xml
```

#### Uage

```bash
parse-nmap-xml.py -h
```

```text
usage: parse-nmap-xml [-h] [-ips] [-ports] [-service SERVICE] [-service-prefix PREFIX] [-separator SEPARATOR] FILE

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