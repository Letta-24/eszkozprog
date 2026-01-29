from netmiko import ConnectHandler

kapcsolo = {
    "device_type": "cisco_ios",
    "host": "192.168.40.133",
    "username": "letti",
    "password": "netmiko2026"
}
def netmiko_show_version():
    try:
        with ConnectHandler(**kapcsolo) as kapcsolat:
            output = kapcsolat.send_command("show version")
    except Exception as ex:
        print(f"Hiba:{ex}")
    

def fajlbeolvas():
    try:
        with open ("show_version.txt", encoding = "utf-8")as fajl:
            szoveg = fajl.read()
    except IOError as ex:
        print(f"IO hiba: {ex}")
    return szoveg

##Milyen IOS verzió fut a szerveren?

def ios_verzio(verzio_info):
    elso_sor =verzio_info.split("\n") [0]
    
    r = elso_sor.split(",")
    
    verzio = r[1].strip().split(" ")[2].lstrip("(").rstrip(")")
    verzio += " " + r[2].strip().lstrip("Version")
    
    return verzio
##Hány internet interface van a kapcsolón?##

def ethernet_interfacek_szama():
    pass

###############################################
    # PROGRAM
###############################################


output = ""

kapcsolo = {
    "device_type": "cisco_ios",
    "host": "192.168.40.133",
    "username": "letti",
    "password": "netmiko2026"
}


#netmiko_show_version(kapcsoló)
#print(output)

verzio_info = fajlbeolvas()

#print(verzio_info)

print(f"IOS verzió: {ios_verzio(verzio_info)}")
print(f"{ethernet_interfacek_szama()} Ethernet interface van a kapcsolón.")