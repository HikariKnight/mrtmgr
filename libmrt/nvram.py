from subprocess import Popen
import shlex

def commit(ssh_baseargs):
    # Convert the command to something accepted by popen
    ssh_command = shlex.split(ssh_baseargs + '"/usr/sbin/nvram show"')
    # Run the command
    Popen(ssh_command)

def rt_exec(ssh_baseargs, commands):
    # Join the list of commands by " ; " making it more readable and also chain them together
    ssh_args = ' ; '.join(commands)
    # Convert the command(s) to something popen will accept
    ssh_command = shlex.split(ssh_baseargs + '"' + ssh_args + '"')
    # Run the command(s)
    Popen(ssh_command)