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

# Work in progress
def set_channel(args):
    # Fake profile
    """ ssid_key = "wl0_ssid,wl1_ssid,dummy"
    nvram_bin = "/usr/sbin/nvram"

    keys = []
    if ',' in ssid_key:
        keys = ssid_key.split(',')

    command = []
    param = args.ssid
    values = param

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


    for key,value in zip(keys,values):
        command.append(nvram_bin + " set " + key + "=" + value)
            

    # Put the command together
    if not len(command) < 1:
        return " ; ".join(command)
    else:
        return command[0] """

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
    if param[0] != "psk" and param[0] != "psk2":
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
