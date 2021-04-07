#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""
import crayons
# function to push commands
def commandpush(devicecmd): # devicecmd==list
    for coffeetime in devicecmd.keys():
        print(crayons.green('Handshaking. .. ... connecting with ' + coffeetime ))
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[coffeetime]:
            print(crayons.red('Attempting to sending command --> ' + mycmds ))
            # we'll learn to write code that sends cmds to device here

def devicereboot(x):
    for ip in x:
        print(f"\nConnecting to {ip}.")
    print("REBOOTING NOW!")    


# start our main script
def main():
    work2do = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":
    ["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]} 
    # data that replaces data stored in file

    ip_list = ["10.0.0.1", "10.0.0.2", "10.0.0.3"]

    print(crayons.blue("Welcome to the network device command pusher")) # welcome message

    ## get data set
    print(crayons.blue("\nData set found\n")) # replace with function call that reads in data from file

    ## run
    commandpush(work2do) # call function to push commands to devices

    devicereboot(ip_list)

# call our main function
main()