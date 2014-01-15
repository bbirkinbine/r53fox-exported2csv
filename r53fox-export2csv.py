#!/usr/bin/env python
#
# take R53Fox exported json and convert it to .csv
#

import argparse
import json

def main():

    parser = argparse.ArgumentParser(description='Convert R53Fox exported json to CSV')
    parser.add_argument('-i', '--infile', help='file to read in for parsing.', required=True)

    args = parser.parse_args()

    js = json.load(open(args.infile,'r'))

    for domain in js.keys():
        hostedzoneid = js[domain]['HostedZoneId']
        comment = js[domain]['Comment']
        callerreference = js[domain]['CallerReference']
        for rrs in js[domain]['ResourceRecordSets']:
            name = rrs['Name']
            weight = rrs['Weight']
            setidentifier = rrs['SetIdentifier']
            ttl = rrs['TTL']
            type = rrs['Type']
            for item in rrs['Value']:
                print("'%s','%s','%s','%s','%s','%s'" % (domain,name,ttl,type,item,comment))
                #print("'%s','%s','%s','%s','%s','%s','%s','%s','%s'" % (domain,name,ttl,type,item,weight,callerreference,setidentifier,comment))

if __name__ == '__main__':
    main()
