# Mesh RouTer ManaGeR (Work in Progress!)
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

### Planned *potential* features
* Change key router settings like: WPA-PSK, WPA2-PSK, SSID
* Update ssh public key (incase you need to change it)
* Change roaming assistant settings (if router supports it)
* Custom router/model profiles (conf files?) to support nvram settings for routers I have not personally tested
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