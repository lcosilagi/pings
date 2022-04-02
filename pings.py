#!/usr/bin/env python3 

import ipaddress, subprocess, argparse, sys


ip = 0

parser = argparse.ArgumentParser(usage = './%(prog)s -i [endereço ip]',
                                        description = 'Script para verificar hosts online através de ping')

parser.add_argument("-i", dest = "ip", required = False, help = "especifique o endereço IP ou range de endereço que deseja dar ping. Ex: 192.168.10.1 ou 192.168.10.0/24")


arg = parser.parse_args()

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

ip = arg.ip

mynet = ipaddress.ip_network(ip)

for host in mynet.hosts():                        
    host = str(host)                                
    proc = subprocess.run(                          
        ['ping', host, '-c', '1', '-w', '1', '-s', '1'],
        stderr=subprocess.DEVNULL,                  
        stdout=subprocess.DEVNULL                   
        )
    
    if  proc.returncode == 0:                       
        print(f'{host} \tOK')                 
