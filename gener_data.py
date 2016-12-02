# Imports

import sys
import os
import random

# Variables

min_packet_size = 11000
max_packet_size = 12500
separator = ','

# Functions

def get_ping(packet_size) :
    """get a ping time for the given packet size"""
    ping_time = os.popen("ping -c 1 -s %s 77.95.65.117 | tail -1 | awk '{print$4}' | cut -d '/' -f 2" % (packet_size)).read()
    if len(ping_time)>1 :
        return ping_time
    else :
        return 0

def gener_data(file_name,n) :
    """adds n random couples (packet_size,ping_time) to file data.dat"""
            
    data_file = open(file_name, 'a')
    for _ in range(n) :    
        packet_size = random.randint(min_packet_size,max_packet_size)
        ping_time = get_ping(packet_size) #type str
        if (ping_time != 0):
            data_file.write(str(packet_size)+separator+ping_time)
    data_file.close()

# Main

def main():
    assert len(sys.argv) == 3, "2 expected arguments : file_name and n"
    file_name = sys.argv[1]
    n = int(sys.argv[2])
    gener_data(file_name,n)

if __name__ == '__main__':
    main()
