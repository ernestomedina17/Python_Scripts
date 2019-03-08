#!/usr/bin/python
import commands
import getpass 
import os
import difflib
import argparse
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Functions:
def list(args):
    if args.dev:
        os.system('/usr/bin/spacecmd -u ' + args.user + ' -p \'' + askPass() + '\' "softwarechannel_list archive*dev*"')
    elif args.qa:
        os.system('/usr/bin/spacecmd -u ' + args.user + ' -p \'' + askPass() + '\' "softwarechannel_list archive*qa*"')
    elif args.prod:
        os.system('/usr/bin/spacecmd -u ' + args.user + ' -p \'' + askPass() + '\' "softwarechannel_list archive*prod*"')
    else:
        os.system('/usr/bin/spacecmd -u ' + args.user + ' -p \'' + askPass() + '\' softwarechannel_list')

def diff(args):
    password = askPass() 
    print("collecting info from channel a...")
    outputa = commands.getoutput('/usr/bin/spacecmd -u ' + args.user + ' -p \'' + password + '\' softwarechannel_listallpackages ' + args.channel_a + ' 2>&1 ')
    print("collecting info from channel b...")
    outputb = commands.getoutput('/usr/bin/spacecmd -u ' + args.user + ' -p \'' + password + '\' softwarechannel_listallpackages ' + args.channel_b + ' 2>&1 ')
    print("generating html report...")
    htmlreport = difflib.HtmlDiff().make_file(outputa, outputb, context=True)
    print("sending email...")
    sendReport(args, htmlreport)
    
    if args.output: 
       print(htmlreport) 
        

def askPass():
    password = getpass.getpass(prompt="What's your spacewalk password? ") 
    return password
    
def print_subHelp(parser_list, parser_diff):
    if len(sys.argv) == 1:
        parser_list.print_help()
        print("")
        parser_diff.print_help()
        print("")
   
def sendReport(args, htmlreport):
    senderemail = "root"
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "SpaceWalk channel package report"
    msg['From'] = senderemail
    msg['To'] = args.email
    text = "This is the text report, HTML format is preferred\n"
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(htmlreport, 'html')
    msg.attach(part1)
    msg.attach(part2)
    s = smtplib.SMTP('localhost')
    s.sendmail(senderemail, args.email, msg.as_string())
    s.quit()
    #postconf -e 'message_size_limit = 104857600' 

# Main Function
def main():
    parser = argparse.ArgumentParser(description = "For extended help select a positional argument {list|diff} plus {-h|--help} ")
    subparsers = parser.add_subparsers()

    parser_list = subparsers.add_parser('list', help="List the channels in spacewalk")
    parser_list.add_argument('-u', "--user", required=True, help="Spacewalk user name is mandatody")
    parser_list.add_argument('-d', '--dev',  action='store_true', help="List only channel archives from DEV")
    parser_list.add_argument('-q', '--qa',   action='store_true', help="List only channel archives from QA")
    parser_list.add_argument('-p', '--prod', action='store_true', help="List only channel archives from PROD")
    parser_list.set_defaults(func=list)

    parser_diff = subparsers.add_parser('diff', help="Compare two channels in spacewalk")
    parser_diff.add_argument('-u', "--user", required=True, help="Spacewalk user name is mandatody")
    parser_diff.add_argument('-e', "--email", required=True, help="Your email address is required to send the report")
    parser_diff.add_argument('-a', "--channel-a", required=True, help="Name of the channel A")
    parser_diff.add_argument('-b', "--channel-b", required=True, help="Name of the channel B")
    parser_diff.add_argument('-o', "--output", action='store_true',  help="Prints the HTML report to the standard output")
    parser_diff.set_defaults(func=diff)

    print_subHelp(parser_list, parser_diff)
    args = parser.parse_args()
    args.func(args)
    

# Execute
if __name__ == "__main__":
    main()
