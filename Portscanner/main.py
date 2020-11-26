from argparse import ArgumentParser
from py_portscanner import PortScanner

parser = ArgumentParser(description="Port Scanner Build in python ",epilog="""This is a description usage
    python main.py -H 0.0.0.0  """)

req_parser = parser.add_argument_group('Required Argument')

req_parser.add_argument('-H','--host',dest='host',type=str,help="specify host ip address",required=True)
req_parser.add_argument('-t','--thread',dest='thread',type=int,help="enter number of thread ")

args= parser.parse_args()

host = args.host
threads = args.thread

if threads:
	p = PortScanner(host,threads)

elif host:
	p = PortScanner(host)

p.main() 
