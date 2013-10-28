import urllib2, re, time
import sendEmail

EVENT_STRING = 'nexus 5'
EVENT_URL = 'https://play.google.com/store/devices'

p = re.compile(EVENT_STRING, re.IGNORECASE)
pageContents = urllib2.urlopen(EVENT_URL).read()

if p.search(pageContents):
    msg = 'Found "' + EVENT_STRING + \
        '" in "' + EVENT_URL + '" at ' + \
        time.asctime(time.gmtime()) + ' UTC'
    print "message: ", msg
    sendEmail.sendEmail(
        'leigh.pauls@gmail.com',
        'Nexus 5 is OUT!!!',
        msg,
        'credentials.txt')
else:
    print 'no match :('

