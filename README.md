# python-manage-ssh-users

This project requires the python language and interpretor to be installed on 
the system you are using for the project. 

## Installing python

Python can be downloaded and installed via: https://www.python.org/downloads/
Before deciding to install from source, please note that many operating systems 
already have python installed by default, e.g.
Mac OS X (BSD Unix based)
Different varieties of linux OS 
(debian, ubuntu, arch, fedora, red hat, suse, etc.)
Different Unix OS (depends)

This will also depend on the relative age of the OS, but most modern 
implementations will have python installed.

Most OS that have Python installed by default will have python3 installed, but 
not all, and many will have both versions installed but default to either 
python2 or python3 as the default binary. 

it is recommended that the native package manager is used, if possible, in 
order to install python. 

e.g. 

ubuntu: apt-get or apt (ubuntu 16.04+)
suse, red hat, fedora: yum
arch: pacman
(all linux flavors will not be explored, you could discover the package
manager with google or duckduckgo)

Windows: I have heard chocolately is nice,
but check out alternatives: 
https://en.wikipedia.org/wiki/List_of_software_package_management_systems#Windows
Not to mention, one may need to manually set the path in Windows

To discover which python is installed, please use your OS's search features,
e.g.:
Linux/Unix: which <name>
Windows: use the find function or search bar or start/run 

## installing a virtualenv

### Linux
If you are using Linux/Unix and Unless you want to install the above library 
into your system python, one good 
way to keep things separated is to use a virtual environment.

In python2 this is fairly complicated for the uninitiated, and there are 
arguments for and against using python2 over python3. 
Therefore, for this project, we are using python3, 
and installing a virtualenv is trivial:

https://docs.python.org/3/library/venv.html

python3 -m venv /path/to/new/virtual/environment
source venv/bin/activate

With a modern version of python (3.7.x) the above method should work on any 
platform. 

e.g. 
cd ~/workspace
python3 -m venv manage-ssh-user
cd manage-ssh-user
source bin/activate
pip install --upgrade pip

Now you may run the script in order to create the remote ssh user. 
Instructions

To exit the virtual environment:
type: deactivate

### windows

use the above method on the CLI to install a venv

## installing parallel-ssh

In order to test and run this project, one will need to install the following:
parallel-ssh

Found at https://github.com/ParallelSSH/parallel-ssh

Assuming one has python installed, this is trivial:

pip install parallel-ssh


