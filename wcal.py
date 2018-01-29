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
REGEX = "^([0-9]{4})\s([a-z]{3})\s([0-9]{1,2})\s,\s([0-9]{1,2}):([0-9]{2})(a|p)\s-\s([0-9]{1,2}):([0-9]{2})(a|p)\s(.*)$"
NOW = datetime.datetime.now()
ICAL_DTSTAMP = NOW.strftime("%Y%m%dT%H%M%S")

for event in CALENDAR:
    if event.startswith("#", 0, 1):
        pass
    elif event.startswith("\n",0,1):
        pass
    else:
        EVENT_LIST = re.split(REGEX, event.rstrip())
        if len(EVENT_LIST) > 1:
            ICAL_UID = hashlib.sha256(event).hexdigest()
            if EVENT_LIST[6] == "p":
                DTSTART_HOUR = str(int(EVENT_LIST[4]) + 12)
            ICAL_DTSTART = EVENT_LIST[1] + \
                           get_month_index(EVENT_LIST[2]) + \
                           EVENT_LIST[3] + \
                           "T" + \
                           DTSTART_HOUR.zfill(2) + \
                           EVENT_LIST[5] + \
                           "00"
            if EVENT_LIST[9] == "p":
                DTEND_HOUR = str(int(EVENT_LIST[7]) + 12)
            ICAL_DTEND = EVENT_LIST[1] + \
                         get_month_index(EVENT_LIST[2]) + \
                         EVENT_LIST[3] + \
                         "T" + \
                         DTEND_HOUR.zfill(2) + \
                         EVENT_LIST[8] + \
                         "00"
            print EVENT_LIST
            print "DTSTAMP:" + ICAL_DTSTAMP
            print "UID:" + ICAL_UID
            print "DTSTART:" + ICAL_DTSTART
            print "DTEND:" + ICAL_DTEND
