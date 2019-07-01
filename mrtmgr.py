#!/usr/bin/python3
import argparse
import os.path
import os
import sys
import shlex
import configparser
from subprocess import Popen
import libmrt

sys.path.append('libmrt')

confPath = os.getcwd()
settingsFile = confPath + "/mrtmgr.conf"

# Check if we are running locally or system-wide (essentially check for mrtmgr.conf in same folder)
if not os.path.exists(settingsFile):
    confPath = "/etc/mrtmgr"
    settingsFile = confPath + "/mrtmgr.conf"

# Setup script parameters
parser = argparse.ArgumentParser()

# Add profiles argument
parser.add_argument("profile", metavar="profile", nargs=1, help='Name of the nvram profile (.conf) from "' + confPath + '/profiles/" to use.')
parser.add_argument("address", metavar='IPs|hostnames|file="filename"', nargs="+",
    help='A space separated list of IPs or hostnames for the routers. \
    Alternatively you can add all the IPs/hostnames on separate lines into a file and just pass file="filename.list"')

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
    nargs="+")

# Channel settings
wifi.add_argument("--channel", metavar="channel",
    help="Update the prefered channel to use for the bands, the default is 0, \
        however this setting is recommended to set in the routers WebUI or leave at auto. 0 = auto",
    nargs="+",
    type=int,
    default="0")

# Make a security group
security = parser.add_argument_group("Security", "Lets you edit and update security \
    details like user login and password for the WebUI, ports and ssh-keys.\
    Most routers only supports ssh-keys using rsa2048 or rsa4096.")

# Change username
security.add_argument("--user", help="Change the routers WebUI username.")

# Change password
security.add_argument("--password", help="Change the routers WebUI password.")

# Change authenticated ssh-key
security.add_argument("--ssh-key", help="Change the public key stored in the nvram that is used to \
    authenticate ssh logins with private keys (primarily by this script). \
    WARNING: Will replace all existing keys!")

# Add ssh-key
security.add_argument("--add-ssh-key", metavar="SSH_KEY",
    help="Add a new ssh-key without removing old ones.")

# Change http port
security.add_argument("--http-port", help="Change the http port used for the router's WebUI, \
    but seriously move over to https already!")

# Change https port
security.add_argument("--https-port", help="Change the https port used for the router's WebUI.")


# Make a tuning group
tuning = parser.add_argument_group("Tuning", "Lets you tune supported routers RSSI or Roaming Assist which \
    automatically kick clients with poor signal off the network so they reconnect to a closer node.")

tuning.add_argument("--rssi", metavar="dBm",
    help="Sets the dBm threshold for when to kick clients off the routers wireless network \
        so they can reconnect to a closer node. NOTE: Change this only if you know what you are doing!",
        type=int)

# Parse all the arguments
args = parser.parse_args()

# Prepare our command
ssh_basecommand = "ssh -oStrictHostKeyChecking=no -oBatchMode=yes -p $PORT $USER@$HOST "
commands = []


if args.ssid:
    libmrt.ssid.set_SSID(args)