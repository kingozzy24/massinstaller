# massinstaller
* MASS library plugin for starcluster * 

# Usage
The MASS installer will add the correct exports to the bash profile
so it is unnecessary to perform exports by hand.

There is an additional `setup` function in the bash profile which will make symbolic 
links to the killMProcess.sh and mprocess files inside of the mass library which are necissary 
for operation. 

The MASS library will always be install under /home/MASS as of 6/12/2015 only the c++ version of the library
is supported by the installer.

# Before using MASS
Starcluster creates passwordless ssh credentials on all nodes inside of a cluster. Because mass expects
the username and password of the user to be entered at the start of execution the library will need to be modified.

in the Utilities.h file under /home/MASS/source the values of keyfile1 and keyfile2 need to be absolute paths instead of using the ~/ to get the
ssh credentials of the current user. This will typically resolve to /root so the values would become 

```
	keyfile1 /root/.ssh/id_rsa.pub  keyfile2 /root/.ssh/id_rsa
```

##Configuration
[plugin MASSInstaller]
setup_class = MASSInstaller.MASSInstaller
username = bit bucket username
password = bit bucket password
version = cpp
