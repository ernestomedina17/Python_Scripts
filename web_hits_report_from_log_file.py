#!/usr/bin/python 

from datetime import date, timedelta

### This scripts counts the lines of a single and big log file matching a datetime(E.g. Format 12/31/2018) day from a hole year 
### And creates a report with the following format: mm/dd/yyyy, count, log-file-name
### This assumens you have removed unwanted lines from the log, like crawlers, security scans, monitoring tools, etc.
### And also it assumes the log is in your current work dir

d1 = date(2018, 1, 1)	# start date
d2 = date(2018, 12, 31) # end date

delta = d2 - d1         # timedelta, 

logfilename = "REPLACEME.log"
logfile = open(logfilename, 'r').read()
report = open('report.txt', 'w')

for i in range(delta.days + 1):
	regexlist = str(d1 + timedelta(i)).replace("-","/").split("/")
	regexstring = regexlist[1] + "/" + regexlist[2] + "/" + regexlist[0]
	count = logfile.count(regexstring)	
	report.write( regexstring + ", " + str(count) + ", Server:/path/to/file/" + logfilename + "\n")

report.close()
