# This Python script checks the values of multiple tunable parameters
# and compares them against current recommended settings from IBM and Epic
# for Epic Applications running on IBM AIX servers.

# Script logic:
# The script takes a list of tunable parameter names, values, and commands
# to check those values as input.

# It runs each command and outputs the current value and the expected value per
# parameter.

import sys, os, subprocess, configparser, datetime
FileExt = datetime.datetime.now().strftime("%m%d%Y-%H%M%S")
filename = "Epic_Tunables_Output." + FileExt

with open('./Epic_Tunables_Datafile', 'r') as ins:
        HC_List = [[n for n in line.split(", ", -1)] for line in ins]
f = open(filename, "w")
for i in range(0, len(HC_List)):
        f.write("For Tunable Parameter: " + HC_List[i][0])
        f.write("\n")
        f.write("Recommended Setting is: " + HC_List[i][1])
        f.write("\n")
        while True:
              try:
                   tunset = (str((subprocess.check_output(HC_List[i][2].strip(), shell=True, universal_newlines=True))))
       	           f.write("Current Setting is: " + tunset)
                   break
              except BaseException: 
                   print("This parameter is not set")
        f.write("\n\n")
f.close()
