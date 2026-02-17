from netmiko import ConnectHandler

login_adatok ={
    "device_type": "cisco_ios",
    "host": "192.168.40.143",
    "username": "letti",
    "password": "letti"
}

'''def ethernet(ssh):
    #1. interfacek kiválogatása
    interface = (ssh.send_command("show running-config | include interface"))
    interface.split('\n')
    
    utp = interface.split('\n')
    print(utp)
    
    
    #2.interfacek '/' jel eltávolítása
    
    for i in range(len(utp)):
            
        perjel = utp[i].split(' ')[1]
        perjel = perjel.split('/')[0] 
        perjel = perjel[:-1]          
        print(perjel)
    
    #3.interfacek megszámolása
    fdb=0
    gdb=0
    for i in range(utp):
        if utp[i] == 'FastEthernet':
            fdb = utp[i] + fdb
            
        if utp[i] == 'GigabitEthernet':
            gdb = utp[i] + gdb
    print()'''
try:
    with ConnectHandler(**login_adatok) as kapcsolat:    
        pass
except Exception as ex:
    print(f"Csatlakozási hiba: {ex}")