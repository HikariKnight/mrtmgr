def set_ssh_key(args):
    sshd_authkeys_key = "sshd_authkeys"
    nvram_bin = "/usr/sbin/nvram"

    return nvram_bin + " set " + sshd_authkeys_key + "=" + args.ssh_key