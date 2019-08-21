import txt_logger

import sys
import subprocess

ips_txt_path = 'C:\\Users\\Brandon\\Documents\\Personal_Projects\\nord_utils\\ips.txt'

NORD_EXE_PATH = "C:\\Program Files (x86)\\NordVPN\\nordvpn" #>nordvpn -c -i 103.86.98.7



def ip_by_index(index):
    lines = txt_logger.readTxt(ips_txt_path)
    return lines[index]


# NORD Commands

def disconnect():
    subprocess.call(NORD_EXE_PATH + ' -d')
    
def connect_by_ip(ip):
    subprocess.call(NORD_EXE_PATH + ' -c -i ' + ip)
    








# disconnect()
connect_by_ip('103.208.220.117')
# print(ip_by_index(2))
# print(sys.argv)
# index = int(sys.argv[1])
# text_file = open("C:\\Users\\Brandon\\Documents\\Personal_Projects\\nord_utils\\Output.txt", "w")
# text_file.write(ip_by_index(index))
# text_file.close()






