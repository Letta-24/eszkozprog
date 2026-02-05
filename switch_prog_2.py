from netmiko import ConnectHandler

login_adatok ={
    "device_type": "cisco_ios",
    "host": "192.168.40.143",
    "username": "letti",
    "password": "letti"
}

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
    
def konzol_ellenor(ssh):
    pass
def konzol_jelszo(ssh):
    
    #replace("konJelszo")
    pass
def interface_szam(ssh):
    #count()
    pass

# -------------------------
# PROGRAM
# -------------------------

try:
    with ConnectHandler(**login_adatok) as kapcsolat:
        #1.f
        vlan_ok(kapcsolat)
        print(kapcsolat.send_command("show vlan brief"))
        #2.f
        #3.f
        
        #4.f
except Exception as ex:
    print(f"Csatlakozási hiba: {ex}")