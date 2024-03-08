# nmap-xml-utilities

Utilities to process nmap XML output.

## Scripts

* [Merge nmap xml files](#merge-nmap-xml-filesnmap-xml-merge)
* [Parse nmap xml file](#parse-nmap-xml-filenmap-xml-parse)

### [Merge nmap xml files](./nmap-xml-merge)

Merge Multiple nmap xml output files into a single xml file.

#### Installation

```bash
curl -sL https://raw.githubusercontent.com/enenumxela/nmap-xml-utilities/main/nmap-xml-merge > ~/.local/bin/nmap-xml-merge
```

#### Uage

```bash
nmap-xml-merge -h
```

```text
usage: nmap-xml-merge [-h] [-f FILE] [-d DIR] [-q]

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  parse FILE
  -d DIR, --dir DIR     Parse all xml in directory
  -q, --quiet           don't print status messages to stdout
```

### [Parse nmap xml file](./nmap-xml-parse)

Parse nmap xml output file to extract bits of information.

#### Installation

```bash
curl -sL https://raw.githubusercontent.com/enenumxela/nmap-xml-utilities/main/nmap-xml-parse > ~/.local/bin/nmap-xml-parse
```

#### Uage

```bash
nmap-xml-parse -h
```

```text
usage: nmap-xml-parse [-h] [-ips] [-ports] [-service SERVICE] [-service-prefix PREFIX] [-separator SEPARATOR] FILE

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