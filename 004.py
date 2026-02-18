from netmiko import ConnectHandler

login_adatok ={
    "device_type": "cisco_ios",
    "host": "192.168.40.143",
    "username": "letti",
    "password": "letti"
}

try:
    with ConnectHandler(**login_adatok) as kapcsolat:    
        #1.
        kapcsolat.send_config_set("login block-for[60]")
        kapcsolat.send_command("show running-config |include password")
        
        #3.tftp mentés
        tftp_ip = input(f"Adja meg a szerver IP-címét!:")
        fajlnev = input(f"Mentendő konfig fálj neve:")
        
        output = kapcsolat.send_multiline_timing(["copy running-config tftp", tftp_ip, fajlnev])
        print(output)
        
except Exception as ex:
    print(f"Csatlakozási hiba: {ex}")




    
#2-es feladathoz kell ,replace, ha min nem teljesíti
'''
    if password < 8:
        print("nem jó add meg másikat!")
        password.replace()
    print("Rendben van")'''