import random

def main():
    "main function"
    
def numToName(portNumArray: list[str], portNameArray: list[str], portNumber: str) -> str:
    """
    This function takes in a list of port numbers, a list of corresponding protocol names, and a specific port number.
    It returns the protocol name corresponding to the given port number, or a message if the port number is not found.
    """
    if portNumber in portNumArray:  
        index = portNumArray.index(portNumber)
        return portNameArray[index]
    else:
        return "Port number not found"
    

def nameToNum(portNumArray, portNameArray, portName):
    result = []
    index = 0
    while index < len(portNameArray):
        if portNameArray[index] == portName:
            result.append(portNumArray[index])
        index += 1
    return result
    
def getInput():
    """
    This function prompts the user for input until a valid choice is entered.
    Valid choices are '1', '2', '3', or 'm'.
    """
    while True:
        user_input = input("Enter your choice (1, 2, 3, or 'm'): ").rstrip()
        if user_input in ['1', '2', '3', 'm']:
            return user_input
        else:
            print("Invalid input. Please enter 1, 2, 3, or 'm'.")

        main()

# Function to get the next port number and its corresponding protocol
def get_next_port_protocol(index):
    port_protocol_pairs = [
        (20, "FTP"),
        (21, "FTP"),
        (22, "SSH"),
        (23, "Telnet"),
        (25, "SMTP"),
        (53, "DNS"),
        (67, "DHCP"),
        (68, "DHCP"),
        (80, "HTTP"),
        (110, "POP3"),
        (137, "NetBIOS"),
        (139, "NetBIOS"),
        (143, "IMAP"),
        (161, "SNMP"),
        (162, "SNMP"),
        (389, "LDAP"),
        (443, "HTTPS"),
        (445, "SMB"),
        (3389, "RDP")
    ]
    length = len(port_protocol_pairs)
    # Use a mathematical function to simulate randomness
    next_index = (index * 3 + 7) % length
    return port_protocol_pairs[next_index]

# Function to get the next protocol and its corresponding port number
def get_next_protocol_port(index):
    port_protocol_pairs = [
        (20, "FTP"),
        (21, "FTP"),
        (22, "SSH"),
        (23, "Telnet"),
        (25, "SMTP"),
        (53, "DNS"),
        (67, "DHCP"),
        (68, "DHCP"),
        (80, "HTTP"),
        (110, "POP3"),
        (137, "NetBIOS"),
        (139, "NetBIOS"),
        (143, "IMAP"),
        (161, "SNMP"),
        (162, "SNMP"),
        (389, "LDAP"),
        (443, "HTTPS"),
        (445, "SMB"),
        (3389, "RDP")
    ]
    length = len(port_protocol_pairs)
    # Use a mathematical function to generate randomness
    next_index = (index * 5 + 11) % length
    return port_protocol_pairs[next_index]

# Function to check user's answer
def check_answer(question, answer):
    if answer == question[1]:
        return True
    else:
        return False

# Main program loop
def main():
    port_index = 0
    protocol_index = 0

    while True:
        print("Main Menu:")
        print("1. Given a port number, identify the PROTOCOL (use abbreviation).")
        print("2. Given a port protocol, identify a port NUMBER.")
        print("3. Exit")
        choice = input("Choice: ").strip()

        if choice == '1':
            print("Option 1: Identify the port's PROTOCOL.")
            question = get_next_port_protocol(port_index)
            port_index += 1
            user_answer = input(f"What is the protocol for port {question[0]} (m=Main Menu)? ").strip()
            if user_answer == 'M':
                continue
            elif check_answer(question, user_answer):
                print("Correct answer!")
            else:
                print(f"Incorrect. The correct answer is {question[1]}.")

        elif choice == '2':
            print("Option 2: Identify the port's NUMBER.")
            question = get_next_protocol_port(protocol_index)
            protocol_index += 1
            user_answer = input(f"What is the number for protocol {question[1]} (m=Main Menu)? ").strip()
            if user_answer == 'M':
                continue
            elif check_answer((question[1], user_answer), str(question[0])):
                print("Correct answer!")
            else:
                print(f"Incorrect. The correct answer is {question[0]}.")

        elif choice == '3':
            print("Program Complete. I hope this has helped in studying for the CompTIA A+ certification.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()