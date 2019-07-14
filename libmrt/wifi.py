def set_SSID(args):
    # Fake profile
    ssid_key = "wl0_ssid,wl1_ssid,dummy"
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
        return command[0]

def set_psk(args):
    # Fake profile for testing
    wpa_psk_key = "wl0_wpa_psk,wl1_wpa_psk"
    nvram_bin = "/usr/sbin/nvram"

    keys = []
    if ',' in wpa_psk_key:
        keys = wpa_psk_key.split(',')

    command = []
    param = args.wpa_psk
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

def set_auth(args):
    # Fake profile for testing
    auth_mode_key = "wl0_auth_mode_x,wl0_akm,wl1_auth_mode_x,wl1_akm,wl_auth_mode_x,wl_akm"
    nvram_bin = "/usr/sbin/nvram"

    keys = []
    if ',' in auth_mode_key:
        keys = auth_mode_key.split(',')

    command = []
    param = args.auth
    values = param
    
    if param[0] != "psk" and param[0] != "psk2":
        print("Incorrect auth mode provided, setting auth mode to psk2")
        param[0] = "psk2"

    if len(values) == 1:
        values = []
        for key in keys:
            values.append(param[0])

    for key,value in zip(keys,values):
        command.append(nvram_bin + " set " + key + "=" + value)

    # Put the command together
    if not len(command) < 1:
        return " ; ".join(command)
    else:
        return command[0]
