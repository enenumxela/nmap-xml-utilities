#!/usr/bin/env python3

import xml.etree.ElementTree as ET

from argparse import ArgumentParser

def parse_ips(nmap_results):
	host_ip_list = [];
	
	for host in nmap_results.findall('host'):
		for hostip in host.iterfind('address[@addrtype="ipv4"]'):
			host_ip_list.append(hostip.get('addr'))
	
	return host_ip_list

def parse_ports(nmap_results, service_name, service_prefix):
	ports = nmap_results.iter('port')
	
	open_port_list = [];
	deduped_open_port_list = []

	for port in ports:
		services = port.iter('service')

		for service in services:
			if service_name == "" and service_prefix == "":
				open_port_list.append(port.get('portid'))

			if service_name != "":
				if service.get("name") == service_name:
					open_port_list.append(port.get('portid'))

			if service_prefix != "":
				if service.get("name").startswith(service_prefix):
					open_port_list.append(port.get('portid'))

	open = set()
	open_add = open.add
	deduped_open_port_list = [ x for x in open_port_list if not (x in open or open_add(x))]
	deduped_open_port_list.sort(key=int)
	
	return deduped_open_port_list

def display_output(items, separator):
	count = len(items)
	current = 0
	output = ""

	for item in items:
		current = current + 1

		if current == count:
			output = output + item
		else:
			output = output + item + separator
	
	print(output)

if __name__ == "__main__":
	
	import sys
	if sys.version_info <= (3, 0):
		sys.stdout.write("This script requires Python 3.x\n")
		sys.exit(1)

	parser = ArgumentParser()
	parser.add_argument(action="store", dest="nmap_xml_file", help="Nmap XML output file", metavar="FILE")
	parser.add_argument('-ips', action='store_true', dest='ips', help='list of live ipv4s')
	parser.add_argument('-ports', action='store_true', dest='ports', help='list open ports')
	parser.add_argument("-service", action="store", dest="service_name", help="service to filter by", metavar="SERVICE", default='')
	parser.add_argument("-service-prefix", action="store", dest="service_prefix", help="service prefix to filter by", metavar="PREFIX", default='')
	parser.add_argument("-separator", action="store", dest="separator", help="output separator", metavar="SEPARATOR", default='\n')

	args = parser.parse_args()

	s = set()

	if args.nmap_xml_file == "":
		sys.exit("No Nmap XML file specified. (try --help)")
	else:
		try: 
			nmap_results = ET.ElementTree(file=args.nmap_xml_file)
		except:
			sys.exit("Please specify a valid nmap XML file")

	if args.ips == True:
		host_ip_list = (parse_ips(nmap_results))

		display_output(host_ip_list, args.separator)
	
	if args.ports == True:
		open_port_list = parse_ports(nmap_results, args.service_name, args.service_prefix)

		display_output(open_port_list, args.separator)