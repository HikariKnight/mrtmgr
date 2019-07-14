def set_RSSI(args):
    # Fake profile
    rssi_key = "wl_user_rssi,wl0_user_rssi,wl1_user_rssi"
    nvram_bin = "/usr/sbin/nvram"

    keys = []
    if ',' in rssi_key:
        keys = rssi_key.split(',')

    command = []
    param = args.rssi
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
        command.append(nvram_bin + " set " + key + "=" + str(value))

    # Put the command together
    if not len(command) < 1:
        return " ; ".join(command)
    else:
        return command[0]