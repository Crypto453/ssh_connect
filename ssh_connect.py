import os
import time

os.system("clear")
banner_a = "         _                                        _   "
banner_b = " ___ ___| |__      ___ ___  _ __  _ __   ___  ___| |_ "
banner_c = "/ __/ __| '_ |    / __/ _ || '_ || '_ | / _ || __| __|"
banner_d = "|__ |__ | | | |  | (_| (_) | | | | | | |  __/ (__| |_ "
banner_e = "|___/___/_| |_|___|___|___/|_| |_|_| |_||___||___|__|"
banner_f = "             |_____|                                  "
banner_banner = [banner_a, banner_b, banner_c, banner_d, banner_e, banner_f]

option_option = ["[ 1 ] Connect to ssh server", "[ 2 ] Install ssh server on my computer", "[ 3 ] Manager ssh ", "[ 4 ] Ssh connection log ", "[ 5 ] EXIT"]

a = ("[==>                        ]10%")
b = ("[====>                      ]15%")
c = ("[=======>                   ]20%")
d = ("[=========>                 ]30%")
e = ("[===========>               ]40%")
f = ("[==============>            ]50%")
g = ("[================>          ]60%")      
h = ("[==================>        ]70%")
i = ("[====================>      ]80%")
j = ("[========================>  ]90%")
k = ("[==========================>]100% COMPLETADO!!!")

carga_a = [a, b, c, d, e, f, g, h, i, j, k]

manager = ["[ 1 ] ssh server start", "[ 2 ] ssh server stop", "[ 3 ] ssh server reboot"]

for banner_x in banner_banner:
    print(banner_x)
    time.sleep(0.3)
for op_x in option_option:
    print(op_x)
eggs_a = int(input("===> "))
if eggs_a == 1:
    eg_a = int(input("Do you have a user? /[1]Yes/[2]No \n===> "))
    if eg_a == 1:
        egg_a = input("Enter your user: ")
        egg_b = input("Write your IP Adress: ")
        egg_c = input("Write your port: ")
        os.system(f"ssh -l {egg_a} {egg_b} -p {egg_c}")
    elif eg_a == 2:
        eggss = input("Write your IP Adress: ")
        eggss_b = input("Write your port: ")
        os.system(f"ssh {eggss} -p {eggss_b}")    
    else: 
        print("ERROR!!!")
        os.system("python3 ssh_connect.py")
elif eggs_a == 2:
    print("[+]INSTALL SSH[+]")
    os.system("clear")
    for banner_v in banner_banner:
        print(banner_v)
        time.sleep(0.3)
        os.system("clear")
    os.system("sudo apt install ssh > nul")
    for carga_carga in carga_a:
        print(carga_carga)
        time.sleep(0.3)
        os.system("clear")
    print("wait......")
    time.sleep(0.1)
    os.system("sudo service ssh start")
    print(a)
    for carga_loading in carga_a:
        print(carga_loading)
        time.sleep(0.3)
        os.system("clear")
    print("ssh server started....") 
    time.sleep(3)
    os.system("python3 ssh_connect.py")   
elif eggs_a == 3:
    os.system("clear")
    for banner_h in banner_banner:
        print(banner_h)
        time.sleep(0.3)
    for man_a in manager:
        print(man_a)
        time.sleep(0.3)
    user_a = int(input("===> "))
    if user_a == 1:
        os.system("sudo service ssh start")
        print("ssh server started....")
        time.sleep(3)
        os.system("python3 ssh_connect.py")
    elif user_a == 2:
        os.system("sudo service ssh stop")
        print("ssh server stoped...")
        time.sleep(3)                    
        os.system("python3 ssh_connect.py")
    elif user_a == 3:
        os.system("sudo service ssh reboot")
        print("ssh server rebooting")
        time.sleep(3)
        os.system("python3 ssh_connect.py")
    else:
        print("ERROR!!!")
        os.system("python3 ssh_connect.py")
elif eggs_a == 4:
    os.system("sudo cat /var/log/auth* | grep Accepted")            
    menu_a = input("Do you want to go back to the menu? [1]Yes / [2]No \n===> ")
    if menu_a == 1:
        os.system("python3 ssh_connect.py")
    elif menu_b == 2:
        quit()
    else:
        print("ERROR!!!")
elif eggs_a == 5:
    quit()
else: 
    print("ERROR!!!")
    os.system("python3 ssh_connect.py")                    
            




    