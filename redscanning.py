import nmap

nmap_path = [r"C:\Program Files (x86)\Nmap\nmap.exe",]
scanner = nmap.PortScanner(nmap_search_path=nmap_path)
ip = input("· Enter an IP Address: ")
print("· This is the IP address you entered:", ip)
scanner.scan(ip)

print(scanner.all_hosts())