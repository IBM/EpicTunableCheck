EpicTunableCheck.py is a python script used to check the setting of various AIX/Power tunables to ensure they meet IBM and Epic recemmendations for the Epic Operational Database.

There are several components to the script, as well as OS requirements for executing it.

Components
EpicTunableCheck.py is the master script that sets up an output file, reads in the file named Epic_Tunables_Data, and executes commands in that file.

Epic_Tunables_Data is the file that contains The tunable names, recommended settings, and the commands to check the existing settings of the tunables.

is the output file format.

OS requirements
python3 must be loaded on the system where the sctipt will be run.

This script has been tested with the latest version of AIX. If you are running an earlier version of AIX, the script may not output the current tunable settings accurately.

This script should be executed by a non-root user via the RBAC facility on your server. This will ensure that no adverse affects occur. It requires 3 authorizations to be added to a new user role. To set up RBAC, follow these steps:

CREATE A ROLE
# mkrole dfltmsg="display tunable" authorizations="aix.system.tune.display,aix.system.stat,aix.security.user.list" display_role

UPDATE THE KERNEL TABLES WITH THIS NEW ROLE
# setkst

ASSIGN THE ROLE TO THE USER
# chuser roles=display_role <user name> 

LOGIN TO USER AND SWITCH TO THE ROLE
# swrole display_role

Now you can execute the script with the proper authprizations to display the current tunables settings.
