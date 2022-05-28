##########################################################################################################

## Developed by Mustafa Ugur Baskin
## Contact: https://www.linkedin.com/in/mustafa-u%C4%9Fur-b-9b0138135/

## GITHUB REPOSITORY ADDRESS: https://github.com/mustafaugurbaskin/Date-and-Time-Finder-for-Python

## APACHE LICENSE 2.0 ® 2020

##########################################################################################################

## IMPROTING LIBRARIES

import datetime
import re
import pytz
import time
import pendulum
import random
from dateutil.relativedelta import relativedelta

## IMPROTING LIBRARIES

##########################################################################################################

class FindDT(object):

    # Initialize
    def __init__(self, inp):

        """
        This class allows user to find date and time from string or input.
        Contains input, tzinfo
        """

        # Input
        self.inp = inp.lower()

        # Set timezone as UTC timezone
        self.local_tz = pytz.UTC
        
        # Set timezone as dict
        self.timezone = {'Europe/Istanbul'}

        # Error words
        self.error = ['Sorry, please say a valid time or date.', 'Unable to find date and time']

    # Find date words from input
    def findDateWords(self):

        """
        This module finds date from given input.
        Inputs should be:

        If date is exact:

        -> August 1, 13 July, 26 August
        -> Next Monday, Next Friday 
        -> On Thursday, On Friday, On Monday

        If date isn't exact and contains 'later, in' etc. add to the current date:
        
        -> Today, tomorrow, overmorrow
        -> Next Day, Next Week, Next Month, Next Year
        -> 5 days later, 8 days later, 3.5 days later
        -> 1 week later, 2 weeks later, 3.5 weeks later
        -> 1 month later, 2 months later, 3.5 month later
        -> 0.5 years later, 1 year later, 2 years later
        """

        try:

            # Date words
            self.month = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
            self.replacemonth = {'january': '1', 'february': '2', 'march': '3', 'april': '4', 'may': '5', 'june': '6', 'july': '7', 'august': '8', 'september': '9', 'october': '10', 'november': '11', 'december': '12'}

            self.daynames = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
            self.replacedaynames = {'monday': pendulum.MONDAY, 'tuesday': pendulum.TUESDAY, 'wednesday': pendulum.WEDNESDAY, 'thursday': pendulum.THURSDAY, 'friday': pendulum.FRIDAY, 'saturday': pendulum.SATURDAY, 'sunday': pendulum.SUNDAY}

            self.next = ['next']
            self.on = ['on']

            self.qtoday = ['today', 'this day']
            self.qtomorrow = ['tomorrow', 'next day', 'next the day']
            self.qovermorrow = ['overmorrow', 'next next day', 'after tomorrow', 'after the tomorrow']

            self.nweek = ['next week', 'next weeks']
            self.nmonth = ['next month', 'next months']
            self.nyear = ['next year', 'next years']

            self.day = ['days', 'day', 'days later', 'day later', 'days after', 'day after']
            self.week = ['weeks', 'week', 'weeks later', 'week later', 'weeks after', 'week after']
            self.lmonth = ['months', 'month', 'months later', 'month later', 'months after', 'month after']
            self.year = ['years', 'year', 'years later', 'year later', 'years after', 'year after']

            # For exact date
            self.days = []
            self.months = []
            self.years = []

            # For adding date to current date
            self.adddays = []
            self.addweeks = []
            self.addmonths = []
            self.addyears = []

            # For 'month'
            if any(mo for mo in self.month if mo in self.inp):

                try:

                    try:

                        # Get day of the month and year from sentence
                        j = "|".join(map(re.escape, self.month))
                        getdate = re.search(fr'(?:{j})\s*(\d{{1,2}})\s*(\d{{4}})\b', self.inp)

                        # <month name>, <day>, <year>
                        if getdate:

                            # Get month name
                            gm = getdate.group().split()
                            gm = ''.join([i for i in gm if not i.isdigit()])

                            # Get day and year
                            getdate = list(map(int, getdate.groups()))

                            # Set month name as integer
                            for k, v in self.replacemonth.items():
                                if k in gm:
                                    gm = gm.replace(k, v)

                            # Set month name, day of the month and year
                            mnthname = int(gm)
                            daymnth = getdate[0]
                            year = getdate[-1]

                            # Check
                            if daymnth > 31 or daymnth < 0 or mnthname == '' or year == '':
                                pass
                            
                            # Append
                            else:
                                # Append day and month to lists
                                self.days.append(daymnth)
                                self.months.append(mnthname)
                                self.years.append(year)           

                        # <month name>, <day>
                        if getdate == None:
                            getdate = re.search(fr'(?:{j})\s*(\d{{1,2}})\b', self.inp)

                            # Get month name
                            gm = getdate.group().split()
                            gm = ''.join([i for i in gm if not i.isdigit()])

                            # Get day and year
                            getdate = list(map(int, getdate.groups()))

                            # Set month name as integer
                            for k, v in self.replacemonth.items():
                                if k in gm:
                                    gm = gm.replace(k, v)

                            # Set month name, day of the month and year
                            mnthname = int(gm)
                            daymnth = getdate[0]

                            # Check
                            if daymnth > 31 or daymnth < 0 or mnthname == '':
                                pass
                            
                            # Append
                            else:
                                # Append day and month to lists
                                self.days.append(daymnth)
                                self.months.append(mnthname)

                    except:
                        # <day>, <month name>, <year>
                        getdate = re.search(fr'\b(\d{{1,2}})\s*(?:{j})\s*(\d{{4}})', self.inp)

                        if getdate:
                            
                            # Get month name
                            gm = getdate.group().split()
                            gm = ''.join([i for i in gm if not i.isdigit()])

                            # Get day and year
                            getdate = list(map(int, getdate.groups()))

                            # Set month name as integer
                            for k, v in self.replacemonth.items():
                                if k in gm:
                                    gm = gm.replace(k, v)

                            # Set month name, day of the month and year
                            mnthname = int(gm)
                            daymnth = getdate[0]
                            year = getdate[-1]

                            # Check
                            if daymnth > 31 or daymnth < 0 or mnthname == '' or year == '':
                                pass
                            
                            # Append
                            else:
                                # Append day and month to lists
                                self.days.append(daymnth)
                                self.months.append(mnthname)
                                self.years.append(year)

                        # <day>, <month name>
                        if getdate == None:
                            getdate = re.search(fr'\b(\d{{1,2}})\s*(?:{j})', self.inp)

                            # Get month name
                            gm = getdate.group().split()
                            gm = ''.join([i for i in gm if not i.isdigit()])

                            # Get day and year
                            getdate = list(map(int, getdate.groups()))

                            # Set month name as integer
                            for k, v in self.replacemonth.items():
                                if k in gm:
                                    gm = gm.replace(k, v)

                            # Set month name, day of the month and year
                            mnthname = int(gm)
                            daymnth = getdate[0]

                            # Check
                            if daymnth > 31 or daymnth < 0 or mnthname == '':
                                pass
                            
                            # Append
                            else:
                                # Append day and month to lists
                                self.days.append(daymnth)
                                self.months.append(mnthname)   

                except:
                    pass

            # For 'next'
            if any(ne for ne in self.next if ne in self.inp):

                try:
                    # Get day name from sentence
                    k = "|".join(map(re.escape, self.next))
                    ka = "|".join(map(re.escape, self.daynames))
                    getdate = re.search(fr'({k})\s*({ka})\b', self.inp)
                     
                    # Next <day name>
                    if getdate:
                        getdate = list(map(str, getdate.groups()))
                    else:
                        pass

                    # Set day name as pendulum object
                    for k, v in self.replacedaynames.items():
                        if k in getdate:
                            getdate[1] = getdate[1].replace(k, str(v))

                    # Append
                    self.days = []
                    self.months = []
                    self.years = []

                    self.years.append(pendulum.now().next(int(getdate[1])).strftime('%Y'))
                    self.months.append(pendulum.now().next(int(getdate[1])).strftime('%m'))
                    self.days.append(pendulum.now().next(int(getdate[1])).strftime('%d'))

                except:
                    pass

            # For 'on'
            if any(on for on in self.on if on in self.inp):

                try:
                    # Get day name from sentence
                    l = "|".join(map(re.escape, self.on))
                    la = "|".join(map(re.escape, self.daynames))
                    getdate = re.search(fr'({l})\s*({la})\b', self.inp)
                     
                    # Next <day name>
                    if getdate:
                        getdate = list(map(str, getdate.groups()))
                    else:
                        pass

                    # Set day name as pendulum object
                    for k, v in self.replacedaynames.items():
                        if k in getdate:
                            getdate[1] = getdate[1].replace(k, str(v))

                    # Append
                    self.days = []
                    self.months = []
                    self.years = []

                    self.years.append(pendulum.now().next(int(getdate[1])).strftime('%Y'))
                    self.months.append(pendulum.now().next(int(getdate[1])).strftime('%m'))
                    self.days.append(pendulum.now().next(int(getdate[1])).strftime('%d'))

                except:
                    pass

            # For 'today'
            if any(to for to in self.qtoday if to in self.inp):

                try:
                    self.days = []
                    self.months = []
                    self.years = []

                    self.years.append(pendulum.now(self.timezone['timezone']).strftime('%Y'))
                    self.months.append(pendulum.now(self.timezone['timezone']).strftime('%m'))
                    self.days.append(pendulum.now(self.timezone['timezone']).strftime('%d'))

                except:
                    pass

            # For 'tomorrow'
            if any(tm for tm in self.qtomorrow if tm in self.inp):

                try:
                    self.adddays.append(1)

                except:
                    pass

            # For 'overmorrow'
            if any(tm for tm in self.qovermorrow if tm in self.inp):

                try:
                    self.adddays.append(2)

                except:
                    pass

            # For 'next week'
            if any(nw for nw in self.nweek if nw in self.inp):

                try:
                    self.addweeks.append(1)

                except:
                    pass

            # For 'next month'
            if any(nm for nm in self.nmonth if nm in self.inp):

                try:
                    self.addmonths.append(1)

                except:
                    pass

            # For 'next year'
            if any(ny for ny in self.nyear if ny in self.inp):

                try:
                    self.addyears.append(1)

                except:
                    pass

            # For 'day(s) later'
            if any(dl for dl in self.day if dl in self.inp):

                try:
                    # Get day from sentence
                    m = "|".join(map(re.escape, self.day))
                    getdate = re.search(fr'\b(\d{{1,9}}(?:\.\d+)?)\s*(?:{m})', self.inp)
                    if getdate:
                        getdate = list(map(float, getdate.groups()))

                    # Get day
                    day = getdate[0]

                    # Append day to list
                    self.adddays.append(day)

                except:
                    pass   

            # For 'week(s) later'
            if any(we for we in self.week if we in self.inp):

                try:
                    # Get week from sentence
                    o = "|".join(map(re.escape, self.week))
                    getdate = re.search(fr'\b(\d{{1,9}}(?:\.\d+)?)\s*(?:{o})', self.inp)
                    if getdate:
                        getdate = list(map(float, getdate.groups()))

                    # Get week
                    week = getdate[0]
                    
                    # Append week to list
                    self.addweeks.append(week)

                except:
                    pass    

            # For 'month(s) later'
            if any(mn for mn in self.lmonth if mn in self.inp):

                try:
                    # Get month from sentence
                    q = "|".join(map(re.escape, self.lmonth))
                    getdate = re.search(fr'\b(\d{{1,9}}(?:\.\d+)?)\s*(?:{q})', self.inp)
                    if getdate:
                        getdate = list(map(float, getdate.groups()))

                    # Get month
                    month = getdate[0]

                    # Append month to list
                    self.addmonths.append(month)

                except:
                    pass

            # For 'year(s) later'
            if any(ye for ye in self.year if ye in self.inp):

                try:
                    # Get year from sentence
                    s = "|".join(map(re.escape, self.year))
                    getdate = re.search(fr'\b(\d{{1,9}}(?:\.\d+)?)\s*(?:{s})', self.inp)
                    if getdate:
                        getdate = list(map(float, getdate.groups()))

                    # Get year
                    year = getdate[0]
                    
                    # Append year to list
                    self.addyears.append(year)

                except:
                    pass
        except:
            pass

    # Find time words from input
    def findTimeWords(self):

        """
        This module finds time from given input.
        Inputs should be:

        # If time is exact:

        -> 5 o'clock, 20 o'clock
        -> 5 a.m., am, ante meridiem
        -> 5 p.m., pm, post meridiem
        -> at 5, at 17, at 23:45, at 11:20

        # If time isn't exact and contains 'later, in' etc. add to the current time:

        -> 5 seconds later, 1.5 secs later, 5 secs after
        -> 5 minutes later, 1.5 mins later, 5 mins after
        -> 5 hours later, 1.5 hrs later, 5 hrs after
        -> in 5 seconds, in 1.5 hours, in 2.5 mins
        """

        try:

            # Time words
            self.mtime = ['o\'clock', 'o clock', 'oclock']

            self.am = ['a.m.', 'am', 'ante meridiem']
            self.pm = ['p.m.', 'pm', 'post meridiem']

            self.second = ['seconds', 'second', 'secs', 'sec', 'seconds later', 'second later', 'seconds after', 'second after', "sec later", "secs later", "sec after", "secs after"]
            self.insecond = ['second', 'seconds', 'sec', 'secs']
            
            self.minute = ['minutes', 'minute', 'mins', 'min', 'minutes later', 'minute later', 'minutes after', 'minute after', "min later", "mins later", "min after", "mins after"]
            self.inminute = ['minute', 'minutes', 'min', 'mins']

            self.hour = ['hours', 'hour', 'hr', 'hrs', 'hours later', 'hour later', 'hours after', 'hour after', 'hr later', 'hrs later', 'hr after', 'hrs after']
            self.inhour = ['hour', 'hours', 'hr', 'hrs']

            # For exact times
            self.hours = []
            self.minutes = []

            # For adding time to current time
            self.addhours = []
            self.addminutes = []
            self.addseconds = []

            # For 'mtime'
            if any(mt for mt in self.mtime if mt in self.inp):

                try:

                    # Get hour from sentence
                    a = "|".join(map(re.escape, self.mtime))
                    gettime = re.search(fr'\b(\d{{1,2}})\s*(?:{a})', self.inp)                    
                    if gettime:
                        gettime = list(map(int, gettime.groups()))

                    # Set hour
                    hrs = gettime[0]
                    mins = 0
                    
                    # Check
                    if hrs > 24 or hrs < 0:
                        pass

                    else:
                        self.hours.append(hrs)
                        self.minutes.append(mins)


                except:
                    pass

            # For 'a.m.'
            if any(am for am in self.am if am in self.inp):

                try:

                    # Get a.m. hour from sentence (format hh:mm)
                    b = "|".join(map(re.escape, self.am))
                    gettime = re.search(fr'\b(\d{{1,2}}):(\d{{2}})\s*(?:{b})', self.inp)
                    if gettime:
                        gettime = list(map(int, gettime.groups()))

                    # If format not in hh:mm
                    if gettime == None:
                        gettime = re.search(fr'\b(\d{{1,2}}) (\d{{1,2}})\s*(?:{b})', self.inp)
                        if gettime:
                            gettime = list(map(int, gettime.groups()))
                        else:
                            gettime = re.search(fr'\b(\d{{1,2}})\s*(?:{b})', self.inp)                    
                            if gettime:
                                gettime = list(map(int, gettime.groups()))

                                # Set hour
                                hrs = gettime[0]
                                mins = 0
                                
                                # Check
                                if hrs > 12 or hrs < 0:
                                    pass
                                elif hrs == 24:
                                    hrs = 0
                                else:
                                    self.hours.append(hrs)
                                    self.minutes.append(mins)

                    # Append it in hour and minute list
                    hrs = gettime[0]
                    mins = gettime[1]

                    # Check
                    if hrs > 12 or hrs < 0:
                        pass

                    if mins > 60 or mins < 0:
                        pass
                    
                    else:
                        self.hours.append(hrs)
                        self.minutes.append(mins)

                except:
                    pass

            # For 'p.m.'
            if any(pm for pm in self.pm if pm in self.inp):

                try:

                    # Get p.m. hour from sentence (format hh:mm)
                    c = "|".join(map(re.escape, self.pm))
                    gettime = re.search(fr'\b(\d{{1,2}}):(\d{{2}})\s*(?:{c})', self.inp)
                    if gettime:
                        gettime = list(map(int, gettime.groups()))

                    # If format not in hh:mm
                    if gettime == None:
                        gettime = re.search(fr'\b(\d{{1,2}}) (\d{{1,2}})\s*(?:{c})', self.inp)
                        if gettime:
                            gettime = list(map(int, gettime.groups()))
                        else:
                            gettime = re.search(fr'\b(\d{{1,2}})\s*(?:{c})', self.inp)                    
                            if gettime:
                                gettime = list(map(int, gettime.groups()))

                                # Set hour
                                hrs = gettime[0] + 12
                                mins = 0
                                
                                # Check
                                if hrs == 12:
                                    hrs = 0
                                elif hrs > 24 or hrs < 0:
                                    pass
                                else:
                                    self.hours.append(hrs)
                                    self.minutes.append(mins)

                    # Append it in hour and minute list
                    hrs = gettime[0] + 12
                    mins = gettime[1]

                    # Check
                    if hrs == 12:
                        hrs = 0
                    
                    if hrs > 24 or hrs < 0:
                        pass

                    if mins > 60 or mins < 0:
                        pass

                    else:
                        self.hours.append(hrs)
                        self.minutes.append(mins)

                except:
                    pass

            # For 'hour(s) later'
            if any(hl for hl in self.hour if hl in self.inp):

                try:

                    # Get hour from sentence
                    d = "|".join(map(re.escape, self.hour))
                    gettime = re.search(fr'\b(\d{{1,9}}(?:\.\d+)?)\s*(?:{d})', self.inp)
                    if gettime:
                        gettime = list(map(float, gettime.groups()))

                    # Get hour
                    hrs = gettime[0]
                    
                    # Append hrs to list
                    self.addhours.append(hrs)

                except:
                    pass

            # For 'in <hrs> hour(s)'
            if any(hi for hi in self.inhour if hi in self.inp):

                try:

                    # Get hour from sentence
                    e = "|".join(map(re.escape, self.inhour))
                    gettime = re.search(fr'in \b(\d{{1,9}}(?:\.\d+)?)\s*(?:{e})', self.inp)                    
                    if gettime:
                        gettime = list(map(float, gettime.groups()))

                    # Get hour
                    hrs = gettime[0]
                    
                    # Append hrs to list
                    self.addhours.append(hrs)

                except:
                    pass

            # For 'minute(s) later'
            if any(ml for ml in self.minute if ml in self.inp):

                try:

                    # Get minute from sentence
                    f = "|".join(map(re.escape, self.minute))
                    gettime = re.search(fr'\b(\d{{1,9}}(?:\.\d+)?)\s*(?:{f})', self.inp)                    
                    if gettime:
                        gettime = list(map(float, gettime.groups()))

                    # Get minute
                    mins = gettime[0]
                    
                    # Append mins to list
                    self.addminutes.append(mins)

                except:
                    pass

            # For 'in <min> minute(s)'
            if any(mi for mi in self.inminute if mi in self.inp):

                try:

                    # Get minute from sentence
                    g = "|".join(map(re.escape, self.inminute))
                    gettime = re.search(fr'in \b(\d{{1,9}}(?:\.\d+)?)\s*(?:{g})', self.inp)                    
                    if gettime:
                        gettime = list(map(float, gettime.groups()))

                    # Get minute
                    mins = gettime[0]
                    
                    # Append mins to list
                    self.addminutes.append(mins)

                except:
                    pass

            # For 'second(s) later'
            if any(sl for sl in self.second if sl in self.inp):

                try:

                    # Get second from sentence
                    h = "|".join(map(re.escape, self.second))
                    gettime = re.search(fr'\b(\d{{1,9}}(?:\.\d+)?)\s*(?:{h})', self.inp)                    
                    if gettime:
                        gettime = list(map(float, gettime.groups()))

                    # Get second
                    scs = gettime[0]           

                    # Append scs to list
                    self.addseconds.append(scs)

                except:
                    pass

            # For 'in <sec> second(s)'
            if any(si for si in self.insecond if si in self.inp):

                try:

                    # Get second from sentence
                    i = "|".join(map(re.escape, self.insecond))
                    gettime = re.search(fr'in \b(\d{{1,9}}(?:\.\d+)?)\s*(?:{i})', self.inp)                    
                    if gettime:
                        gettime = list(map(float, gettime.groups()))

                    # Get second
                    scs = gettime[0]
                    
                    # Append scs to list
                    self.addseconds.append(scs)

                except:
                    pass

            # If no exact time match
            if self.hours == [] and self.minutes == []:

                # If there's match with add time
                if self.addhours != [] or self.addminutes != [] or self.addseconds != []:
                    pass

                # If not
                else:
                    try:

                        # Get time from sentence in hh:mm format
                        gettime = re.search(fr'\b(\d{{1,2}}):(\d{{2}})', self.inp)
                        if gettime:
                            gettime = list(map(int, gettime.groups()))

                            # Set hour
                            hrs = gettime[0]
                            mins = gettime[1]

                            # Check
                            if hrs > 24 or hrs < 0:
                                pass
                            if mins > 60 or mins < 0:
                                pass
                            else:
                                # Append hrs and mins to list
                                self.hours.append(hrs)
                                self.minutes.append(mins)
                       
                        # Get time from sentence in hh mm format
                        if gettime == None:
                            gettime = re.search(fr'\b(\d{{1,2}}) (\d{{2}})\b', self.inp)
                            gettime = list(map(int, gettime.groups()))

                            # Set hour
                            hrs = gettime[0]
                            mins = gettime[1]

                            # Check
                            if hrs > 24 or hrs < 0:
                                pass
                            if mins > 60 or mins < 0:
                                pass
                            else:
                                # Append hrs and mins to list
                                self.hours.append(hrs)
                                self.minutes.append(mins)

                    except:
                        pass
        except:
            pass

    def checkDate(self):

        """
        This method edits output of date & time.
        
        If date and time outputs are empty, raise error message and pass.

        If date or time output comes from exact output,
        Choose the one at the end of the list, and set as result.
        Check the setted results using current date as reference point.

        If date or time output comes from date add output,
        Get sum of the numbers, and set as result.
        Check the setted results using current date as reference point.

        If outputs at the previous time and date.
        Raise error message, pass

        If time output is less than 3 minutes from current time.
        Raise error message, pass
        """

        try:

            # Call methods
            self.findDateWords()
            self.findTimeWords()

            # Get current date
            self.currentday = int(datetime.datetime.now().replace(tzinfo = self.local_tz).strftime('%d'))
            self.currentmonth = int(datetime.datetime.now().replace(tzinfo = self.local_tz).strftime('%m'))
            self.currentyear = int(datetime.datetime.now().replace(tzinfo = self.local_tz).strftime('%Y'))

            # Get current time
            self.currenthour = int(datetime.datetime.now().replace(tzinfo = self.local_tz).strftime('%H'))
            self.currentminute = int(datetime.datetime.now().replace(tzinfo = self.local_tz).strftime('%M'))

            # Current date & time
            self.currentdate = datetime.datetime.now().replace(tzinfo = self.local_tz)

            # Set boolean for time and year
            self.bool = False
            self.ybool = False

            # Check if the lists are empty

            if self.hours == [] and self.minutes == []:
                if self.addhours == [] and self.addminutes == [] and self.addseconds == []:
                    if self.days == [] and self.months == [] and self.years == []:
                        if self.adddays == [] and self.addweeks == [] and self.addmonths == [] and self.addyears == []:
                            raise NameError

            # DATE ADD OUTPUT CHECK

            # Add time check
            if self.addhours != []:
                self.addhours = sum(self.addhours)
            else:
                self.addhours = 0

            if self.addminutes != []:
                self.addminutes = sum(self.addminutes)
            else:
                self.addminutes = 0

            if self.addseconds != []:
                self.addseconds = sum(self.addseconds)
            else:
                self.addseconds = 0
                
            # Add date check
            if self.adddays != []:
                self.adddays = sum(self.adddays)
            else:
                self.adddays = 0
                
            if self.addweeks != []:
                self.addweeks = sum(self.addweeks)
            else:
                self.addweeks = 0
                
            if self.addmonths != []:
                self.addmonths = sum(self.addmonths)
            else:
                self.addmonths = 0
                
            if self.addyears != []:
                self.addyears = sum(self.addyears)
            else:
                self.addyears = 0
                
            # Check if getdate already has a date
            self.getdate = self.currentdate + relativedelta(years = self.addyears, months = self.addmonths, weeks=self.addweeks, days = self.adddays, 
                                                                    hours = self.addhours, minutes = self.addminutes, seconds = self.addseconds)

            # EXACT OUTPUT CHECK

            # Time check
            if self.hours != []:
                self.hours = self.hours[-1]
            else:
                if isinstance(self.getdate, datetime.datetime):
                    if self.getdate == self.currentdate:
                        self.hours = int(self.currentdate.strftime('%H'))
                    else:
                        self.bool = True

            if self.minutes != []:
                self.minutes = self.minutes[-1]
            else:
                if isinstance(self.getdate, datetime.datetime):
                    if self.getdate == self.currentdate:
                        self.minutes = int(self.currentdate.strftime('%M'))
                    else:
                        self.bool = True

            # Date check
            if self.days != []:
                self.days = int(self.days[-1])
            else:
                if self.getdate != '':
                    self.days = int(self.getdate.strftime('%d'))
                else:
                    self.days = self.currentday

            if self.months != []:
                self.months = int(self.months[-1])
            else:
                if self.getdate != '':
                    self.months = int(self.getdate.strftime('%m'))
                else:
                    self.months = self.currentmonth
            
            if self.years != []:
                self.years = int(self.years[-1])
                if self.years < self.currentyear:
                    self.ybool = True
            else:
                if self.getdate != '':
                    self.years = int(self.getdate.strftime('%Y'))
                else:
                    self.years = self.currentyear

            # Empty time check
            if self.bool == False:
                # Set temporary date
                tempdate = datetime.datetime(self.years, self.months, self.days, self.hours, self.minutes, int(self.currentdate.strftime('%S')), int(self.currentdate.strftime('%f'))).replace(tzinfo = self.local_tz)

                # Set the variables
                self.hours = int(tempdate.strftime('%H'))
                self.minutes = int(tempdate.strftime('%M'))
                self.days = int(tempdate.strftime('%d'))
                self.months = int(tempdate.strftime('%m'))
                self.years = int(tempdate.strftime('%Y'))

                # Set variables as a date
                self.getdate = datetime.datetime(self.years, self.months, self.days, self.hours, self.minutes, tzinfo=self.local_tz)

            # Print datetime object if everything is True
            if self.getdate != '':
                print(self.getdate)

        except:
            print(random.choice(self.error))
            pass
