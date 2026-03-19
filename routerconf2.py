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
        "encapsulation dot1q 11",
        "ip address 192.168.11.11 255.255.255.0",
        "no shutdown",
        "interface G0/1.13",
        "encapsulation dot1q 13",
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
       print(kapcsolat.send_command("show ip interface brief"))
       
       #2.
       
       #3.tftp mentés
       tftp = input(f"Kérlek add meg a szerver ip címét:")
       fajlnev = input (f"mentendő konfig fálj neve:")
       
       output = kapcsolat.send_multiline_timing(["copy running-config tftp",tftp,fajlnev])
       print(output)
       
       #4.alinterfécek kiíratása vlanjaikkkal
       all = kapcsolat.send_command("show running-config | section interfaces")
       all = kapcsolat.send_command("show running-config | include GigabitEthernet")
       allint = all.split("\n")
       print(allint)
       for i in range (allint):
           if "." in allint:
            print(allint.strip("."))

            
        
except Exception as ex:
    print(f"Csatlakozási hiba: {ex}")