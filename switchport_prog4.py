from netmiko import ConnectHandler

login_adatok ={
    "device_type": "cisco_ios",
    "host": "192.168.40.143",
    "username": "letti",
    "password": "letti"
}
#1.
def konzol_jelszo_ellenorzes(ssh, online):
    konzol_kimenet = "line con 0\
                        password Jelszo123\
                        logging synchronous\
                        login"
    
    konzol_kimenet.split('/n')
    
try:
    with ConnectHandler(**login_adatok) as kapcsolat:    
        #1.
            konzol_jelszo_ellenorzes(kapcsolat)
            print(kapcsolat.send_command("show running config |section line console"))
except Exception as ex:
    print(f"Csatlakozási hiba: {ex}")