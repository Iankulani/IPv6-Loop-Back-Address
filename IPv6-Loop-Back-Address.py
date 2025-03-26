# -*- coding: utf-8 -*-
"""
Created on Tue March  26 08:345:47 2025

@author: IAN CARTER KULANI

"""

from colorama import Fore
import pyfiglet
import os
font=pyfiglet.figlet_format("IPv6 Loop Back Address")
print(Fore.GREEN+font)

# Function to generate IPv6 loopback address
def create_ipv6_loopback():
    print("IPv6 Loopback Address Generation")
    print("The default IPv6 loopback address is ::1.")

    # Asking if the user wants to customize the loopback address
    custom_address = input("Do you want to enter a custom loopback address (yes/no)? ").strip().lower()

    if custom_address == 'yes':
        # User can customize the address (usually, it's always ::1 for loopback, so we'll guide them)
        print("IPv6 loopback address is always a unique address for loopback traffic.")
        address = input("Enter the custom loopback address (it should typically be in the format 'xxxx:xxxx:xxxx:xxxx::1'): ").strip()
        
        # Check if the address is in correct format (basic validation)
        if address.count("::") == 1 and address.endswith("::1"):
            print(f"Custom IPv6 Loopback Address: {address}")
        else:
            print("Invalid address format. Using default loopback address ::1")
            address = "::1"

    else:
        # Using default IPv6 loopback address
        address = "::1"
        print(f"Using default IPv6 Loopback Address: {address}")
    
    return address

# Main function
def main():
    ipv6_address = create_ipv6_loopback()
    print(f"Your configured IPv6 loopback address is: {ipv6_address}")

# Run the program
if __name__ == "__main__":
    main()
