import ipaddress

def calculate_subnet(ip_with_cidr):
    try:
        # Create an IPv4 network object
        # strict=False allows the user to enter a host IP rather than the exact network ID
        network = ipaddress.IPv4Network(ip_with_cidr, strict=False)
        
        print(f"\n--- Subnet Details for {ip_with_cidr} ---")
        print(f"Network Address:   {network.network_address}")
        print(f"Broadcast Address: {network.broadcast_address}")
        print(f"Subnet Mask:       {network.netmask}")
        print(f"Total IPs:         {network.num_addresses}")
        
        # Subtracting 2 for Network and Broadcast addresses
        usable_hosts = network.num_addresses - 2 if network.num_addresses > 2 else 0
        print(f"Usable Hosts:      {usable_hosts}")
        
        # Get the range of usable IPs
        hosts = list(network.hosts())
        if hosts:
            print(f"Usable IP Range:   {hosts[0]} - {hosts[-1]}\n")
        else:
            print("Usable IP Range:   None (Point-to-Point or Host Route)\n")
            
    except ValueError as e:
        print(f"\nError: Invalid IP or CIDR notation. Make sure it looks like 192.168.1.0/24\nDetails: {e}\n")

if __name__ == "__main__":
    print("Welcome to the Subnet Calculator!")
    while True:
        user_input = input("Enter an IP address with CIDR (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        calculate_subnet(user_input)