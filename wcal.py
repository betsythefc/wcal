#!/usr/bin/env python

import re
import hashlib
import datetime

def get_month_index(month):
    """Gets 3 character month name and the month number

    Args:
        month   str 3 character month, i.e. jan, feb, dec

    Returns:
        str     2 digit number (string) of month index, i.e. 01, 02, 12
    """
    months = [
    "null",
    "jan",
    "feb",
    "mar",
    "apr",
    "may",
    "jun",
    "jul",
    "aug",
    "sep",
    "oct",
    "nov",
    "dec"
    ]
    return str(months.index(month)).zfill(2)

WHEN_FILE = '/Users/bmcnab/.when/calendar'

CALENDAR = open(WHEN_FILE, "r")
REGEX = "^([0-9]{4})\s([a-z]{3})\s([0-9]{1,2})\s,(\s([0-9]{1,2}):([0-9]{2})(a|p)(\s-\s([0-9]{1,2}):([0-9]{2})(a|p)){0,1}){0,1}\s(.*)"
NOW = datetime.datetime.now()
ICAL_DTSTAMP = NOW.strftime("%Y%m%dT%H%M%S")
ICAL_PRODID = "wcal"

print "BEGIN:VCALENDAR"
print "VERSION:2.0"
print "PRODID:" + ICAL_PRODID
print "CALSCALE:GREGORIAN"
print "METHOD:PUBLISH"

for event in CALENDAR:
    if event.startswith("#", 0, 1):
        pass
    elif event.startswith("\n",0,1):
        pass
    else:
        EVENT_LIST = re.split(REGEX, event.rstrip())
        if len(EVENT_LIST) > 1:
            print "BEGIN:VEVENT"
            print "SUMMARY:" + EVENT_LIST[-2]
            ICAL_UID = hashlib.sha256(event).hexdigest()
            if EVENT_LIST[5] is not None:
                if EVENT_LIST[7] == "p":
                    DTSTART_HOUR = str(int(EVENT_LIST[5]) + 12)
                else:
                    DTSTART_HOUR = str(EVENT_LIST[5])
                ICAL_DTSTART = EVENT_LIST[1] + \
                               get_month_index(EVENT_LIST[2]) + \
                               EVENT_LIST[3] + \
                               "T" + \
                               DTSTART_HOUR.zfill(2) + \
                               EVENT_LIST[6] + \
                               "00"
            else:
                ICAL_DTSTART = EVENT_LIST[1] + \
                               get_month_index(EVENT_LIST[2]) + \
                               EVENT_LIST[3]
            if EVENT_LIST[9] is not None:
                if EVENT_LIST[11] == "p":
                    DTEND_HOUR = str(int(EVENT_LIST[9]) + 12)
                else:
                    DTEND_HOUR = str(EVENT_LIST[9])
                ICAL_DTEND = EVENT_LIST[1] + \
                             get_month_index(EVENT_LIST[2]) + \
                             EVENT_LIST[3] + \
                             "T" + \
                             DTEND_HOUR.zfill(2) + \
                             EVENT_LIST[10] + \
                             "00"
            else:
                ICAL_DTEND = EVENT_LIST[1] + \
                             get_month_index(EVENT_LIST[2]) + \
                             EVENT_LIST[3]
            print "DTSTAMP:" + ICAL_DTSTAMP
            print "UID:" + ICAL_UID
            print "DTSTART:" + ICAL_DTSTART
            print "DTEND:" + ICAL_DTEND
            print "END:VEVENT"

print "END:VCALENDAR"
