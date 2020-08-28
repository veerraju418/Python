import os
inp=input('do you want to shutdown your pc')
if inp=='yes':
    os.system('shutdown /s /t 1')
else:
    exit
