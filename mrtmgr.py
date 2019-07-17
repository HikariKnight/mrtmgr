#!/usr/bin/python3
import argparse
import os.path
import os
import sys
import shlex
import configparser
import libmrt
import re

sys.path.append('libmrt')

confPath = os.getcwd()
settingsFile = confPath + "/mrtmgr.conf"

# Check if we are running locally or system-wide (essentially check for mrtmgr.conf in same folder)
if not os.path.exists(settingsFile):
    confPath = "/etc/mrtmgr"
    settingsFile = confPath + "/mrtmgr.conf"

# Read the config file
config = configparser.ConfigParser()
config.read(settingsFile)

# Setup script parameters
parser = argparse.ArgumentParser()

# Add profiles argument
parser.add_argument("profile", metavar="profile", nargs=1, help='Name of the nvram profile (.conf) from "' + confPath + '/profiles/" to use.')
parser.add_argument("address", metavar='IP|hostname|group="filename"', nargs=1,
    help='The IP or hostname for the router. \
    Alternatively you can add all the IPs/hostnames on separate lines into a file and just pass group="filename".\
    The file is fetched from a .list file in "' + confPath + '/groups" with the same name you provide.')

# Make a group for wireless settings
wifi = parser.add_argument_group("Wireless", "Each parameter can take one or more argument, \
    passing one will use that value for all bands while passing more than one will use the first \
    value for the 2.4Ghz band and the 2nd value for all 5Ghz bands. If you pass 3 arguments then \
    the last one will be used for the 2nd 5Ghz band (tri-band routers), should it exist.")

# SSID
wifi.add_argument("--ssid", metavar="SSID",
    help="Update SSID for the wireless network(s)",
    nargs="+")

# WPA-PSK
wifi.add_argument("--wpa-psk", metavar="PSK",
    help="Update the wireless password for the wireless network(s)",
    nargs="+")

# Authentication
wifi.add_argument("--auth", metavar="psk|psk2",
    help="Update the authentication method for the wireless network(s).\
        psk = WPA-PSK, \
        psk2 = WPA2-PSK.",
    nargs=1)

# Channel settings
wifi.add_argument("--channel", metavar="channel",
    help="Update the prefered channel to use for the 2.4Ghz bands, the default is auto, \
        however this setting is recommended to set in the routers WebUI or leave at auto. \
        Valid channels are: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13",
    nargs=1)

# 5Ghz Channel settings
wifi.add_argument("--channel-5g", metavar="channel",
    help="Update the prefered channel to use for the 5Ghz bands, the default is auto, \
        however this setting is recommended to set in the routers WebUI or leave at auto. \
        Valid channels are (depending on router): 0, 36, 40, 44, 48, 52, 56, 60, 64, 100, 104, 108, 112, 116, 132, 136, 140",
    nargs=1)

# Make a security group
security = parser.add_argument_group("Security", "Lets you edit and update security \
    details like user login and password for the WebUI, ports and ssh-keys.\
    Most routers only supports ssh-keys using rsa2048 or rsa4096.")

# Change authenticated ssh-key
security.add_argument("--ssh-key", help="Change the public key stored in the nvram that is used to \
    authenticate ssh logins with private keys (primarily by this script). \
    WARNING: Will replace all existing keys!")

# Add ssh-key
#security.add_argument("--add-ssh-key", metavar="SSH_KEY",
#    help="Add a new ssh-key without removing old ones.")

# Change http port
security.add_argument("--http-port", help="Change the http port used for the router's WebUI, \
    but seriously move over to https already!",
    type=int)

# Change https port
security.add_argument("--https-port", help="Change the https port used for the router's WebUI.",
    type=int)


# Make a tuning group
tuning = parser.add_argument_group("Tuning", "Lets you tune supported routers RSSI or Roaming Assist which \
    automatically kick clients with poor signal off the network so they reconnect to a closer node.")

tuning.add_argument("--rssi", metavar="dBm",
    help="Sets the dBm threshold for when to kick clients off the routers 2.4Ghz wireless network \
        so they can reconnect to a closer node. NOTE: Change this only if you know what you are doing!",
        type=int, nargs="+")

tuning.add_argument("--rssi-5g", metavar="dBm",
    help="Sets the dBm threshold for when to kick clients off the routers 5Ghz wireless network \
        so they can reconnect to a closer node. NOTE: Change this only if you know what you are doing!",
        type=int, nargs="+")

endconfig = parser.add_argument_group("End config", "Signify you are ending the configuration here.\
    (This is a workaround to stop the arguments taking 1 or more option from thinking profile and IP is\
    part of its own options)")

endconfig.add_argument("--commit", action='store_true', help='This argument MUST be used before PROFILE,\
    it is here to "end" the config so that any parameters using 1 or more values wont include profile and IP\
    and tells mrtmgr to commit the changes to the routers and reboot them.')

endconfig.add_argument("--dry-run", action='store_true', help='This argument MUST be used before PROFILE,\
    it is here to "end" the config so that any parameters using 1 or more values wont include profile and IP\
    and tells mrtmgr to not commit the changes and just print out the commands.')

# Parse all the arguments
args = parser.parse_args()

profile = libmrt.profile.load(confPath,args.profile)

# Check if we are going to have strict key checks in ssh (enable for production!)
strict_checks = ''
if config["ssh"].getboolean("strict_checks"):
    strict_checks = "-oStrictHostKeyChecking=yes"
else:
    strict_checks = "-oStrictHostKeyChecking=no"

# Prepare our command
ssh_baseargs = 'ssh ' + strict_checks + ' -oBatchMode=yes -i "' + config["ssh"]["privkey_file"] + '" ' + profile['router']['user'] + '@'
commands = []

if not args.commit and not args.dry_run:
    print('Missing the --commit or --dry-run argument at the end of the "optional" arguments.')
    exit()
elif args.commit and args.dry_run:
    print('Please only use --commit or --dry-run, they cannot be used together!')
    exit()


# Run the libmrt functions for the arguments passed
if args.ssid:
    commands.append(libmrt.wifi.set_SSID(args,profile))

if args.wpa_psk:
    commands.append(libmrt.wifi.set_psk(args,profile))

if args.channel:
    commands.append(libmrt.wifi.set_channel(args,profile))

if args.channel_5g:
    commands.append(libmrt.wifi.set_channel_5g(args,profile))

if args.auth:
    commands.append(libmrt.wifi.set_auth(args,profile))

if args.rssi:
    commands.append(libmrt.rssi.set_RSSI(args,profile))

if args.rssi_5g:
    commands.append(libmrt.rssi.set_RSSI_5G(args,profile))

if args.http_port:
    commands.append(libmrt.webui.set_http_port(args,profile))

if args.https_port:
    commands.append(libmrt.webui.set_https_port(args,profile))

if args.ssh_key:
    commands.append(libmrt.sshd.set_ssh_key(args,profile))
# End of argument handling

# Make an empty string before generating the ssh base command
ssh_basecmd = ''

# If a group list of addresses was passed
if "group=" in args.address[0]:
    # Remove group= from the beginning of the passed file
    regex = re.compile("^group=")
    group = regex.sub("",args.address[0])
    
    # Open the config file and read the addresses
    with open(confPath + '/groups/' + group + '.list') as addresses:
        # For each line/address
        for address in addresses:
            # Print to console
            print('Configuring ' + address + '')

            # Generate a ssh_base command
            ssh_basecmd = ssh_baseargs + address.rstrip() + ' '

            # If --dry-run was passed, do a dry run and print the commands with no interaction with the routers
            if args.dry_run:
                # Print to console that we are doing a dry-run
                print('the command would have been run to configure ' + address + ' if you used --commit')
                
                # Generate the command and print it
                libmrt.nvram.dry_run(ssh_basecmd, commands, profile)

                # Print an empty line for spacing
                print('')

            # If --commit was passed do a full run executing the commands on the routers
            if args.commit:
                # Print to console that we are commiting and rebooting the router
                print('commiting config and rebooting ' + address)

                # Generate the command and commit it
                libmrt.nvram.rt_exec(ssh_basecmd, commands, profile)

                # Print an empty line for spacing
                print('')
else:
    # Generate a single ssh_base command
    ssh_basecmd = ssh_baseargs + args.address[0] + ' '

    # If --dry-run was passed, do a dry run and print the commands with no interaction with the routers
    if args.dry_run:
        libmrt.nvram.dry_run(ssh_basecmd, commands, profile)

    # If --commit was passed do a full run executing the commands on the routers
    if args.commit:
        libmrt.nvram.rt_exec(ssh_basecmd, commands, profile)