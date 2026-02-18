#pylint:disable=W2402
#pylint:disable=W0612
#pylint:disable=W3101
#pylint:disable=W0718
#pylint:disable=W1203
import os
import logging
import socket
import requests
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import json
import platform
import getpass

# Thiết lập logging
logging.basicConfig(filename='security_tool.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SecurityTool:
    def __init__(self):
        self.users = self.load_users()
        self.key = None

    def load_users(self):
        if os.path.exists('users.json'):
            with open('users.json', 'r') as f:
                return json.load(f)
        return {}

    def save_users(self):
        with open('users.json', 'w') as f:
            json.dump(self.users, f)

    def add_user(self, username, password):
        if username in self.users:
            logging.warning(f"User {username} already exists.")
            return False
        self.users[username] = password
        self.save_users()
        logging.info(f"User {username} added successfully.")
        return True

    def authenticate_user(self, username, password):
        return self.users.get(username) == password

    def scan_ip(self, ip_range):
        logging.info(f"Scanning IP range: {ip_range}")
        active_ips = []
        for i in range(1, 255):
            ip = f"{ip_range}.{i}"
            try:
                socket.gethostbyaddr(ip)
                active_ips.append(ip)
                logging.info(f"Active IP found: {ip}")
            except socket.herror:
                continue
        return active_ips

    def hide_ip(self):
        try:
            response = requests.get('http://api.ipify.org?format=json')
            logging.info(f"Current IP: {response.json()['ip']}")
            return response.json()['ip']
        except Exception as e:
            logging.error(f"Error hiding IP: {str(e)}")
            return None

    def encrypt_data(self, data):
        self.key = get_random_bytes(16)  # Khóa AES 128-bit
        cipher = AES.new(self.key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(data.encode('utf-8'))#utf = 8,16,32
        return (ciphertext, cipher.nonce, tag)

    def display_system_info(self):
        info = f"""
        System Information:
        --------------------
        OS: {platform.system()} {platform.release()}
        Processor: {platform.processor()}
        Architecture: {platform.architecture()[0]}
        """
        print(info)
        logging.info("Displayed system information.")

    def run(self):
        print("Welcome to the Security Tool")
        print("------------------------------")
        while True:
            print("\nMenu:")
            print("---------------------1. Add User------------------")
            print("--------------------2. Authenticate User----------")
            print("%~~~                        3. Scan IP")
            print("^^^^                            4. Hide IP")
            print(" >>>>>                       5.Encrypt Data")
            print(" //////                           6.DisplaySystemInfo")
            print("   *******                     7.Exit=====>")
            
            choice = input("Choose an option: ")
            
            if choice == '1':
                username = input("Enter username: ")
                password = getpass.getpass("Enter password: ")
                self.add_user(username, password)
            elif choice == '2':
                username = input("Enter username: ")
                password = getpass.getpass("Enter password: ")
                if self.authenticate_user(username, password):
                    print("Authentication successful.")
                else:
                    print("Authentication failed.")
            elif choice == '3':
                ip_range = input("Enter IP range (e.g., 192.168.1): ")
                active_ips = self.scan_ip(ip_range)
                print("Active IPs:", active_ips)
            elif choice == '4':
                current_ip = self.hide_ip()
                if current_ip:
                    print("Your current IP is hidden:", current_ip)
            elif choice == '5':
                data = input("Enter data to encrypt: ")
                ciphertext, nonce, tag = self.encrypt_data(data)
                print(f"Encrypted data: {ciphertext.hex()}")
                logging.info("Data encrypted successfully.")
            elif choice == '6':
                self.display_system_info()
            elif choice == '7':
                logging.info("Exiting the tool.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    tool = SecurityTool()
    tool.run()