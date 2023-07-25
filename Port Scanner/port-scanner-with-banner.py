import socket

def grab_banner(target_host, port):
    
    try:
        # Create a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set a timeout so that the scan is not indefinite
        client_socket.settimeout(2)
        
        # Attempt to connect to the target host on the specified port
        client_socket.connect((target_host, port))
        
        # Receive the banner response (max 1024 bytes) from the service
        banner = client_socket.recv(1024).decode().strip()
        
        # Close the socket
        client_socket.close()
        
        return banner
    
    except (socket.error, socket.timeout):
        
        return ""
    

# Function to scan ports and grab banners

def scan_ports_with_banners(target_host, ports):
    
    # Create empty object to hold results
    
    open_ports_with_banners = {}
    
    for port in ports:
        banner = grab_banner(target_host, port)
        
        if banner:
            open_ports_with_banners[port] = banner
    
    return open_ports_with_banners

if __name__ == "__main__":
    
    target_host = input("Enter the target host (e.g. example.com): ")
    port_range = input("Enter the range of ports to scan (e.g. 1-100): ")
    
    try:
        start_port, end_port = map(int, port_range.split("-"))
        ports_to_scan = range(start_port, end_port + 1)
        
    except ValueError:
        print("Invalid port range input. Please provide a valid range.")
        
        exit(1)
        
    open_ports = []
    open_ports_with_banners = {}
    
    for port in ports_to_scan:
        
        try:
            # Create a socket object
            
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Set a timeout
            
            # client_socket.timeout(1)
            
            # Attempt to connect to the target host on current port
            
            result = client_socket.connect_ex((target_host, port))
            
            # If the connection is successful (port open), add it to the list
            
            if result == 0:
                
                open_ports.append(port)
                banner = grab_banner(target_host, port) 
                
                if banner:
                    open_ports_with_banners[port] = banner
                    
            # Close the socket
            
            client_socket.close()
            
        except socket.error:
            
            pass # Ignore any socket error and go to next port  
        
if open_ports:
     
    print(f"Open ports on {target_host}: {', '.join(map(str, open_ports))}")  
    print("Open ports with banners:")
     
    for port, banner in open_ports_with_banners.items():
        print(f"Port {port}: {banner}")
         
else:
    print(f"No open ports found on {target_host} in the specified range.")
    
       
        
    

        