import socket
import sys

def port_tara(hedef_ip, portlar):
    print(f"\n[+] {hedef_ip} adresi taranıyor...\n")
    
    for port in portlar:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)
        
        sonuc = s.connect_ex((hedef_ip, port))
        
        if sonuc == 0:
            print(f"[AÇIK] Port {port} aktif!")
        else:
            print(f"[KAPALI] Port {port}")
            
        s.close()

if __name__ == "__main__":
    hedef = input("Taranacak IP veya Alan Adını Girin (Örn: scanme.nmap.org): ")
    if not hedef:
        hedef = "scanme.nmap.org"
        
    test_portlari = [21, 22, 80, 443]
    port_tara(hedef, test_portlari)
