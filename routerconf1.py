from netmiko import ConnectHandler

login_adatok ={
    "device_type": "cisco_ios",
    "host": "192.168.40.243",
    "username": "letti",
    "password": "letti"
}

try:
    with ConnectHandler(**login_adatok) as kapcsolat:
        #szomszéd lekérdezés és szomszédok elem számának kiíratása
        os = kapcsolat.send_command("show ip ospf neighbor")
        ospf=os.split("\n")
        print(len(ospf)-2)

    #pc cím hirdetése
    pc = kapcsolat.send_config_set("router ospf 13")
    pc = kapcsolat.send_config_set("network 172.162.243.14 255.255.255.252")
    ell = kapcsolat.send_command ("show ip ospf 13 | include network")
    print(ell)
    
    #ospf sávszélesség bekérése a felhasználótól
    band = input("Kérlek add meg a sávszélességet az ospf-hez:")
    
    ellb = kapcsolat.send_command("show ip ospf 13 | include bandwith")
    
    
    
    #Egyedi router azonosító kérése
    azon = input("Kérlek add meg az ospf azonosítót:")
    
    
except Exception as ex:
    print(f"Csatlakozási hiba: {ex}")
    
#pc ip 172.162.243.14 255.255.255.252