import dns.resolver
import argparse
import json

from dns.resolver import NXDOMAIN, NoAnswer, Resolver, Timeout
from termcolor import colored, cprint

parser = argparse.ArgumentParser()

requiredNamed = parser.add_argument_group('Required Arguments')
requiredNamed.add_argument("-d", "--domain", default=None, help="FQDN to fetch the SRV records for")
args = parser.parse_args()

def lookup_srv(domain):
    srv_records=dns.resolver.query(domain, 'SRV')
    srvinfo={}
    records=[]
    for srv in srv_records:
        record={}
        record['weight']   = srv.weight
        record['priority'] = srv.priority
        record['host']     = str(srv.target).rstrip('.')
        record['port']     = srv.port
        record['resolvedAddresses'] = lookup_a(str(srv.target).rstrip('.'))
        records.append(record)
    print(records)
    srvinfo['records'] =  records
    return srvinfo

def lookup_a(domain):
    result = dns.resolver.query(domain, 'A')
    resolved_addresses = []
    for ipval in result:
        resolved_addresses.append("{}".format(ipval.to_text()))
    return resolved_addresses

def main():
    if args.domain is None:
        cprint("Please specify the FQDN to fetch the SRV Records using the flag -d or --domain", "red")
    else:
        try:
            srvinfo = lookup_srv(args.domain)
            print(json.dumps(srvinfo,indent=4,skipkeys=True))
        except NXDOMAIN:
            cprint("Lookup for domain {} failed with NXDOMAIN".format(args.domain),"red")
        except Timeout:
            cprint("Looking up domain {} failed with a Timeout".format(args.domain),"red")
        
if __name__ == "__main__":
    main()
