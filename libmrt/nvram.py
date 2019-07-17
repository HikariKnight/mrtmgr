from subprocess import Popen
import shlex
import re

def _commit(ssh_command):
    # Commit the changes to the router
    Popen(ssh_command)


def rt_exec(ssh_basecmd, commands, profile):
    # Combine the ssh command with shlex to make it popen compatible
    ssh_command = shlex.split(_combineCmd(ssh_basecmd, commands, profile))
    # Run the command(s)
    _commit(ssh_command)


def dry_run(ssh_basecmd, commands, profile):
    ssh_command = _combineCmd(ssh_basecmd, commands, profile)
    
    # Remove the $PATH environment from each command
    removePATH = re.compile('PATH=' + profile['router'].get('PATH', '/bin:/usr/bin:/sbin:/usr/sbin:/jffs/sbin:/jffs/bin:/jffs/usr/sbin:/jffs/usr/bin:/mmc/sbin:/mmc/bin:/mmc/usr/sbin:/mmc/usr/bin:/opt/sbin:/opt/bin:/opt/usr/sbin:/opt/usr/bin '))
    ssh_command = removePATH.sub('',ssh_command)

    # Run the command(s)
    print(ssh_command)


def _combineCmd(ssh_basecmd, commands, profile):
    # Load profile
    PATH_env = profile['router'].get('PATH','/bin:/usr/bin:/sbin:/usr/sbin:/jffs/sbin:' +
    '/jffs/bin:/jffs/usr/sbin:/jffs/usr/bin:/mmc/sbin:/mmc/bin:/mmc/usr/sbin:/mmc/usr/bin:' +
    '/opt/sbin:/opt/bin:/opt/usr/sbin:/opt/usr/bin')
    nvram_bin = profile['router'].get('nvram_bin','$(which nvram)')
    
    # Combine the commands
    ssh_args = ' ; '.join(commands)
    return ssh_basecmd + '"' + ssh_args + ' ; PATH=' + PATH_env + ' ' + nvram_bin + ' commit ; PATH=' + PATH_env + ' reboot"' 