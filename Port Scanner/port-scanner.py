import socket

def scan_ports(target_host, ports):
    
    open_ports = [] # create an empty list to store port results
    
    for port in ports:
        try:
            # Create a socket object
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
                # AF-INET = socket address family for IPv4
                # SOCK_STREAM = socket type for TCP
            
            # Set a timeout to prevent the scan from hanging indefinitely on closed ports
            client_socket.settimeout(1)
            
            # Attempt to connect to the target host on the current port
            result = client_socket.connect_ex((target_host, port))
            
            # If the connection was successful (port is open), add it to the list
            if result == 0:
                open_ports.append(port)
            
            # Close the socket
            client_socket.close()
            
        except socket.error:
            pass  # Ignore any socket errors and move to the next port

    return open_ports

if __name__ == "__main__":
    # Get the host address and port number from the user
    
    target_host = input("Enter the target host (e.g., example.com): ")
    port_range = input("Enter the range of ports to scan (e.g., 1-100): ")

    try:
        start_port, end_port = map(int, port_range.split("-"))
        ports_to_scan = range(start_port, end_port + 1)
        
    except ValueError: # check that the port range is correct
        
        print("Invalid port range input. Please provide a valid range (e.g., 1-100).")
        exit(1)

    open_ports = scan_ports(target_host, ports_to_scan) # call the main function to scan ports with the user parameters

    # Print out the output
    if open_ports:
        print(f"Open ports on {target_host}: {', '.join(map(str, open_ports))}") 
    else:
        print(f"No open ports found on {target_host} in the specified range.")
