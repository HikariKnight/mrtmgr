def set_ssh_key(args, profile):
    # Load profile info
    sshd_authkeys_key = profile['nvram'].get('sshd_authkeys_key',None)
    nvram_bin = profile['router'].get('nvram_bin','$(which nvram)')
    PATH_env = profile['router'].get('PATH','/bin:/usr/bin:/sbin:/usr/sbin:/jffs/sbin:' +
    '/jffs/bin:/jffs/usr/sbin:/jffs/usr/bin:/mmc/sbin:/mmc/bin:/mmc/usr/sbin:/mmc/usr/bin:' +
    '/opt/sbin:/opt/bin:/opt/usr/sbin:/opt/usr/bin')

    # If no sshd_authkeys key is defined then error out and exit
    if not sshd_authkeys_key:
        print("Error: Profile has no value in 'sshd_authkeys_key'")
        exit()

    # Return the router nvram command
    return PATH_env + ' ' + nvram_bin + " set " + sshd_authkeys_key + "=" + args.ssh_key