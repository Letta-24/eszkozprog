from netmiko import ConnectHandler

login_adatok ={
    "device_type": "cisco_ios",
    "host": "192.168.40.143",
    "username": "letti",
    "password": "letti"
}

#Vlanok kiíratása

def vlan_ok(ssh):
    parancsok = [
    "vlan 10",
    "name Tanulo",
    "vlan 20",
    "name Oktato",
    "vlan 30",
    "name Pedagogus",
    "vlan 100",
    "name Ugyvitel"
    ]
    ssh.send_config_set(parancsok)
    
#konzol jelszavas védelem ellenőrzése

def konzol_ellenor(ssh):
   ssh.send_config_set(konzol_ellenor)
#konzoljelszó megváltoztatása
def konzol_jelszo(ssh):
    konzoljel = [
        "line console 0",
        "password konJelszo"
        ]
    ssh.send_config_set(konzoljel)
    
    
#interfészek típusai és annak darab száma  
def interface_szam(ssh):
    
    ssh.send_config_set(interface_szam)
    
# -------------------------
# PROGRAM
# -------------------------

try:
    with ConnectHandler(**login_adatok) as kapcsolat:
        #1.f
        vlan_ok(kapcsolat)
        print(kapcsolat.send_command("show vlan brief"))
        #2.f
        konzol_ellenor(kapcsolat)
        print(kapcsolat.send_command("show running-config | include line con 0"))
        #3.f
        konzol_jelszo(kapcsolat)
        print(kapcsolat.send_command("show running-config | include line con 0"))
        print(kapcsolat.send_command("show running-config | include password"))
        #4.f
        interface_szam(kapcsolat)
        print(kapcsolat.send_command("show running-config | include interface"))
except Exception as ex:
    print(f"Csatlakozási hiba: {ex}")