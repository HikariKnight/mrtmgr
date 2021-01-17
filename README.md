# Mesh RouTer ManaGeR
A commandline tool to manage several different vendor routers in AP(Access Point) mode through ssh with private key authentication and make them act close to a mesh network over an ethernet/wired backhaul, thus avoiding vendor locking yourself.
<br>
<br>

## Disclaimer:
*This tool does not magically turn your router into a mesh router, all it does is let you manage multiple routers in AP mode or with DHCP disabled from a single command and syncronize those settings to multiple APs making it similar to a mesh router setup, I know it is not the 100% correct term, but most people understand what a mesh network is with todays marketing. <br>
If someone has a better and more correct name, I have no issues to change the project name to reflect it.*
<br>
<br>

## Information
The idea for this project came when the small business I work for (which uses Asus AiMesh with an ethernet backhaul) hit the undocumented max capacity for the AiMesh firmware (which is 10 nodes btw) where adding any more nodes would kick a working online node off the AiMesh system and later crash the whole network.
This made us think, why not just put all the routers in AP mode and manage them from our Raspberry Pi which already manage 2 older D-Link routers, this would let us overcome some of the limitations with AiMesh too, which is being locked to a singular wireless channel on our wifi as different floors have different channels being the most "optimal" channel.<br>
All we care about is having a single SSID+wifi password for the whole building with optimal channels (if possible) and an easy way to manage all 15 Access Points without vendor locking ourselves, which will be this projects primary goal.

This project is a work in progress but here are some of the known requirements and features that I know that I will be trying to code into the project.
<br>

## Usage
In order for this tool to work, you first need to make yourself an ssh-rsa private key, preferably rsa2048 or rsa4096, whichever your routers support. Then add that public key to your routers authorized keys in the Router WebUI.
Finally tell mrtmgr where it can find the private key in mrtmgr.conf and the utility can do changes to the routers from there on if it has a compatible profile for the routers.

Out of the box, there are profiles for the Asus RT-AC66U (stock firmware) and the D-Link DIR-879 (DD-WRT firmware), but you can easily write your own by doing changes in your router's WebUI and then look for those changes in the routers nvram once with "nvram show" in the routers command line and write your own profile config.

You can then just call the utility using a command like this for a single router
```
./mrtmgr --ssid 2.4ghz_wifi 5ghz_wifi --wpa-psk supersecret supersecret5ghz --commit rt66u 192.168.1.1
```

Or this for a group of routers (where it will fetch the ip addresses from a rt66u.list file in the groups folder)
```
./mrtmgr --ssid 2.4ghz_wifi 5ghz_wifi --wpa-psk supersecret supersecret5ghz --commit rt66u group=rt66u
```

### Features
* [X] Change key router settings like: WPA-PSK, WPA2-PSK, SSID
* [X] Change wireless password
* [X] Update ssh public key (incase you need to change it)
* [X] Change roaming assistant settings (if router supports it)
* [X] Change WebUI port (http and https, but seriously move over to https!)
* [X] Custom router/model profiles (conf files?) to support nvram settings for routers I have not personally tested


### Planned *potential* features
* Sync settings from main router (essentially bandwagon on the main routers WebUI?)
* Custom nvram commands?
* Automatic profile detection (if possible)
<br>

### Requirements
__Router:__
* SSH with private key authentication (rsa2048 or rsa4096) <br>
Note: Preferably with the ability to disable user+password ssh login!
* "nvram" commandline tool

__Computer or management device:__ <br>
Note: This tool is designed to be run from a Raspberry Pi or a Linux system
* SSH
* Python3
  * confparser
  * shlex
  * argparse
  * subprocess
  * re

## Make a system package for a package manager?
If you want this tool to run in a system level then just move all the files to /opt/mrtmgr then **_move_** the folders "groups" and "profiles" and the file mrtmgr.conf to /etc/mrtmgr

Finally symlink /opt/mrtmgr/mrtmgr to /usr/local/mrtmgr or for a package for a package manager symlink it to /usr/bin/mrtmgr


# How can I contribute?
Fork the project and do changes and open a pull request.<br>
However simply making a profile for other routers alone is a HUGE help in itself!

All you have to do is ssh into your router and run "nvram show" and look for the changes you have done in the WebUI once you have saved them and compare them and just add the key names (the name before the = in the settings) to a .conf file (look at the [rt66u.conf](https://github.com/HikariKnight/mrtmgr/blob/develop/profiles/rt66u.conf) and [dir879_dd-wrt.conf](https://github.com/HikariKnight/mrtmgr/blob/develop/profiles/dir879_dd-wrt.conf) as examples)

# How can I support you?
You could support me with the following links below
<br>

[![Donate](https://img.shields.io/badge/Buy%20me%20a%20drink-Donate-green.svg)](https://ko-fi.com/hikariknight)

<br>

[![Donate with PayPal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=4YAU4MPDT8ZJQ)
