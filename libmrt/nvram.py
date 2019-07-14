from subprocess import Popen
import shlex

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
    # Run the command(s)
    print(ssh_command)

def _combineCmd(ssh_basecmd, commands, profile):
    # Load profile
    nvram_bin = profile['router'].get('nvram_bin','/usr/sbin/nvram')
    
    # Combine the commands
    ssh_args = ' ; '.join(commands)
    return ssh_basecmd + '"' + ssh_args + ' ; ' + nvram_bin + ' commit ; /sbin/reboot"' 