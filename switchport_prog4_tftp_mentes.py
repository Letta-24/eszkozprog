from netmiko import ConnectHandler

login_adatok ={
    "device_type": "cisco_ios",
    "host": "192.168.40.143",
    "username": "letti",
    "password": "letti"
}


try:
    with ConnectHandler(**login_adatok) as kapcsolat:    
        tftp_ip = input(f"Adja meg a szerver IP-címét!:")
        fajlnev = input(f"Mentendő konfig fálj neve:")
        
        output = kapcsolat.send_multiline_timing(["copy running-config tftp", tftp_ip, fajlnev])
        print(output)
        
except Exception as ex:
    print(f"Csatlakozási hiba: {ex}")
    
    
    
        
#--------------------------------------------------------------------------------------------------------------------