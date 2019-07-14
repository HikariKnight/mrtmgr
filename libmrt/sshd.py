def set_ssh_key(args, profile):
    # Load profile info
    sshd_authkeys_key = profile['nvram'].get('sshd_authkeys_key',None)
    nvram_bin = profile['router'].get('nvram_bin','/usr/sbin/nvram')

    if not sshd_authkeys_key:
        print("Error: Profile has no value in 'sshd_authkeys_key'")
        exit()

    return nvram_bin + " set " + sshd_authkeys_key + "=" + args.ssh_key