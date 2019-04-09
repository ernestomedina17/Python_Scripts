#!/usr/bin/python

### This scripts reads 4 files with a single column of int numbers and adds them and write them into a file.
### Requirement, the 4 should have the same amount of lines

logfile01 = open("Report_01.txt", 'r')
logfile02 = open("Report_02.txt", 'r')
logfile03 = open("Report_03.txt", 'r')
logfile04 = open("Report_04.txt", 'r')

report = open('Report_Aggregated.txt', 'w+r')

### Lines Validation
num_line01 = sum(1 for line in logfile01)
num_line02 = sum(1 for line in logfile02)
num_line03 = sum(1 for line in logfile03)
num_line04 = sum(1 for line in logfile04)

if ( num_line01 == num_line02 and num_line01 == num_line03 and num_line01 == num_line04 ):
    print("The file's lines matches")
else:
    print("The file's lines do not match, check your stuff")

logfile01.seek(0)
logfile02.seek(0)
logfile03.seek(0)
logfile04.seek(0)

for var in range(num_line01):
    report.write(str(int(logfile01.readline()) + int(logfile02.readline()) + int(logfile03.readline()) + int(logfile04.readline())) + "\n")

logfile01.close()
logfile02.close()
logfile03.close()
logfile04.close()

report.seek(0)

if ( sum(1 for line in report) == num_line01 ):
    print("done")
else:
    print("error, something is wrong, what are you doing")

report.close()
