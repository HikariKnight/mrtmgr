def set_RSSI(args, profile):
    # Load profile info
    rssi_key = profile['nvram'].get('roam_assist_keys',None)
    nvram_bin = profile['router'].get('nvram_bin','$(which nvram)')
    PATH_env = profile['router'].get('PATH','/bin:/usr/bin:/sbin:/usr/sbin:/jffs/sbin:' +
    '/jffs/bin:/jffs/usr/sbin:/jffs/usr/bin:/mmc/sbin:/mmc/bin:/mmc/usr/sbin:/mmc/usr/bin:' +
    '/opt/sbin:/opt/bin:/opt/usr/sbin:/opt/usr/bin')

    # If there is no RSSI key defined, error out
    if not rssi_key:
        print("Error: Profile has no value in 'roam_assist_keys' or function is unsupported!")
        exit()

    # Add keys to a list
    keys = []
    if ',' in rssi_key:
        keys = rssi_key.split(',')
    else:
        keys.append(rssi_key)

    # Prepare values for the settings
    param = args.rssi
    values = param

    # Loop through the rssi argument values and append them to the values list
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
        command.append(PATH_env + ' ' + nvram_bin + " set " + key + "=" + str(value))

    # Put the commands together and return the single command string
    if not len(command) < 1:
        return " ; ".join(command)
    else:
        return command[0]

def set_RSSI_5G(args, profile):
    # Load profile info
    rssi_5g_key = profile['nvram'].get('roam_assist_5g_keys',None)
    nvram_bin = profile['router'].get('nvram_bin','$(which nvram)')
    PATH_env = profile['router'].get('PATH','/bin:/usr/bin:/sbin:/usr/sbin:/jffs/sbin:' +
    '/jffs/bin:/jffs/usr/sbin:/jffs/usr/bin:/mmc/sbin:/mmc/bin:/mmc/usr/sbin:/mmc/usr/bin:' +
    '/opt/sbin:/opt/bin:/opt/usr/sbin:/opt/usr/bin')
    
    # If there is no RSSI key defined, error out
    if not rssi_5g_key:
        print("Error: Profile has no value in 'roam_assist_5g_keys' or function is unsupported!")
        exit()

    # Add keys to a list
    keys = []
    if ',' in rssi_5g_key:
        keys = rssi_5g_key.split(',')
    else:
        keys.append(rssi_5g_key)

    # Prepare values for the settings
    param = args.rssi_5g
    values = param

    # Loop through the rssi argument values and append them to the values list
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
        command.append(PATH_env + ' ' + nvram_bin + " set " + key + "=" + str(value))

    # Put the commands together and return the single command string
    if not len(command) < 1:
        return " ; ".join(command)
    else:
        return command[0]