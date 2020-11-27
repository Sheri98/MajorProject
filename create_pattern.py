import subprocess


def pattern_create(length):
    cmd = '/usr/share/metasploit-framework/tools/exploit/pattern_create.rb'
    arg =   '-l'
    value = str(length)
    proc = subprocess.Popen([cmd,arg,value],stdout=subprocess.PIPE)
    (data, error) = proc.communicate()
    return data