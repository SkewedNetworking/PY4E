def format_mac_address(mac_address):
    # Remove punctuation from the MAC address
    mac_address = ''.join(char for char in mac_address if char.isalnum())

    # Verify proper MAC address legth (should be 12)
    if len(mac_address) != 12:
        return "Invalid MAC address. Please enter a 12-character MAC address."

    # Format the MAC address in different patterns
    patterns = [
        ':'.join([mac_address[i:i + 2] for i in range(0, 12, 2)]),
        ':'.join([mac_address[i:i + 4] for i in range(0, 12, 4)]),
        '-'.join([mac_address[i:i + 2] for i in range(0, 12, 2)]),
        '-'.join([mac_address[i:i + 4] for i in range(0, 12, 4)]),
        '.'.join([mac_address[i:i + 2] for i in range(0, 12, 2)]),
        '.'.join([mac_address[i:i + 4] for i in range(0, 12, 4)]),
    ]

    # Return the formatted MAC addresses
    return '\n'.join(patterns)

# Get MAC address input from the user
user_mac = input("Utilize this program to take a MAC address and convert it into various formats. \nUseful for taking a MAC address and having a list of various MAC-formats to intput into logging systems / searches.\nFormats returned are:\n\txx:xx:xx:xx:xx:xx\n\txxxx:xxxx:xxxx\n\txx-xx-xx-xx-xx-xx\n\txxxx-xxxx-xxxx\n\txx.xx.xx.xx.xx.xx\n\txxxx.xxxx.xxxx\nEnter a MAC address: ")

# Format and print the result
formatted_mac_address = format_mac_address(user_mac)
print(formatted_mac_address)