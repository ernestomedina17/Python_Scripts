#!/usr/bin/python

## Script written by Ernesto Medina - Jan 30 2019
## The purpose of this script is to zero log and rotated files to save space 
## in non prod envs, it will not delete the files, so the rotation can continue BAU

from os import walk, statvfs
from os.path import join

logdirs = [ 
"/opt/app/name/dirA",
"/opt/app/name/dirB",
"/opt/app/name/dirC",
]

FILE_SYSTEM = "/opt/app/name"

### Get FS usage 
BLOCK_SIZE = statvfs(FILE_SYSTEM).f_bsize
BEFORE_BAVAIL = statvfs(FILE_SYSTEM).f_bavail

### Walk the directories and list the files
for VAR in sorted(logdirs):
   for root, dirs, files in walk(VAR):
      try:
         for name in files:
            with open(join(root,name), "w") as logfile:
               logfile = ""
      except IOError as e:
         print "I/O error({0}): {1}".format(e.errno, e.strerror)

### Get FS usage 
AFTER_BAVAIL = statvfs(FILE_SYSTEM).f_bavail

print("\n")
print("---------------------------------------------------------------------------------------")
TOTAL_REMOVED = AFTER_BAVAIL - BEFORE_BAVAIL
print("TOTAL FREED SPACE: " + str(TOTAL_REMOVED * BLOCK_SIZE / 1024 / 1024) + " MB")
print("\n") 
