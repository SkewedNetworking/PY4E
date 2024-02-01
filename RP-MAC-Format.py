def format_mac_address(mac_address):
    # Remove any punctuation from the MAC address
    mac_address = ''.join(char for char in mac_address if char.isalnum())

    # Verify proper MAC address length (should be 12)
    if len(mac_address) != 12:
        return "Invalid MAC address length. Please enter a 12-character MAC address."

    # Format the MAC address in different patterns
    patterns = [
        ':'.join([mac_address[i:i + 2] for i in range(0, 12, 2)]),
        ':'.join([mac_address[i:i + 4] for i in range(0, 12, 4)]),
        '-'.join([mac_address[i:i + 2] for i in range(0, 12, 2)]),
        '-'.join([mac_address[i:i + 4] for i in range(0, 12, 4)]),
        '.'.join([mac_address[i:i + 2] for i in range(0, 12, 2)]),
        '.'.join([mac_address[i:i + 4] for i in range(0, 12, 4)]),"\n"
    ]

    # Return the formatted MAC addresses
    return '\n'.join(patterns)

# Get MAC address input from the user
print("\nUtilize this program to take a MAC address and convert it into various formats. \nUseful for taking a MAC address and having a list of various MAC-formats to input into various monitoring systems / searches.\nFormats returned are:\n\n\txx:xx:xx:xx:xx:xx\n\txxxx:xxxx:xxxx\n\txx-xx-xx-xx-xx-xx\n\txxxx-xxxx-xxxx\n\txx.xx.xx.xx.xx.xx\n\txxxx.xxxx.xxxx\n\nWhen you are ready to exit the program, type 'exit'.\n")

#Enter infinite loop
while True:
    user_mac = input("Enter a MAC address:\n\n")
    # If user enters "quit", it will exit the program.
    if user_mac.lower() == 'exit':
        break
    # Send variable 'user_mac' to function "format_mac_address" and assign returned value to variable 'formatted_mac_address'
    # Then print it!
    formatted_mac_address = format_mac_address(user_mac)
    print(formatted_mac_address)