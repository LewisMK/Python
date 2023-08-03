from scapy.all import *
from scapy.layers.inet import IP, TCP
import dns.resolver
import threading

def syn_scan(target, port):
    
    src_port = RandShort()
    
    response = sr1(IP(dst=target)/TCP(sport=src_port, dport = port, flags = "S"), timeout = 1, verbose = 0)

    if response and response.haslayer(TCP):
        if response[TCP].flags == 0x12:
            print(f"Port {port} is open")
            
            send(IP(dst=target)/TCP(sport=src_port, dport = port, flags = "R"))
        elif response[TCP].flags == 0x14:
            print(f"Port {port} is closed")
            
            
def dns_scan(domain):
    
    answers = dns.resolver.resolve(domain, 'A')
    
    for answer in answers:
        print(f"Found DNS record: {answer.address}")
          
def scan_ports(target, start_port, end_port):
    
    for port in range(start_port, end_port + 1):
        syn_scan(target, port)   


def main():
    
    target = input("Enter the target IP address or hostname: ")
    port_range = input("Enter the port range to scan (e.g 1-100): ")
    dns_domain = input("Enter the domain for DNS scanning: ")
    
    
    start_port, end_port = map(int, port_range.split("-"))
    
    print(f"Scanning {target} for open ports in range {start_port}-{end_port}:")
    
    threads = []
    
    num_threads = 10
    chunk_size = (end_port - start_port + 1) // num_threads
    
    for i in range(num_threads):
        thread_start = start_port + i * chunk_size
        thread_end = thread_start + chunk_size - 1 if i != num_threads - 1 else end_port
        
        thread = threading.Thread(target=scan_ports, args = (target, thread_start, thread_end))
        threads.append(thread)
        thread.start()
    
    
    dns_scan(dns_domain)
    
if __name__ == "__main__":
  
      main()    
        
 