from netmiko import ConnectHandler

login_adatok ={
    "device_type": "cisco_ios",
    "host": "192.168.40.243",
    "username": "letti",
    "password": "letti"
}
#3.loopback létrehozzása
def loop_back(ssh):
    loop = [
        "interface loopback 100",
        "description this is an infinite loop",
        "ip address 10.10.10.10 255.255.255.0",
        "no shutdown",
        "exit"
    ]
    
    ssh.send_config_set(loop)
    
try:
    with ConnectHandler(**login_adatok) as kapcsolat:    
        #1.üzemidő mutatása
        ido = kapcsolat.send_command("show version | include uptime")
        time = ido.split(" ")
        print(f"Az eszköz {time[-2]} {time[-1]} ideje müködik")
        
        
        #2.nem aktív interfészek mutatása
        inter = kapcsolat.send_command("sh ip interface brief")
        face = inter.split("\n")
        for interfesz in face:
            if "down" in interfesz:
                print(f"\n{interfesz.split(" ")[0]}")
                
                
        #3.1 loopback ellenőrzése
        loop_back(kapcsolat)
        if len(kapcsolat.send_command("show ip interface brief | include loopback100")) != 0:
            print(f"\nInterfész létrehozása sikerült!")
        
        #4.sávszélesség paraméterek
        
        szeles = kapcsolat.send_command("show interface G0/0")
        print(f"A G0/0 interfész EIGRP mérték számításban szereplő paraméreteinek értékei:")
        
        for sor in szeles.split("\n"):
            if "BW" in sor:
                adatok = sor.split(",").strip()
                
                for adat in adatok:
                    if "BW" in adat:
                        print(f"\tSávszélesség: {adat.split(" ")[-2:]}")
                    elif "DLY" in adat:
                        print(f"\tKésleltetés: {adat.split(" ")[-2:]}")
            elif "reliability" in sor :
                if "reliability" in adat:
                    print(f"\tMegbízhatóság: {adat.split(" ")[-1]}")
                    print(f"\tTerhelés:", end = " ")
                elif "load" in adat:
                    print(f"{adat.split(" ")[-1]}", end = " ")
        print("\n")


except Exception as ex:
    print(f"Csatlakozási hiba: {ex}")