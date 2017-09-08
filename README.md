eventviewer.py info

Eventviewer purpose:
This script parses windows event logs from windows 7 and up
with the extension .evtx 
It outputs the file to a terminal and also to a text file called
'win_eventlog.txt'

Requirements:
python-evtx obtainable through pip:
sudo pip install python-evtx
Or it can also be compiled from the code at - 
	https://github.com/williballenthin/python-evtx


Usage:
python eventviewer.py log_file
	
This script parses windows event logs from windows 7 and up
with the extension .evtx. It outputs the file to a terminal 
and also to a text file called 'win_eventlog.xml’ when run
with admin privileges

Tips:
Create an alias for the script in bash so it can be run with a 
single command, instead of typing ‘python /Users/billy/python_scripts/eventviewer.py’
each time. To do this on Mac perform the following steps - 
	
	1. Open a terminal in your home directory (you can get 
	there with just ‘cd’ and press return)
	2. Open the file ‘.bash_profile’ with an editor such as
	‘nano’
	3. Add the following line to the file WITHOUT spaces 
	between the command name, the = sign or the true command - 
		alias <your command>=‘python <path to script>’
	Example - 
		alias eventviewer=‘python /Users/billy/python_scripts/eventviewer.py’
	4. Save the file and exit (with nano press ‘control + o’ 
	to save and ‘control + x’ to exit
	5. Refresh the bash shell environment with the following command - 
		‘source ~/.bash_profile’
	6. Test your new command
	**Note if you move the script the nan file will need to be edited to reflect
	the change.	

Notes on PIP:
PIP is an installer used by python to install 3rd party libraries.
It normally does not come with python by default. To install pip 
run the following commands - sudo easy_install pip

Troubleshooting:
On Mac OS sometimes pip will fail installing packages. Try the 
following to resolve - 

1. Make sure python 2.7.13 is installed. If not install it from - 
	https://www.python.org/downloads/
   Close and re-open your terminal and try again.
2. Remove the old version of python with - 
   	sudo rm -R /System/Library/Frameworks/Python.framework/Versions/2.7
   Close and re-open your terminal and try again.
3. Move the new installation with - 
   	sudo mv /Library/Frameworks/Python.framework/Versions/2.7 /System/Library/Frameworks/Python.framework/Versions	
   Close and re-open your terminal and try again.
4. For more steps see your friendly neighborhood search engine!

For more information about python-evtx see - 
	https://github.com/williballenthin/python-evtx
