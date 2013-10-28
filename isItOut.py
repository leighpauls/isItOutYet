#!/usr/bin/env python

import urllib2, re, time, sys
import sendEmail

EVENT_STRING = 'nexus 5'
EVENT_URL = 'https://play.google.com/store/devices'

def main():
    p = re.compile(EVENT_STRING, re.IGNORECASE)
    pageContents = urllib2.urlopen(EVENT_URL).read()

    if p.search(pageContents):
        msg = 'Found "' + EVENT_STRING + \
            '" in "' + EVENT_URL + '" at ' + \
            time.asctime(time.gmtime()) + ' UTC'
        # print "message: ", msg
        sendEmail.sendEmail(
            'leigh.pauls@gmail.com',
            'Nexus 5 is OUT!!!',
            msg,
            sys.argv[1])

if __name__=='__main__':
    main()
