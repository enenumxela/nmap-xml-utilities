#!/usr/bin/env python3

import os
import re
import logging
import xml.etree.ElementTree as ET

from argparse import ArgumentParser

def merge_nMap(xmlFile, mf):
	HOSTS = 0

	with open(mf, mode = 'a', encoding='utf-8') as mergFile:
		with open(xmlFile) as f:
			if not f.read(1):
				logging.warning(f"Skipping empty file: {xmlFile}")

				return HOSTS

			f.seek(0)

			try:
				nMapXML = ET.parse(f)
			except ET.ParseError as e:
				logging.error(f"Failed to parse {xmlFile}: {e}")

				return HOSTS

			for host in nMapXML.findall('host'):
				HOSTS = HOSTS + 1

				cHost = ET.tostring(host, encoding='unicode', method='xml') 

				mergFile.write(cHost)
				mergFile.flush()

	return HOSTS

def addHeader(f):
	nMap_Header  = '<?xml version="1.0" encoding="UTF-8"?>'
	nMap_Header += '<!DOCTYPE nmaprun>'
	nMap_Header += '<?xml-stylesheet href="file:///usr/share/nmap/nmap.xsl" type="text/xsl"?>'
	nMap_Header += '<!-- Nmap Merged with https://github.com/enenumxela/nmap-utils/blob/main/merge-nmap-xml -->'
	nMap_Header += '<nmaprun scanner="nmap" args="nmap -iL hostList.txt" start="1" startstr="https://github.com/enenumxela/nmap-utils/blob/main/merge-nmap-xml.py" version="7.70" xmloutputversion="1.04">'
	nMap_Header += '<scaninfo type="syn" protocol="tcp" numservices="1" services="1"/>'
	nMap_Header += '<verbose level="0"/>'
	nMap_Header += '<debugging level="0"/>'

	mFile = open(f, "w")

	mFile.write(nMap_Header)
	mFile.close()

def addFooter(f, h):
	nMap_Footer  = '<runstats><finished time="1" timestr="Wed Sep  0 00:00:00 0000" elapsed="0" summary="Nmap done at Wed Sep  0 00:00:00 0000; ' + str(h) + ' IP address scanned in 0.0 seconds" exit="success"/>'
	nMap_Footer += '</runstats>'
	nMap_Footer += '</nmaprun>'

	mFile = open(f, "a")

	mFile.write(nMap_Footer)
	mFile.close()

def main_nMapMerger(xmlSet):
	HOSTS = 0

	# Check to ensute we have work to do
	if not xmlSet:
		print("No XML files were found ... No work to do")

		exit()

	# Create the Merged filename
	from datetime import datetime

	dtNow = datetime.now() 
	dt = re.sub(r"\s+", '-', str(dtNow))
	dt = re.sub(r":", '-', str(dt))
	mergeFile = "merge-nmap-" + dt + ".xml"

	# Add Header to mergefile
	addHeader(mergeFile)

	for xml in xmlSet:
		if xml.endswith('.xml'):
			logging.debug("Parsing: %r", xml)

			H = merge_nMap(xml, mergeFile)

			HOSTS = HOSTS + H

	# Add Footer to mergefile
	addFooter(mergeFile, HOSTS)

	print('')
	print ("Output XML File:", os.path.abspath(mergeFile))

if __name__ == "__main__":
	
	import sys
	if sys.version_info <= (3, 0):
		sys.stdout.write("This script requires Python 3.x\n")
		sys.exit(1)

	parser = ArgumentParser()

	parser.add_argument("-f", "--file", 	dest="filename", help="XML file to merge", metavar="FILE")
	parser.add_argument("-d", "--dir", 		dest="directory", help="XML files to merge directory", metavar="DIR")
	parser.add_argument("-q", "--quiet",	dest="verbose",	action="store_false", default=True, help="don't print status messages to stdout")

	args = parser.parse_args()

	s = set()
	
	if args.verbose:
		logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

		print('Debug On')

	if args.filename is not None:
		f = args.filename
		if f.endswith('.xml'):
			logging.debug("Adding: %r", f)

			s.add(f)

	elif args.directory is not None:
		if os.path.isdir(args.directory):
			path = args.directory
			
			for f in os.listdir(path):
				# For now we assume xml is nMap
				if f.endswith('.xml'): 
					fullname = os.path.join(path, f)

					logging.debug("Adding: %r", fullname)

					s.add(fullname)
		else:
			logging.warn("Not a directory: %r", args.directory)
	else :
		print ("usage issues =(")

		parser.print_help()

		exit()

	main_nMapMerger(s)
