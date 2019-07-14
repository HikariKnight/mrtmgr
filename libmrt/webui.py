def set_http_port(args):
    # Fake profile
    http_lanport_key = "http_lanport"
    nvram_bin = "/usr/sbin/nvram"

    return nvram_bin + " set " + http_lanport_key + "=" + str(args.http_port)


def set_https_port(args):
    # Fake profile
    https_lanport_key = "https_lanport"
    nvram_bin = "/usr/sbin/nvram"

    return nvram_bin + " set " + https_lanport_key + "=" + str(args.https_port)