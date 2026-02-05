from netmiko import ConnectHandler

login_adatok ={
    "device_type": "cisco_ios",
    "host": "192.168.40.143",
    "username": "letti",
    "password": "letti"
}
def mentes(ssh):
    ssh.save_config()
    
def set_enable_pwd(ssh):
    jelszo = input("Add meg az új enable jelszót!:")
    ssh.send_config_set(f"enable password {jelszo}")
    
def banner_jelszo_ellenorzes(ssh):
    ssh.send_config_set(f"banner motd #Jogosulatlanul bejelenktkezni TILOS!#")
    print(ssh.send_command("show running-config |include password"))
    print(ssh.send_command("show running-config |include secret"))
    
# -------------------------
# PROGRAM
# -------------------------

try:
    with ConnectHandler(**login_adatok) as kapcsolat:
        # 2.f
        print(kapcsolat.find_prompt())
        # 3.f
        #print()
        mentes(kapcsolat)
        valasz = kapcsolat.send_command("show startup-config")
        
        if  "not present" not in valasz: 
            print("A mentés sikerült!")
        else:
            print("A mentés nem sikerült!")
        
        # 4.f
            print(set_enable_pwd)
            print(kapcsolat.send_command("show running-config | include enable"))
            
        #5.f
        
        #6.f
        
        #7.f
        print()
        print(kapcsolat.send_command("no ip domain lookup"))
        #8.f
        print()
        print(kapcsolat.send_command("spanning-tree mode rapid pvst"))
        #9.f
        print()
        print(kapcsolat.send_command("erase startup-config"))
except Exception as ex:
    print(f"Csatlakozási hiba: {ex}")