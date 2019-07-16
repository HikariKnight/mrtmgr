import re


def set_SSID(args, profile):
    # Load profile info
    ssid_key = profile['nvram'].get('ssid_keys',None)
    nvram_bin = profile['router'].get('nvram_bin','/usr/sbin/nvram')

    # If no ssid key is defined then error out and exit
    if not ssid_key:
        print("Error: Profile has no value in 'ssid_keys'")
        exit()

    # Add keys to a list
    keys = []
    if ',' in ssid_key:
        keys = ssid_key.split(',')
    else:
        keys.append(ssid_key)
    
    # Prepare values for the settings
    param = args.ssid
    values = param

    # Loop through the ssid argument values and append them to the values list
    if len(values) == 1:
        values = []
        for key in keys:
            values.append(param[0])
    elif len(values) == 2:
        values = []
        i = 0
        for key in keys:
            if i == 0:
                values.append(param[0])
                i += 1
            else:
                values.append(param[1])

    # Generate router nvram commands to apply the values
    command = []
    for key,value in zip(keys,values):
        command.append(nvram_bin + " set " + key + "=" + value)
            

    # Put the command together and return the single command string
    if not len(command) < 1:
        return " ; ".join(command)
    else:
        return command[0]


def set_psk(args, profile):
    # Load profile info
    wpa_psk_key = profile['nvram'].get('wpa_psk_keys',None)
    nvram_bin = profile['router'].get('nvram_bin','/usr/sbin/nvram')

    # If no ssid key is defined then error out and exit
    if not wpa_psk_key:
        print("Error: Profile has no value in 'wpa_psk_keys'")
        exit()

    # Add keys to a list
    keys = []
    if ',' in wpa_psk_key:
        keys = wpa_psk_key.split(',')
    else:
        keys.append(wpa_psk_key)

    # Prepare values for the settings
    param = args.wpa_psk
    values = param

    # Loop through the wpa-psk argument values and append them to the values list
    if len(values) == 1:
        values = []
        for key in keys:
            values.append(param[0])
    elif len(values) == 2:
        values = []
        i = 0
        for key in keys:
            if i == 0:
                values.append(param[0])
                i += 1
            else:
                values.append(param[1])

    # Generate router nvram commands to apply the values
    command = []
    for key,value in zip(keys,values):
        command.append(nvram_bin + " set " + key + "=" + value)

    # Put the command together and return the single command string
    if not len(command) < 1:
        return " ; ".join(command)
    else:
        return command[0]


def set_channel(args, profile):
    # Load profile info
    channel_key = profile['nvram'].get('channel_2.4g_keys',None)
    nvram_bin = profile['router'].get('nvram_bin','/usr/sbin/nvram')

    # If no channel key is defined then error out and exit
    if not channel_key:
        print("Error: Profile has no value in 'channel_2.4g_key'")
        exit()

    # Get the passed channel number
    param = args.channel

    # Regex containing all 2.4Ghz channels
    channels = re.compile("^[0-9]$|^1[0-3]$")

    # If the number provided is not an actual 2.4Ghz channel number
    if not channels.match(param[0]):
        print("{} is not a valid channel!\nValid channels are: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13".format(param[0]))
        exit()

    # Add keys to a list
    keys = []
    if ',' in channel_key:
        keys = channel_key.split(',')
    else:
        keys.append(channel_key)
    
    # Prepare values for the settings
    values = []
    for key in keys:
        values.append(param[0])

    # Generate router nvram commands to apply the values
    command = []
    for key,value in zip(keys,values):
        command.append(nvram_bin + " set " + key + "=" + value)

    # Put the command together
    if not len(command) < 1:
        return " ; ".join(command)
    else:
        return command[0]


def set_channel_5g(args, profile):
    # Load profile info
    channel_5g_key = profile['nvram'].get('channel_5g_keys',None)
    nvram_bin = profile['router'].get('nvram_bin','/usr/sbin/nvram')

    # If no channel_5g key is defined then error out and exit
    if not channel_5g_key:
        print("Error: Profile has no value in 'channel_5g_key'")
        exit()

    # Get the passed channel number
    param = args.channel_5g

    # Regex containing all 5Ghz channels i know about
    #channels_5g = re.compile("0|36|40|44|48|52|56|60|64|100|104|108|112|116|132|136|140")
    channels_5g = re.compile("^0$|^36$|^4[0|4|8]$|^5[2|6]$|^6[0|4]$|^10[0|4|8]$|^11[2|6]$|^13[2|6]$|^140$")

    # If the number provided is not an actual 2.4Ghz channel number
    if not channels_5g.match(param[0]):
        print("{} is not a valid channel!\nValid channels are (depending on router): 0, 36, 40, 44, 48, 52, 56, 60, 64, 100, 104, 108, 112, 116, 132, 136, 140".format(param[0]))
        exit()

    # Add keys to a list
    keys = []
    if ',' in channel_5g_key:
        keys = channel_5g_key.split(',')
    else:
        keys.append(channel_5g_key)
    
    # Prepare values for the settings
    values = []
    for key in keys:
        values.append(param[0])

    # Generate router nvram commands to apply the values
    command = []
    for key,value in zip(keys,values):
        command.append(nvram_bin + " set " + key + "=" + value)
            
    # Put the command together
    if not len(command) < 1:
        return " ; ".join(command)
    else:
        return command[0]


def set_auth(args, profile):
    # Load profile info
    auth_mode_key = profile['nvram'].get('auth_mode_keys',None)
    nvram_bin = profile['router'].get('nvram_bin','/usr/sbin/nvram')

    # If no ssid key is defined then error out and exit
    if not auth_mode_key:
        print("Error: Profile has no value in 'auth_mode_keys'")
        exit()

    # Add keys to a list
    keys = []
    if ',' in auth_mode_key:
        keys = auth_mode_key.split(',')
    else:
        keys.append(auth_mode_key)
    
    # Prepare values for the settings
    param = args.auth
    values = param
    
    # If the argument is not psk or psk2 then force change it to psk2
    if param[0] != "psk" and param[0] != "psk2" and param[0] != "pskpsk2" and param[0] != "wpa2" and param[0] != "wpawpa2":
        print("Incorrect auth mode provided, setting auth mode to psk2")
        param[0] = "psk2"

    # Loop through the wpa-psk argument values and append them to the values list
    if len(values) == 1:
        values = []
        for key in keys:
            values.append(param[0])


    # Generate router nvram commands to apply the values
    command = []
    for key,value in zip(keys,values):
        command.append(nvram_bin + " set " + key + "=" + value)

    # Put the command together and return the single command string
    if not len(command) < 1:
        return " ; ".join(command)
    else:
        return command[0]
