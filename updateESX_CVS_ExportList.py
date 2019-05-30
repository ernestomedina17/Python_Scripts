#!/bin/python
### Update a CSV file generated from vCenter with additional details of PoweredOff VMs
### This script is meant to be run in a ESX Host

import csv
import os
import glob
import ntpath
import os.path
import time

ROOTDIR = '/vmfs/volumes/XXXXXXXXX-*'    ### DataStore locations
EXPORTLISTOFF = "ExportList_Off.csv"    ### CSV file exported from vCenter grepping "Powered Off" with fieldnames/columns shown below. 
REPORTLISTOFF = "ExportList_Off_Report.csv" ### The CSV flie updated with 2 additional columns: ['Directory','flat.vmdk Disk Last Modified']

rootdirlist = glob.glob(ROOTDIR)

with open(EXPORTLISTOFF,'r') as csvinput:   ### fieldnames=['Name','State','Used Space','Memory Size','CPUs'])
    with open(REPORTLISTOFF, 'w') as csvoutput:
        writer = csv.writer(csvoutput, lineterminator='\n')
        reader = csv.reader(csvinput)
        report = []
        ### The lines below are in case you want to update the header
        #row = next(reader)
        #row.append('Directory')
        #row.append('flat.vmdk Disk Last Modified')
        #report.append(row)
              
        for row in reader:
            for rootdir in rootdirlist:
                for root, dirs, files in os.walk(rootdir):                                                                           
                    for dirname in dirs: 
                        if dirname == row[0]:                                                                                                            
                            path = os.path.join(root, dirname)
                            row.append(path)
                            try:
                                row.append(time.ctime(os.path.getmtime(path + "/" + dirname + "-flat.vmdk")))
                            except:
                                row.append(time.ctime(os.path.getmtime(path + "/" + dirname + "_1-flat.vmdk")))
                            report.append(row)
        writer.writerows(report)

