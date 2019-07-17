def set_http_port(args, profile):
    # Load profile info
    http_lanport_key = profile['nvram'].get('http_lanport_key',None)
    nvram_bin = profile['router'].get('nvram_bin','$(which nvram)')
    PATH_env = profile['router'].get('PATH','/bin:/usr/bin:/sbin:/usr/sbin:/jffs/sbin:' +
    '/jffs/bin:/jffs/usr/sbin:/jffs/usr/bin:/mmc/sbin:/mmc/bin:/mmc/usr/sbin:/mmc/usr/bin:' +
    '/opt/sbin:/opt/bin:/opt/usr/sbin:/opt/usr/bin')

    # If no http_lanport key is defined then error out and exit
    if not http_lanport_key:
        print("Error: Profile has no value in 'http_lanport_key'")
        exit()

    # Return the router nvram command
    return PATH_env + ' ' + nvram_bin + " set " + http_lanport_key + "=" + str(args.http_port)


def set_https_port(args, profile):
    # Load profile info
    https_lanport_key = profile['nvram'].get('https_lanport_key',None)
    nvram_bin = profile['router'].get('nvram_bin','$(which nvram)')

    # If no https_lanport key is defined then error out and exit
    if not https_lanport_key:
        print("Error: Profile has no value in 'https_lanport_key'")
        exit()

    # Return the router nvram command
    return nvram_bin + " set " + https_lanport_key + "=" + str(args.https_port)