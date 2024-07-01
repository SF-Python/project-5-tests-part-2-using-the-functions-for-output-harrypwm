import random
# Function to randomly select a port number and its corresponding protocol

def main():
    "main function"
    
def numToName(portNumArray: list[str], portNameArray: list[str], portNumber: str) -> str:
    if portNumber in portNumArray:
        index = portNumArray.index(portNumber)
        return portNameArray[index]
    else:
        return "Port number not found"
    
def nameToNum(portNumArray: list[str], portNameArray: list[str], portName: str) -> list[str]:
    indices = [i for i, x in enumerate(portNameArray) if x == portName]
    if indices:
        return [portNumArray[i] for i in indices]
    else:
        return ["Port name not found"]
    
def getInput():
    while True:
        user_input = input("Enter your choice (1, 2, 3, or 'm'): ").rstrip()
        if user_input in ['1', '2', '3', 'm']:
            return user_input
        else:
            print("Invalid input. Please enter 1, 2, 3, or 'm'.")

        main()


def random_port_protocol():
   port_protocol_pairs = {
       20: "FTP",
       21: "FTP",
       22: "SSH",
       23: "Telnet",
       25: "SMTP"
   }
   port = random.choice(list(port_protocol_pairs.keys()))
   return port, port_protocol_pairs[port]
# Function to randomly select a protocol and its corresponding port number
def random_protocol_port():
   port_protocol_pairs = {
       20: "FTP",
       21: "FTP",
       22: "SSH",
       23: "Telnet",
       25: "SMTP"
   }
   protocol = random.choice(list(port_protocol_pairs.values()))
   ports = [port for port, prot in port_protocol_pairs.items() if prot == protocol]
   port = random.choice(ports)
   return protocol, port
# Function to check user's answer
def check_answer(question, answer):
   if answer == question[1]:
       return True
   else:
       return False
# Main program loop
def main():
   while True:
       print("Choose an option:")
       print("1. Given a port number, identify the PROTOCOL")
       print("2. Given a port protocol, identify a port NUMBER")
       print("3. Exit")
       choice = input("Enter your choice (1/2/3): ")
       if choice == '1':
           print("Identify the protocol for the given port number:")
           question = random_port_protocol()
           user_answer = input(f"What protocol is associated with port {question[0]}? ").strip().upper()
           if user_answer == 'M':
               continue
           elif check_answer(question, user_answer):
               print("Correct!")
           else:
               print("Incorrect. The correct answer is:", question[1])
       elif choice == '2':
           print("Identify the port number for the given protocol:")
           question = random_protocol_port()
           user_answer = input(f"What port is associated with the protocol {question[0]}? ").strip().upper()
           if user_answer == 'M':
               continue
           elif check_answer(question, user_answer):
               print("Correct!")
           else:
               print("Incorrect. The correct answer is:", question[1])
       elif choice == '3':
           print("Exiting the program.")
           break
       else:
           print("Invalid choice. Please enter 1, 2, or 3.")
if __name__ == "__main__":
   main()