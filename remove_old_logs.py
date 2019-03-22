#!/usr/bin/python

## Script written by Ernesto Medina - Mar 22 2019
## The purpose of this script is to remove server logs with a change time (ctime) greather than 180 days 

from os import walk, remove
from os.path import join, getctime, getatime, getmtime
from re import compile 
from time import time 

# Global Variables 
BASE_DIR = "/SOME/DIRECTORY/PATH"
FILE_NAME_PATTERN = compile("^server_20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]\.log$")
## time() returns seconds since the Epoch "January 1, 1970"
EXPIRY_TIME = time() - 15552000 ## 180 days expressed in seconds

# Functions 
def find_log_dirs():
	logdirs = [] 
	for root, dirs, files in walk(BASE_DIR):
		try:
			for dname in dirs:
				if dname == "logs":
					logdirs.append(join(root, dname))
		except IOError as e:
			print "I/O error({0}): {1}".format(e.errno, e.strerror)
	return logdirs

def find_old_files(logdirs):
	logfiles = []
	for logdir in logdirs: 
		for root, dirs, files in walk(logdir):
			try:
				for fname in files:
					absolute_fname = join(root, fname)
					if FILE_NAME_PATTERN.match(fname) and getctime(absolute_fname) < EXPIRY_TIME:
						logfiles.append(absolute_fname)
			except IOError as e:
				print "I/O error({0}): {1}".format(e.errno, e.strerror)
			except OSError as e:
				print "OS  error({0}): {1}".format(e.errno, e.strerror)
	return logfiles

# Main Function
def main():
	logdirs  = find_log_dirs()
	logfiles = find_old_files(logdirs)
	for file in logfiles:
		#print(file)
		remove(file)

# Execute
if __name__ == "__main__":
    main()

