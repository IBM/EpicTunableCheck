EpicTunableCheck.py3 is a python script used to check the settings of various AIX/Power tunables to ensure they meet IBM and Epic recommendations for the Epic Operational Database.

There are several components to the script, as well as OS requirements for executing it.

Components
EpicTunableCheck.py3 is the master script that sets up an output file, reads in the file named Epic_Tunables_Datafile, and executes commands in that file.

Epic_Tunables_Datafile is the file that contains the tunable names and the commands to check the existing settings of the tunables.

Epic_Tunables_Output.Date-Time is the output file format.

OS requirements
python3 must be loaded on the system where the script will be run.

This script has been tested with the latest version of AIX. If you are running an earlier version of AIX, the script may not output the current tunable settings accurately.

This script should be executed by a non-root user via the RBAC facility on your server. This will ensure that no adverse effects occur. It requires 3 authorizations to be added to a new user role. To set up RBAC, follow these steps:

CREATE A ROLE
# mkrole dfltmsg="display tunable" authorizations="aix.system.tune.display,aix.system.stat,aix.security.user.list" display_role

UPDATE THE KERNEL TABLES WITH THIS NEW ROLE
# setkst

ASSIGN THE ROLE TO THE USER
# chuser roles=display_role <user name> 

LOGIN TO USER AND SWITCH TO THE ROLE
# swrole display_role

Now you can execute the script with the proper authorizations to display the current tunables settings.
# python3 EpicTunableCheck.py3

The script will prompt you for the full path to your irisdb file and for the names of your Epic Volume Groups.

To check the current tunable settings against Epic recommended settings, download the document at this link:

https://galaxy.epic.com/Redirect.aspx?DocumentID=2220736

