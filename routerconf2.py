from netmiko import ConnectHandler

login_adatok ={
    "device_type": "cisco_ios",
    "host": "192.168.40.243",
    "username": "letti",
    "password": "letti"
}
def roas_conf(ssh):
    roas= [
        "interface G0/1.11",
        "encapsulation dot1q vlan 11",
        "ip address 192.168.11.11 255.255.255.0",
        "no shutdown",
        "interface G0/1.13",
        "encapsulation dot1q vlan 13",
        "ip address 192.168.13.13 255.255.254.0",
        "no shutdown",
        "interface G0/1",
        "no shutdown"
    ]

    ssh.send_config_set(roas)

try:
    with ConnectHandler(**login_adatok) as kapcsolat:    
       #1.Roas konfigurálás
       roas_conf(kapcsolat)
       print(kapcsolat.send_command("show running-config | include Interfaces"))
       print(kapcsolat.send_command("show running-config | include GigabitEthernet"))
       #2. 
       vl = input(f"Kérlek add meg a vlan azonosító számát:")
       vl = input(f"Kérlek add meg a vlan ip címét:")
       
except Exception as ex:
    print(f"Csatlakozási hiba: {ex}")