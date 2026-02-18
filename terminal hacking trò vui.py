#pylint:disable=W0611
#pylint:disable=W2402
import time
import random
import math
import security_md
class TerminalHackSimulator:
    def __init__(self):
        self.commands = ["log/var/ls", "cat/etc/passwd", "clear","run","roblox","file/install", "sys/exit"]
        self.log = []
    
    def display_welcome(self):
        print("Welcome to the Terminal Hack Simulator")
        print("Type 'sys/exit' 'log/var/ls' 'cat/etc/passwd' to leave  the simulator.")
    
    def log_command(self, command):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.log.append(f"{timestamp} - {command}")
    
    def show_log(self):
        print("\n--- Command Log ---")
        for entry in self.log:
            print(entry)
        print("-------------------\n")
    
    def run(self):
        self.display_welcome()
        while True:
            command = input("》》》 ")
            self.log_command(command)
            
            if command == "sys/exit":
                self.show_log()
                print("Exiting the simulator. Goodbye!")
                break
            elif command in self.commands:
                print(f"sys/terminal/Executing: {command}")
                time.sleep(1)  # Simulate processing time
                print("# "+str(2+int(1>0))+"%")
                print("### "+str(23+int(23>4))+"%")
                print("###### "+str(47+int(47>8))+"%")
                print("######### "+str(99)+"%")
                print("###########"+str(100)+"%")
                print("《《Success.》》")
            else:
                print("Error: Command not found.")
            

if __name__ == "__main__":
    simulator = TerminalHackSimulator()
    simulator.run()