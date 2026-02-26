from netmiko import ConnectHandler

login_adatok ={
    "device_type": "cisco_ios",
    "host": "192.168.40.143",
    "username": "letti",
    "password": "letti"
}

try:
    with ConnectHandler(**login_adatok) as kapcsolat:    
        pass
except Exception as ex:
    print(f"Csatlakozási hiba: {ex}")
