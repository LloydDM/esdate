#!/usr/bin/env python

import datetime
import argparse

esmonth = {1: "Morning Star",
           2: "Sun's Dawn",
           3: "First Seed",
           4: "Rain's Hand",
           5: "Second Seed",
           6: "Mid Year",
           7: "Sun's Height",
           8: "Last Seed",
           9: "Heartfire",
           10: "Frostfall",
           11: "Sun's Dusk",
           12: "Evening Star"}

esday = {0: "Morndas",
         1: "Tirdas",
         2: "Middas",
         3: "Turdas",
         4: "Fredas",
         5: "Loredas",
         6: "Sundas"}

parser = argparse.ArgumentParser(description = "Displays the date using the Elder Scrolls calendar.  Using no arguments returns the date emulating the format of the traditional Unix 'date' command.")
group = parser.add_mutually_exclusive_group()
group.add_argument("-a", "--arena", help = "Output emulates the Arena player status screen", action = "store_true")
group.add_argument("-d", "--daggerfall", help = "Output emulates the Daggerfall compass screen", action = "store_true")
group.add_argument("-m", "--morrowind", help = "Output emulates the Morrowind wait screen", action = "store_true")
group.add_argument("-o", "--oblivion", help = "Output emulates the Oblivion wait screen", action = "store_true")
group.add_argument("-s", "--skyrim", help = "Output emulates the Skyrim wait screen", action = "store_true")
args = parser.parse_args()

i = datetime.datetime.now()

# Setup the hour for 12-hour clock
h = datetime.datetime.strptime(str(i.hour), "%H")

if i.day in [1, 21, 31]:
    suffix = "st"
elif i.day in [2, 22]:
    suffix = "nd"
elif i.day in [3, 23]:
    suffix = "rd"
else:
    suffix = "th"

if 0 <= i.hour <= 2 or 21 <= i.hour <= 23:
    timeofday = 'at night.'
elif 3 <= i.hour <= 5:
    timeofday = 'early morning.'
elif 6 <= i.hour <= 11:
    timeofday = 'in the morning.'
elif 12 <= i.hour <= 17:
    timeofday = 'in the afternoon.'
elif 18 <= i.hour <= 20:
    timeofday = 'in the evening.'

if args.arena:
    print "It is {0:02d}:{1:02d} {2}".format(int(h.strftime("%I")), i.minute, timeofday)
    print "The date is {0}, {1:01d}{2} of {3} in the year 7E {4}".format(esday[i.weekday()], i.day, suffix, esmonth[i.month], i.year) 
elif args.daggerfall:
    print "It is {0:01d}:{1:02d} on {2} the {3:01d}{4} of {5}.".format(i.hour, i.minute, esday[i.weekday()], i.day, suffix, esmonth[i.month])
elif args.morrowind:
    print "{0} {1} (Day {2}) {3:01d} {4}".format(i.day, esmonth[i.month], i.timetuple().tm_yday, int(h.strftime("%I")), h.strftime("%p"))
elif args.oblivion:
    print "{0} {1:01d}:{2:02d} {3}".format(esday[i.weekday()], int(h.strftime("%I")), i.minute, h.strftime("%p"))
    print "{0} {1:01d}, 7E{2}".format(esmonth[i.month], i.day, i.year)
elif args.skyrim:
    print "{0}, {1:01d}:{2:02d} {3}, {4}{5} of {6}".format(esday[i.weekday()], int(h.strftime("%I")), i.minute, h.strftime("%p"), i.day, suffix, esmonth[i.month])
else:
    print "{0} {1} {2} {3}:{4:02d}:{5:02d} 7E{6}".format(esday[i.weekday()], esmonth[i.month], i.day, i.hour, i.minute, i.second, i.year)
