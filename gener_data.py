# Imports

import sys
import os
import random

# Variables

min_packet_size = 50
max_packet_size = 1400
separator = ','

# Functions

def get_ping(packet_size) :
    """get a ping time for the given packet size"""
    return os.popen("ping -c 1 -s %s www.youtube.com | tail -1 | awk '{print$4}' | cut -d '/' -f 2" % (packet_size)).read()

def gener_data(file_name,n) :
    """adds n random couples (packet_size,ping_time) to file data.dat"""
    for _ in range(n) :        
        data_file = open(file_name, 'a')
        packet_size = random.randint(min_packet_size,max_packet_size)
        ping_time = get_ping(packet_size) #type str
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
