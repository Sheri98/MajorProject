import subprocess
def find_offset():
    cmd = '/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb'
    arg = '-l'
    add = str(input("Enter the EIP value"))
    value = str(input("Enter the length"))
    poc = subprocess.Popen([cmd,arg,value,"-q",add],stdout=subprocess.PIPE)
    return poc.communicate()