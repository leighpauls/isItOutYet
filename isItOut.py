import urllib2, re, time, sys
import sendEmail

NEW_HOTNESS = 'Nexus 5'
OLD_BUSTED = 'nexus 4'
EVENT_URL = 'https://play.google.com/store/devices'

def main():
    newHotnessRegex = re.compile(NEW_HOTNESS, re.IGNORECASE)
    oldBustedRegex = re.compile(OLD_BUSTED, re.IGNORECASE)
    pageContents = urllib2.urlopen(EVENT_URL).read()

    newHotnessFound = newHotnessRegex.search(pageContents)
    oldBustedGone = not oldBustedRegex.search(pageContents)

    if newHotnessFound or oldBustedGone:
        condition = 'Found "' + NEW_HOTNESS + '"'
        if oldBustedGone:
            condition = '"' + OLD_BUSTED + '" was not found'

        msg = condition + ' at ' + EVENT_URL + ' at ' + \
            time.asctime(time.gmtime()) + ' UTC'
        # print "message: ", msg
        sendEmail.sendEmail(
            sys.argv[1],
            sys.argv[2],
            NEW_HOTNESS + ' is OUT!!!',
            msg)

if __name__=='__main__':
    main()
